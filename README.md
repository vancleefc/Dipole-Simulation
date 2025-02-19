Electric Dipole Simulation

This Python script simulates the electric field of a dipole using streamlines and allows for dynamic interaction through sliders.

Description
The script visualizes the electric field of a dipole by solving for the electric field vectors using Coulomb’s law. The field is displayed using a stream plot, with interactive sliders that let users adjust charge values, charge separation, and zoom level in real time.

Dependencies:
Python 3
NumPy
Matplotlib
Numba

How It Works:
Grid Creation: A 2D grid is generated to compute electric field components.
Field Calculation: The electric field is computed for each grid point using Coulomb’s law.
Visualization: A streamplot is used to display field lines, with charges marked in red (positive) and blue (negative).
Interactivity: Sliders allow real-time adjustment of charge magnitudes, distance, and zoom level.

How to Run:
Ensure you have the required dependencies installed, then execute:
python dipole_simulation.py

Expected Behavior:
Field lines originate from the positive charge and terminate at the negative charge.
Adjusting charge values affects field intensity and direction.
Changing the charge separation alters field symmetry.
Zooming in and out provides different perspectives on the field behavior.
