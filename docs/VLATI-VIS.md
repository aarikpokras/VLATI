# VLATI-VIS

VLATI-VIS is the visualization and animation program for VLATI. It's capable of animating each body's trajectory over time, using different origins, and speeding up the simulation with a certain multiplier.

Syntax:
```console
VLATI-VIS [-h] [-f FRAME] trajectory_file start_frame end_frame multiplier
```

The multiplier is applied to the index of the trajectory arrays, so it applies to the start and end frame. For example, if you use t=200 as the start frame and 300 as the multiplier, the first frame will be t=60000. The same applies for the end frame.

The multiplier argument can be followed with an `x`, or alternatively nothing.

The `--frame`/`-f` argument can be used to change the inertial frame of the visualization. For example, for the Moon to be at the center of the visualization, use `-f moon`. This is case sensitive; as such, all frames must be lowercase.

{: .note }
If you've added a body to VLATI, its trajectory needs to be exported to the .npz file in order to be used in the frame argument.

{: .important }
VLATI-VIS draws its starting date from conf.py, so when running VLATI-VIS, make sure that the date in conf.py applies to the simulation loaded into VLATI-VIS. In other words, don't change conf.py in between running the main program and VLATI-VIS. This will be fixed in the near future.

## Examples

Play the trajectory from output.npz at 200x speed, from frame zero to 500000 in an Earth-centered inertial frame:
```console
VLATI-VIS output.npz 0 2500 200
```

Play the trajectory from output.npz at 100x speed, from frame 200000 to 500000 in a Moon-centered inertial frame:
```console
VLATI-VIS output.npz 2000 5000 100x -f moon
```
