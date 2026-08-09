---
nav_order: 8
---

# Adding a gravitational body

<!--{: .outdated }
This information is outdated. It will be fixed in a coming documentation update.-->

{: .note }
For most normal uses of VLATI, this is not required; approximate ephemerides are already provided, and the Sun and Moon are already integrated. That being said, if you would still like to continue with this, keep reading.

{: .note }
It is recommended to read the [data flow](/VLATI/dataflow) section to familiarize yourself with how data moves through VLATI.

This is difficult; I recommend becoming familiar with the program's "shape" before doing this.

{: .sourcefile }
main.py

### 1. Mass scalar and t=0 position vector

First, add the t=0 position vector. This denotes where your body will be at t=0 (this doesn't *really* have too much influence on the physics of the simulation if you're using a motion function or SPICE/NAIF). You will find it under the comment marked `### R VECS ###` around line 31. Already there, you will find variables named `r_sun`, `r_moon`, and `r_earth`. Add yours in. For this tutorial, the body we'll add can be called `mars`.

```python
### R VECS ###

r_moon = np.array([384398861.0, 0.0, 0.0])
r_earth = np.array([0.0, 0.0, 0.0])
r_sun = np.array([149599999999.7966, 0.0, 0.0])

r_mars = np.array([posx, posy, posz])
```

{: .note }
Make sure to add decimals to this to indicate to VLATI and NumPy that it's a vector of floating-point numbers and not integers.

Next, directly underneath, you'll need a mass scalar for your body in milligrams. No scientific notation is allowed, and it is discouraged to copy and paste mass values.

Just kidding. Use kilograms. Scientific notation (Pythonic and not Pythonic) is, of course, allowed.

```python
m_moon = 7.34767309 * (10**22)
m_sun = 1.989 * (10**30)

m_mars = 6.41693 * (10**23)
```

### 2. Initialization in `bds`

`bds` is an array of tuples. Each tuple contains a body's mass scalar and its position vector (the one that you initialized earlier - it's important to initialize it, but the t=0 value isn't super important to the physics).

Add your tuple to `bds`:
```python
bds = [ (r_earth, 5.972 * (10**24)), (r_moon, m_moon), (r_sun, m_sun), (r_mars, m_mars) ]
```

It will now be automatically factored into the calculations.

<hr />

<!--
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
-->
