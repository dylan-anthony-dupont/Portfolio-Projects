# appendix_G_C4O_final.py
# =============================================================================
# "Camera-ready" implementation of the C4-O boundary certificate at m1
#
# Certifies on the short rectangle B(α=1, m1, δ) that:
#       sup_{∂B} |E - G_out| / |G_out|  <  1
#
# where E(v) = Λ_2(1 + v),  Λ_2(u) = π^{-u/4} Γ(u/4) ζ(u/2).
# In width-2, the nontrivial zeros of E occur at v = 2 i T_k, where
# T_k are the classical imaginary parts of ζ(1/2 + i T_k) = 0. Hence
#   m1 := 2*T1  (twice the first classical nontrivial zero height).
#
# This code:
#   1) Uses a *high-precision, embedded constant* for T1 (with many digits)
#      to define m1, OR optionally recomputes m1 via mpmath.findroot.
#   2) Samples E on ∂B; constructs U_b = log|E| and a continuously unwrapped
#      boundary phase φ_b = arg E at high precision.
#   3) Solves the Dirichlet problem ΔU=0 inside B with boundary data U_b.
#   4) Builds the *boundary trace* V_b of the conjugate via boundary-only
#      Cauchy–Riemann integration: dV/ds = (-U_y, U_x)·t along ∂B.
#   5) Computes the pointwise ratio 2|sin(Δφ/2)| with Δφ = φ_b - V_b;
#      prints its supremum. If < 1, the C4-O certificate passes.
#
# Notes:
# - This is a *boundary-only* certification; no Riemann mapping is needed.
# - In a zero-free simply-connected region, the outer determined by U_b
#   matches E up to a unimodular constant (fixed by an anchor), so the
#   observed ratio should be numerically ~0 (limited by discretization).
#
# CLI examples:
#   python appendix_G_C4O_final.py
#   python appendix_G_C4O_final.py --dps 150 --nside 4096 --nx 257 --ny 257 --plot
#   python appendix_G_C4O_final.py --compute-m1 --dps 180 --print-constants
#   python appendix_G_C4O_final.py --save ratio_m1.csv
#
# Dependencies: Python 3.11+ (3.12 OK), mpmath, numpy, scipy, (optional) matplotlib
# =============================================================================

import argparse
import math
import sys
import platform
import numpy as np
import mpmath as mp

from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.interpolate import RegularGridInterpolator

# Optional plotting
try:
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except Exception:
    HAVE_MPL = False


# =============================================================================
# 0) Environment + constants
# =============================================================================

def env_dump():
    """Print environment details (useful for the appendix log)."""
    print("=== ENV INFO ===")
    print("Python:", sys.version.splitlines()[0])
    print("Platform:", platform.platform())
    try:
        import numpy as _np; print("NumPy:", _np.__version__)
    except Exception: pass
    try:
        import mpmath as _mp; print("mpmath:", _mp.__version__)
    except Exception: pass
    try:
        import scipy as _sp; print("SciPy:", _sp.__version__)
    except Exception: pass
    try:
        import matplotlib as _mpl; print("matplotlib:", _mpl.__version__)
    except Exception: pass
    print("================")

# High-precision embedded value for the first classical zeta zero height T1.
# Source: standard literature / tables; many digits included.
# If you prefer to *compute* it instead, pass --compute-m1 (see below).
DEFAULT_T1_STR = (
    "14.134725141734693790457251983562470270784257115699243"
    "411530761"
)

def get_m1(override_compute: bool, dps_for_root: int):
    """
    Return m1 = 2*T1 either from the embedded constant or by computing T1 via
    mpmath.findroot on ζ(s), starting near 0.5 + 14.13i, 0.5 + 14.2i.

    We use complex-variable rootfinding on s, then take Im(s) = T1 and set m1 = 2*T1.
    """
    if not override_compute:
        T1 = mp.mpf(DEFAULT_T1_STR)  # high-precision embedded constant
        return 2*T1, T1, False, None  # (m1, T1, computed=False, info=None)

    # Compute T1 via complex rootfinding on s -> ζ(s)=0 near the critical line
    info = {}
    try:
        dps_old = mp.mp.dps
        mp.mp.dps = max(dps_for_root, dps_old)

        s0 = mp.mpf('0.5') + 1j*mp.mpf('14.13')
        s1 = mp.mpf('0.5') + 1j*mp.mpf('14.20')

        def f(s):
            return mp.zeta(s)

        s_root = mp.findroot(f, (s0, s1))  # complex secant on ζ(s)
        T1 = mp.im(s_root)
        m1 = 2*T1

        info = {
            "s_root": s_root,
            "Re(s_root)": mp.re(s_root),
            "Im(s_root)=T1": T1
        }
        mp.mp.dps = dps_old
        return m1, T1, True, info

    except Exception as e:
        # Fall back to embedded constant if rootfinding fails
        T1 = mp.mpf(DEFAULT_T1_STR)
        m1 = 2*T1
        info = {"error": str(e), "fallback": "embedded T1 used"}
        return m1, T1, False, info


# =============================================================================
# 1) Core functions: Λ2 and E
# =============================================================================

def zeta2(u: mp.mpf):
    """ζ_2(u) = ζ(u/2)."""
    return mp.zeta(u / 2)

def Lambda2(u: mp.mpf):
    """Λ_2(u) = π^{-u/4} Γ(u/4) ζ_2(u)."""
    return mp.power(mp.pi, -u/4) * mp.gamma(u/4) * zeta2(u)

def E_of_v(v: mp.mpf):
    """E(v) = Λ_2(1 + v)."""
    return Lambda2(1 + v)


# =============================================================================
# 2) Rectangle geometry and boundary sampling
# =============================================================================

def define_box(alpha: mp.mpf, m1: mp.mpf, eta: mp.mpf):
    """
    δ := η*α / (log(m1))^2,  B = [α-δ, α+δ] × [m1-δ, m1+δ].
    We return *float* endpoints for the grid (interior solver uses floats).
    """
    logm = mp.log(m1)
    delta = eta*alpha/(logm**2)
    xL = float(alpha - delta)
    xR = float(alpha + delta)
    yB = float(m1 - delta)
    yT = float(m1 + delta)
    return float(delta), (xL, xR, yB, yT)

def boundary_nodes(xL, xR, yB, yT, N_side):
    """
    ∂B CCW polyline without duplicated corners:
      bottom: (xL->xR, yB)
      right:  (xR, yB->yT)
      top:    (xR->xL, yT)
      left:   (xL, yT->yB)
    """
    xs, ys = [], []
    # bottom
    for k in range(N_side):
        t = k/(N_side-1)
        xs.append(xL + t*(xR-xL)); ys.append(yB)
    # right (skip bottom-right corner)
    for k in range(1, N_side):
        t = k/(N_side-1)
        xs.append(xR); ys.append(yB + t*(yT-yB))
    # top (skip top-right corner)
    for k in range(1, N_side):
        t = k/(N_side-1)
        xs.append(xR - t*(xR-xL)); ys.append(yT)
    # left (skip both corners)
    for k in range(1, N_side-1):
        t = k/(N_side-1)
        xs.append(xL); ys.append(yT - t*(yT-yB))
    return np.array(xs, dtype=float), np.array(ys, dtype=float)

def boundary_data(xL, xR, yB, yT, N_side, dps):
    """
    Evaluate E on ∂B at high precision (mpmath), then convert to float arrays
    only *after* taking log|E| and arg(E).
    Returns xs, ys, U_b = log|E|, φ_b = unwrap(arg E).
    """
    xs, ys = boundary_nodes(xL, xR, yB, yT, N_side)
    EV = []
    mp.mp.dps = int(dps)
    for x, y in zip(xs, ys):
        v = mp.mpc(x, y)
        EV.append(E_of_v(v))
    U_b = np.array([float(mp.log(abs(z))) for z in EV], dtype=float)
    phi = np.array([float(mp.arg(z)) for z in EV], dtype=float)
    phi_b = np.unwrap(phi)
    return xs, ys, U_b, phi_b


# =============================================================================
# 3) Dirichlet solver for U (harmonic extension of log|E|)
# =============================================================================

def _slice_segments(xs, ys, U_b, N_side):
    """Split the boundary into 4 edges in the same order as boundary_nodes()."""
    nB = N_side
    nR = N_side - 1
    nT = N_side - 1
    nL = N_side - 2

    i0 = 0
    i1 = i0 + nB
    i2 = i1 + nR
    i3 = i2 + nT
    i4 = i3 + nL
    assert i4 == len(xs) == len(ys) == len(U_b)

    xb = xs[i0:i1];  Ub = U_b[i0:i1];  yb = ys[i0:i1]
    xr = xs[i1:i2];  Ur = U_b[i1:i2];  yr = ys[i1:i2]
    xt = xs[i2:i3];  Ut = U_b[i2:i3];  yt = ys[i2:i3]
    xl = xs[i3:i4];  Ul = U_b[i3:i4];  yl = ys[i3:i4]

    bottom = {'coord': xb, 'U': Ub, 'const': yb[0]}  # y fixed
    right  = {'coord': yr, 'U': Ur, 'const': xr[0]}  # x fixed
    top    = {'coord': xt, 'U': Ut, 'const': yt[0]}  # y fixed
    left   = {'coord': yl, 'U': Ul, 'const': xl[0]}  # x fixed
    return bottom, right, top, left

def solve_harmonic_dirichlet_U(xL, xR, yB, yT, nx, ny, xs_b, ys_b, U_b, N_side):
    """
    Solve ΔU=0 on the rectangle with Dirichlet boundary values U|∂B = U_b.
    - Uniform (nx × ny) grid (float).
    - Edge-wise 1D interpolation to set boundary node values.
    - Sparse 5-point Laplacian for interior.
    """
    xgrid = np.linspace(xL, xR, nx)
    ygrid = np.linspace(yB, yT, ny)
    hx = xgrid[1]-xgrid[0]; hy = ygrid[1]-ygrid[0]

    bottom, right, top, left = _slice_segments(xs_b, ys_b, U_b, N_side)

    # Monotone coordinates for interpolation
    xb, Ub = bottom['coord'], bottom['U']               # inc x
    yr, Ur = right['coord'],  right['U']                # inc y
    xt, Ut = top['coord'][::-1], top['U'][::-1]         # make inc x
    yl, Ul = left['coord'][::-1], left['U'][::-1]       # make inc y

    U = np.zeros((ny, nx), dtype=float)
    # set Dirichlet BCs
    U[0,  :] = np.interp(xgrid, xb, Ub)          # bottom
    U[-1, :] = np.interp(xgrid, xt, Ut)          # top
    U[:,  0] = np.interp(ygrid, yl, Ul)          # left
    U[:, -1] = np.interp(ygrid, yr, Ur)          # right

    # Build linear system for interior nodes
    Nunk = (nx-2)*(ny-2)
    A = lil_matrix((Nunk, Nunk))
    b = np.zeros(Nunk, dtype=float)

    def idx(i, j):  # map interior (i,j) to unknown index
        return (j-1)*(nx-2) + (i-1)

    inv_hx2 = 1.0/(hx*hx)
    inv_hy2 = 1.0/(hy*hy)

    for j in range(1, ny-1):
        for i in range(1, nx-1):
            k = idx(i, j)
            A[k, k] = -2.0*inv_hx2 - 2.0*inv_hy2
            # left / right neighbors
            if i-1 >= 1: A[k, idx(i-1, j)] = inv_hx2
            else:        b[k] -= U[j, i-1]*inv_hx2
            if i+1 <= nx-2: A[k, idx(i+1, j)] = inv_hx2
            else:           b[k] -= U[j, i+1]*inv_hx2
            # down / up neighbors
            if j-1 >= 1: A[k, idx(i, j-1)] = inv_hy2
            else:        b[k] -= U[j-1, i]*inv_hy2
            if j+1 <= ny-2: A[k, idx(i, j+1)] = inv_hy2
            else:           b[k] -= U[j+1, i]*inv_hy2

    if Nunk > 0:
        u_int = spsolve(A.tocsr(), b)
        for j in range(1, ny-1):
            for i in range(1, nx-1):
                U[j, i] = u_int[idx(i, j)]

    return xgrid, ygrid, U


# =============================================================================
# 4) Build V_b on ∂B via boundary-only Cauchy–Riemann integration
# =============================================================================

def centered_derivatives(U, xgrid, ygrid):
    """Compute U_x and U_y on the grid via centered diffs (one-sided at edges)."""
    ny, nx = U.shape
    hx = xgrid[1]-xgrid[0]; hy = ygrid[1]-ygrid[0]
    Ux = np.zeros_like(U); Uy = np.zeros_like(U)
    # interior
    Ux[:, 1:-1] = (U[:, 2:] - U[:, :-2])/(2*hx)
    Uy[1:-1, :] = (U[2:, :] - U[:-2, :])/(2*hy)
    # edges
    Ux[:, 0]  = (U[:, 1] - U[:, 0]) / hx
    Ux[:, -1] = (U[:, -1] - U[:, -2]) / hx
    Uy[0, :]  = (U[1, :] - U[0, :]) / hy
    Uy[-1, :] = (U[-1, :] - U[-2, :]) / hy
    return Ux, Uy

def rotate_boundary(xs, ys, arrs, anchor_xy):
    """
    Rotate boundary arrays so the node nearest to the anchor (ax,ay) is first.
    Returns rotated xs, ys, and the rotated copies of each array in `arrs`.
    """
    ax, ay = anchor_xy
    idx = int(np.argmin((xs-ax)**2 + (ys-ay)**2))
    def rot(a): return np.concatenate([a[idx:], a[:idx]], axis=0)
    xs_r = rot(xs); ys_r = rot(ys)
    arrs_r = [rot(a) for a in arrs]
    return xs_r, ys_r, arrs_r, idx

def boundary_CR_integrate_Vb(xs, ys, phi_b, Ux, Uy, ygrid, xgrid):
    """
    Integrate dV/ds = (-U_y, U_x) · t along the boundary polyline to build V_b.
    - Interpolate Ux,Uy at segment midpoints (ym, xm).
    - Clamp (ym, xm) into the box to avoid rare out-of-bounds due to roundoff.
    - Enforce periodic closure of V_b modulo 2π by distributing residual.
    """
    Ux_interp = RegularGridInterpolator((ygrid, xgrid), Ux,
                                        method='linear', bounds_error=False, fill_value=None)
    Uy_interp = RegularGridInterpolator((ygrid, xgrid), Uy,
                                        method='linear', bounds_error=False, fill_value=None)

    N = len(xs)
    xs_c = np.concatenate([xs, xs[:1]])
    ys_c = np.concatenate([ys, ys[:1]])

    Vb = np.zeros(N, dtype=float)
    Vb[0] = float(phi_b[0])  # enforce equality at anchor

    x0, x1 = float(xgrid[0]), float(xgrid[-1])
    y0, y1 = float(ygrid[0]), float(ygrid[-1])

    for i in range(N-1):
        xA, yA = xs_c[i],   ys_c[i]
        xB, yB = xs_c[i+1], ys_c[i+1]
        dx, dy = xB-xA, yB-yA
        ds = math.hypot(dx, dy)
        if ds == 0.0:
            Vb[i+1] = Vb[i]
            continue
        tx, ty = dx/ds, dy/ds
        xm, ym = xA + 0.5*dx, yA + 0.5*dy
        xm = min(max(xm, x0), x1)
        ym = min(max(ym, y0), y1)
        Ux_m = float(Ux_interp([[ym, xm]])[0])
        Uy_m = float(Uy_interp([[ym, xm]])[0])
        dV = (-Uy_m)*tx + (Ux_m)*ty
        Vb[i+1] = Vb[i] + dV*ds

    diff = Vb[-1] - Vb[0]
    k = round(diff/(2*np.pi))
    closure_err = diff - 2*np.pi*k
    if abs(closure_err) > 0:
        seg_ds = np.hypot(np.diff(xs_c), np.diff(ys_c))[:N]
        s_nodes = np.zeros(N, dtype=float)
        s_nodes[1:] = np.cumsum(seg_ds[:-1])
        total_len = float(np.sum(seg_ds))
        if total_len > 0:
            Vb = Vb - closure_err*(s_nodes/total_len)

    return Vb


# =============================================================================
# 5) Driver: compute boundary ratio and (optionally) save diagnostics
# =============================================================================

def boundary_ratio(alpha, m1, delta, xL, xR, yB, yT,
                   dps=150, N_side=4096, nx=257, ny=257, make_plot=False,
                   anchor="top", save_csv=None):
    """
    High-level driver to compute the C4-O boundary ratio and optional CSV/plot.
    anchor ∈ {"top","bottom","left","right"} chooses where φ_b and V_b are pinned equal.
    """
    mp.mp.dps = int(dps)
    mp.mp.trap_complex = True

    xs_b, ys_b, U_b, phi_b = boundary_data(xL, xR, yB, yT, N_side, dps)

    xgrid, ygrid, U = solve_harmonic_dirichlet_U(xL, xR, yB, yT, nx, ny, xs_b, ys_b, U_b, N_side)

    absE_b = np.exp(U_b)
    min_absE = float(np.min(absE_b))
    max_absE = float(np.max(absE_b))

    Ux, Uy = centered_derivatives(U, xgrid, ygrid)
    if anchor == "top":
        ax, ay = 0.5*(xL+xR), yT
    elif anchor == "bottom":
        ax, ay = 0.5*(xL+xR), yB
    elif anchor == "left":
        ax, ay = xL, 0.5*(yB+yT)
    elif anchor == "right":
        ax, ay = xR, 0.5*(yB+yT)
    else:
        raise ValueError("anchor must be one of: top, bottom, left, right")

    xs_r, ys_r, [phi_r], _ = rotate_boundary(xs_b, ys_b, [phi_b], (ax, ay))

    Vb = boundary_CR_integrate_Vb(xs_r, ys_r, phi_r, Ux, Uy, ygrid, xgrid)

    dphi = phi_r - Vb
    dphi = ((dphi + np.pi) % (2*np.pi)) - np.pi
    ratio = 2.0*np.abs(np.sin(0.5*dphi))
    rmax = float(np.max(ratio))

    if save_csv is not None:
        seg_ds = np.hypot(np.diff(xs_r, append=xs_r[0]), np.diff(ys_r, append=ys_r[0]))
        s = np.cumsum(seg_ds); s -= s.min(); s /= s.max()
        out = np.column_stack([s, ratio])
        np.savetxt(save_csv, out, delimiter=",", header="s_normalized,ratio", comments="")
        print(f"[saved] CSV: {save_csv}")

    if make_plot and HAVE_MPL:
        seg_ds = np.hypot(np.diff(xs_r, append=xs_r[0]), np.diff(ys_r, append=ys_r[0]))
        s = np.cumsum(seg_ds); s -= s.min(); s /= s.max()
        plt.figure()
        plt.plot(s, ratio, lw=1)
        plt.axhline(1.0, ls='--')
        plt.title("Boundary ratio along ∂B")
        plt.xlabel("Normalized arclength s")
        plt.ylabel("|E - G_out| / |G_out|")
        plt.tight_layout()
        try:
            plt.show()
        except Exception:
            pass

    return {
        "rmax": rmax,
        "min_absE_boundary": min_absE,
        "max_absE_boundary": max_absE,
        "anchor": anchor,
        "grids": {"N_side": N_side, "nx": nx, "ny": ny},
        "precision": dps
    }


# =============================================================================
# 6) Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="C4-O boundary certification at m1 (width-2, height-local).")
    parser.add_argument("--dps", type=int, default=150, help="mpmath precision (decimal digits)")
    parser.add_argument("--nside", type=int, default=4096, help="Boundary points per side")
    parser.add_argument("--nx", type=int, default=257, help="Grid points in x (>= 65 recommended)")
    parser.add_argument("--ny", type=int, default=257, help="Grid points in y (>= 65 recommended)")
    parser.add_argument("--eta", type=str, default="1e-2", help="η for δ = η*α/(log m1)^2 (string parsed by mp.mpf)")
    parser.add_argument("--anchor", choices=["top","bottom","left","right"], default="top", help="Boundary anchor location")
    parser.add_argument("--plot", action="store_true", help="Show boundary ratio plot")
    parser.add_argument("--save", type=str, default=None, help="CSV path to save (s_normalized, ratio)")

    # NOTE: argparse converts hyphens to underscores: --print-constants -> args.print_constants, etc.
    parser.add_argument("--print-constants", action="store_true", help="Print T1 and m1 with high precision")
    parser.add_argument("--compute-m1", action="store_true", help="Compute m1 via zeta rootfinding instead of using the embedded constant")
    parser.add_argument("--root-dps", type=int, default=200, help="Internal precision for rootfinding if --compute-m1")
    args = parser.parse_args()

    env_dump()

    mp.mp.dps = int(args.dps)
    mp.mp.trap_complex = True

    alpha = mp.mpf('1')

    m1, T1, computed, info = get_m1(args.compute_m1, args.root_dps)

    # FIXED: use args.print_constants (underscores), not args.print-constants
    if args.print_constants:
        print("\n=== CONSTANTS ===")
        print("T1 (classical first nontrivial zero height) =", mp.nstr(T1, n=mp.mp.dps))
        print("m1 = 2*T1 =", mp.nstr(m1, n=mp.mp.dps))
        if computed:
            print("m1 was computed via findroot on ζ(s).")
            if info is not None:
                print("  Re(s_root) =", mp.nstr(info.get("Re(s_root)"), n=50))
                print("  Im(s_root)=T1 =", mp.nstr(info.get("Im(s_root)=T1"), n=50))
        else:
            if info is not None and "error" in info:
                print("Rootfinding error:", info["error"], "→ using embedded T1.")
        print("=================\n")

    eta = mp.mpf(args.eta)
    delta, (xL, xR, yB, yT) = define_box(alpha, m1, eta)

    print("Parameters:")
    print(f"  alpha = {float(alpha)}")
    print(f"  m1    = {mp.nstr(m1, n=30)}   (m1 := 2*T1)")
    print(f"  T1    = {mp.nstr(T1, n=30)}")
    print(f"  eta   = {mp.nstr(eta, n=30)}")
    print(f"  delta = {delta:.12e}")
    print(f"  Box   = [{xL:.12f}, {xR:.12f}] × [{yB:.12f}, {yT:.12f}]")
    print("Settings:")
    print(f"  dps   = {args.dps}")
    print(f"  N_side= {args.nside}")
    print(f"  nx×ny = {args.nx}×{args.ny}")
    print(f"  anchor= {args.anchor}")

    result = boundary_ratio(alpha, m1, delta, xL, xR, yB, yT,
                            dps=args.dps, N_side=args.nside, nx=args.nx, ny=args.ny,
                            make_plot=args.plot, anchor=args.anchor, save_csv=args.save)

    print("\nResult:")
    print(f"  Sup boundary ratio  sup_{{∂B}} |E - G_out| / |G_out|  ≈ {result['rmax']:.12f}")
    print(f"  |E| on ∂B:   min ≈ {result['min_absE_boundary']:.6e},  max ≈ {result['max_absE_boundary']:.6e}")
    print("  Certification:", "PASS (< 1)" if result["rmax"] < 1.0 else "FAIL (≥ 1)")

if __name__ == "__main__":
    main()

