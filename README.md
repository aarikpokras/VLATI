# VLATI
Verlet Leapfrog Astronomical Trajectory Integrator (2D)

Uses a Velocity Verlet integrator, along with the law of universal gravitation and very approximate (currently only lunar) ephemerides to find the path of a spacecraft through space given an initial state vector.

## Configuration
A configuration file named conf.py is required in the same directory in which VLATI is run. 

## Add a body
To add a body, add it to the `bds` tuple array. The format is as follows:
```python
[ ... ( pos_vector_m, mass_kg ) ]
```

The position vectors are NumPy arrays, which can be added with something along the lines of:
```python
r_body = np.array([ pos_x_m, pos_y_m ])
```

A dot can be added to designate the position of the body in the Matplotlib visualization:
```python
### MPL BODY COLORS ###
# ...

ax.plot( [r_body[0]], [r_body[1]], '[color][shape]')

# ...
#######################
```

For `shape`, you can just use o. Additionally, you can use any shape usable in Matplotlib format strings.

The placeholders for color and shape can be changed based on Matplotlib format strings. A quick reference for the colors:
|Color|Code|
|---|---|
|Blue|b|
|Green|g|
|Red|r|
|Cyan|c|
|Magenta|m|
|Yellow|y|
|Black|k|
|White|w|
