VLATI-VIS is the visualization and animation program for VLATI. It's capable of animating each body's trajectory over time, along with a certain multiplier to control animation speed.

Syntax:
```console
VLATI_VIS [trajectory file] [start frame] [end frame] [multiplier][x|]
```

The multiplier is applied to the index of the trajectory arrays, so it applies to the start and end frame. For example, if you use t=200 as the start frame and 300 as the multiplier, the first frame will be t=60000. The same applies for the end frame.

The multiplier argument can be followed with an `x`, or alternatively nothing.