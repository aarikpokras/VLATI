# VLATI
Verlet Leapfrog Astronomical Trajectory Integrator (2D)

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/aarikpokras/vlati@715a910/images/vlati-out.png" width="700" />
</p>

Uses a Velocity Verlet integrator, along with the law of universal gravitation and very approximate (currently only lunar) ephemerides to find the path of a spacecraft through space given an initial state vector.

## Dependencies
In order to use VLATI, you need the following Python packages (each is installable via `pip`):
* matplotlib
* numpy
* mplcursors

They can be installed through the following command:
```console
pip install matplotlib numpy mplcursors
```

## Configuration
A configuration file named conf.py is required in the same directory in which VLATI is run. It must contain a dictionary with the same name.
```python
###### conf.py ######
conf = {
  ... config options
}
```

The options available are found in the conf.py file in the root directory of this repository. Every option in the file is required, and no more and no less can be used (as of now). The conf.py file in this repository is ready for use with the simulator. The following will list each of the configuration options, what they affect, and what units they use.
|Variable|Unit|Purpose|
|---|---|---|
|`frames_to_simulate`|frames|Tells VLATI how many iterations it should simulate.|
|`seconds_timestep`|seconds|What the Δt of the simulation is; generally, the smaller the more accurate; good to keep it ~1.|
|`degrees_moon_start_angle_N`|degrees|Where the Moon's revolution about the Earth starts relative to absolute upwards (increases clockwise).|
|`meters_spacecraft_start_vec`|meters|The starting location vector of the spacecraft.|
|`meters_per_second_spacecraft_start_v_vec`|meters per second|The starting velocity vector of the spacecraft.|
|`bool_burn`|`True`/`False`|Whether the below burn settings apply.|
|`meters_per_second_delta_v_burn`|meters per second|The Δv vector of the burn.|
|`seconds_burn_time_elapsed`|seconds|At what time elapsed to perform the burn|

## Add a body
This is difficult; I recommend becoming familiar with the program's "shape" before doing this.

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
