import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from numba import njit  # Import Numba's JIT compiler

# Use Numba to accelerate the electric field calculation
@njit
def electric_field(q1, q2, x0, y0, d, X, Y):
    # Initialize electric field components
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    
    # Calculate electric field for each point in the grid
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            # Position vectors relative to the charges
            r1 = np.sqrt((X[i, j] - (x0 + d/2))**2 + (Y[i, j] - y0)**2)
            r2 = np.sqrt((X[i, j] - (x0 - d/2))**2 + (Y[i, j] - y0)**2)
            
            # Electric field components due to each charge
            Ex1 = q1 * (X[i, j] - (x0 + d/2)) / r1**3
            Ey1 = q1 * (Y[i, j] - y0) / r1**3
            Ex2 = q2 * (X[i, j] - (x0 - d/2)) / r2**3
            Ey2 = q2 * (Y[i, j] - y0) / r2**3
            
            # Total electric field at this point
            Ex[i, j] = Ex1 + Ex2
            Ey[i, j] = Ey1 + Ey2
    
    return Ex, Ey

# Initial charges, positions, and distance
q1, q2 = 1.0, -1.0
x0, y0 = 0.0, 0.0
d = 2.0  # Initial distance between charges
zoom_level = 5.0  # Initial zoom level

# Create the figure and axis
plt.style.use('dark_background')  # Set dark theme
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(left=0.1, bottom=0.4)  # Adjust layout for sliders

# Function to create a grid based on the zoom level
def create_grid(zoom_level, resolution=100):  # Increased resolution
    x = np.linspace(-zoom_level, zoom_level, resolution)
    y = np.linspace(-zoom_level, zoom_level, resolution)
    return np.meshgrid(x, y)

# Plot the initial electric field
X, Y = create_grid(zoom_level)
Ex, Ey = electric_field(q1, q2, x0, y0, d, X, Y)
stream = ax.streamplot(X, Y, Ex, Ey, density=2.0, linewidth=1, arrowsize=1, arrowstyle='->', color='darkgreen')  # Increased density
scatter = ax.scatter([x0 + d/2, x0 - d/2], [y0, y0], c=['red', 'blue'], s=200)
charge1_text = ax.text(x0 + d/2, y0 + 0.3, f'{q1:+.1f}', color='white', ha='center', va='center')
charge2_text = ax.text(x0 - d/2, y0 + 0.3, f'{q2:+.1f}', color='white', ha='center', va='center')
ax.set_title(f'Electric Dipole: q1={q1}, q2={q2}, Distance={d}')
ax.set_xlim(-zoom_level, zoom_level)
ax.set_ylim(-zoom_level, zoom_level)
ax.grid(True, color='gray', linestyle='--', alpha=0.5)

# Add sliders for q1, q2, distance, and zoom
ax_q1 = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor='lightgray')
ax_q2 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor='lightgray')
ax_d = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgray')
ax_zoom = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgray')
q1_slider = Slider(ax_q1, 'q1', -5.0, 5.0, valinit=q1, valstep=0.1)
q2_slider = Slider(ax_q2, 'q2', -5.0, 5.0, valinit=q2, valstep=0.1)
d_slider = Slider(ax_d, 'Distance', 0.5, 5.0, valinit=d, valstep=0.1)
zoom_slider = Slider(ax_zoom, 'Zoom', 1.0, 20.0, valinit=zoom_level, valstep=0.5)  # Extended zoom range

# Function to update the plot when sliders are changed
def update(val):
    q1 = q1_slider.val
    q2 = q2_slider.val
    d = d_slider.val
    zoom_level = zoom_slider.val
    
    # Recreate the grid based on the new zoom level
    global X, Y
    X, Y = create_grid(zoom_level)
    
    # Recalculate the electric field
    Ex, Ey = electric_field(q1, q2, x0, y0, d, X, Y)
    
    # Clear the previous plot and redraw
    ax.clear()
    ax.streamplot(X, Y, Ex, Ey, density=2.0, linewidth=1, arrowsize=1, arrowstyle='->', color='darkgreen')  # Increased density
    ax.scatter([x0 + d/2, x0 - d/2], [y0, y0], c=['red', 'blue'], s=200)
    ax.text(x0 + d/2, y0 + 0.3, f'{q1:+.1f}', color='white', ha='center', va='center')
    ax.text(x0 - d/2, y0 + 0.3, f'{q2:+.1f}', color='white', ha='center', va='center')
    ax.set_title(f'Electric Dipole: q1={q1}, q2={q2}, Distance={d:.2f}')
    ax.set_xlim(-zoom_level, zoom_level)
    ax.set_ylim(-zoom_level, zoom_level)
    ax.grid(True, color='gray', linestyle='--', alpha=0.5)
    plt.draw()

# Attach the update function to the sliders
q1_slider.on_changed(update)
q2_slider.on_changed(update)
d_slider.on_changed(update)
zoom_slider.on_changed(update)

# Show the plot
plt.show()