import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function: D(s, N, mk)
def D_generalized(s, N, mk):
    real_part = np.sqrt(N) / 2
    imag_part = (mk * np.sqrt(N) / 2) * np.cos((np.pi * s) / (2 * np.sqrt(N)))
    return real_part + 1j * imag_part

# Parameters
N = 4
mk = 28.269450284
s_values = np.linspace(-10, 10, 1000)

# Compute D(s, N, mk)
D_vals = D_generalized(s_values, N, mk)
real_vals = D_vals.real
imag_vals = D_vals.imag

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
point, = ax.plot([], [], 'bo', markersize=6)
trace, = ax.plot([], [], 'b-', linewidth=1)

ax.set_xlim(0, 2)
ax.set_ylim(-70, 70)
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_title(f'Animation of D(s, N={N}, mk={mk})')
ax.grid(True)
ax.axhline(0, color='gray', lw=0.5)
ax.axvline(0, color='gray', lw=0.5)

# Initialization
def init():
    point.set_data([], [])
    trace.set_data([], [])
    return point, trace

# Update function
def update(frame):
    point.set_data([real_vals[frame]], [imag_vals[frame]])
    trace.set_data(real_vals[:frame+1], imag_vals[:frame+1])
    return point, trace

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(s_values),
                              init_func=init, blit=True, interval=20)

# Save animation
ani.save("D_generalized_N4_mk28.gif", writer="pillow", fps=30)