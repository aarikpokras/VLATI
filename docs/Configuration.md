---
nav_order: 4
---

# Configuration

A configuration file named conf.py is required in the same directory in which VLATI is run. It must contain a dictionary with the same name.
```python
###### conf.py ######
conf = {
  ... config options
}
```

## List of configuration options

The options available are found in the conf.py file in the root directory of this repository. Every option in the file is required, and no more and no less can be used (as of now). The conf.py file in this repository is ready for use with the simulator. The following will list each of the configuration options, what they affect, and what units they use.

|Variable|Unit|Purpose|
|---|---|---|
|`frames_to_simulate`|frames|Tells VLATI how many iterations it should simulate.|
|`seconds_timestep`|seconds|What the Δt of the simulation is; generally, the smaller the more accurate; good to keep it ~1.|
|`meters_spacecraft_start_vec`|meters|The starting location vector of the spacecraft.|
|`meters_per_second_spacecraft_start_v_vec`|meters per second|The starting velocity vector of the spacecraft.|
|`burn_array`|various|Read below for information regarding `burn_array`.|
|`traj_output_file`|file path|Where to save the trajectories of the Sun, Moon, and spacecraft. Should be a file with a `.npz` extension.|
|Advanced|
|`ephemeris_file`|file path|The file in which the ephemeris is located.|
|`leap_file`|file path|The file in which the leap second information is located.|

## Notes about config options

### `traj_output_file`
Exports an `npz` file containing trajectories. It's used as an input in VLATI-VIS.

### Usage of `burn_array`
`burn_array` is actually a burn tuple. Unfortunately, **zero** or **at least two** elements are required in the burn tuple. If you want only one burn, use the following entry in the burn tuple (along with, of course, your chosen burn):
```python
[0, 0, 1]
```

The structure of the `burn_array` configuration option is as follows:
```python
( [ burn_time_elapsed_seconds, np.array([ dv vector ]), 0 ] )
```
The zero indicates to VLATI that the burn hasn't been performed yet. During each timestep, when iterating through the burn array, it checks this to see whether it should execute the burn, and changes it to `1` when it has.

An example of the Δv vector:
```python
np.array([1000.0, 0.0])
```
At least one of the vector components must contain a .0 (or any other decimal, to your preference) to indicate to NumPy that the vector represents a vector of floating-point numbers, not integers.
