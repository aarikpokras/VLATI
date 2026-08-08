# Adding a gravitational body

{: .note }
For most normal uses of VLATI, this is not required; approximate ephemerides are already provided, and the Sun and Moon are already integrated. That being said, if you would still like to continue with this, keep reading.

This is difficult; I recommend becoming familiar with the program's "shape" before doing this.

To add a body, add it to the `bds` tuple array. The format is as follows:
```python
[ ... ( pos_vector_m, mass_kg ) ]
```

The starting position vectors are NumPy arrays, which can be added with something along the lines of:
```python
r_body = np.array([ pos_x_m, pos_y_m, pos_z_m ])
```
Although this will be overridden (subjectively) immediately at t = dt by your motion function. For maximum accuracy, set this to roughly where the body would be at t = 0.

A dot can be added to designate the position of the body in the Matplotlib visualization:
```python
### MPL BODY COLORS ###
# ...

ax.plot( [r_body[0]], [r_body[1]], [r_body[2]], '[color][shape]')

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

In order to add motion to it, find the equations that govern its x and y movement over time, and create a function (like the already-existing function `r_moon_vec`) in main.py that returns a NumPy array that contains the position vector of the body (it does not have to be exactly like this; if your function somehow only defines delta-motion, use that. Whatever works).

Next you need to add this to the integration loop.
```python
  ### COMPUTE NEW POS OF PLANETS ###
  _iter += 1

  r_moon = r_moon_vec(_iter * dt)
  bds[1] = (r_moon, m_moon)

  r_newbody = r_newbodyfunc(_iter * dt)
  bds[3] = (r_newbody, m_newbody)

  ##################################
```

You need to rewrite the tuple in `bds`, as they are immutable.
