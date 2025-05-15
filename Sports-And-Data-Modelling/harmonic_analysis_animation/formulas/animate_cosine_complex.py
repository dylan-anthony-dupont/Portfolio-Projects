import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function: D(s, N)
def corrected_D(s, N):
    real_part = np.sqrt(N) / 2
    imag_part = (np.pi / 4) * np.cos((np.pi * s) / (2 * np.sqrt(N)))
    return real_part + 1j * imag_part

# Input range for s (same for all)
s_values = np.linspace(-20, 20, 1000)

# Two values of N to compare
N1 = 1
N2 = 4
N3 = 9
N4 = 16

# Compute D(s, N) for both
D1_vals = corrected_D(s_values, N1)
D2_vals = corrected_D(s_values, N2)
D3_vals = corrected_D(s_values, N3)
D4_vals = corrected_D(s_values, N4)

# Separate real and imag parts
real1, imag1 = D1_vals.real, D1_vals.imag
real2, imag2 = D2_vals.real, D2_vals.imag
real3, imag3 = D3_vals.real, D3_vals.imag
real4, imag4 = D4_vals.real, D4_vals.imag

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 6))
point1, = ax.plot([], [], 'bo', label='N = 1', markersize=6)
trace1, = ax.plot([], [], 'b-', linewidth=1)
point2, = ax.plot([], [], 'ro', label='N = 4', markersize=6)
trace2, = ax.plot([], [], 'r-', linewidth=1)
point3, = ax.plot([], [], 'go', label='N = 9', markersize=6)
trace3, = ax.plot([], [], 'g-', linewidth=1)
point4, = ax.plot([], [], 'o', color='purple', label='N = 16', markersize=6)
trace4, = ax.plot([], [], '-', color='purple', linewidth=1)

ax.set_xlim(0, 2)
ax.set_ylim(-1, 1)
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_title('Comparison of D(s, N) for N = 1, 4, 9, and 16')
ax.legend()
ax.grid(True)
ax.axhline(0, color='gray', lw=0.5)
ax.axvline(0, color='gray', lw=0.5)

# Initialization
def init():
    point1.set_data([], [])
    trace1.set_data([], [])
    point2.set_data([], [])
    trace2.set_data([], [])
    point3.set_data([], [])
    trace3.set_data([], [])
    point4.set_data([], [])
    trace4.set_data([], [])
    return point1, trace1, point2, trace2, point3, trace3, point4, trace4

# Update function for animation
def update(frame):
    point1.set_data([real1[frame]], [imag1[frame]])
    trace1.set_data(real1[:frame+1], imag1[:frame+1])
    point2.set_data([real2[frame]], [imag2[frame]])
    trace2.set_data(real2[:frame+1], imag2[:frame+1])
    point3.set_data([real3[frame]], [imag3[frame]])
    trace3.set_data(real3[:frame+1], imag3[:frame+1])
    point4.set_data([real4[frame]], [imag4[frame]])
    trace4.set_data(real4[:frame+1], imag4[:frame+1])
    return point1, trace1, point2, trace2, point3, trace3, point4, trace4

# Animate
ani = animation.FuncAnimation(fig, update, frames=len(s_values),
                              init_func=init, blit=True, interval=20)

# Save as GIF
ani.save("cosine_complex_multiple_N_vals.gif", writer="pillow", fps=30)

