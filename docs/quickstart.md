---
nav_order: 4
---

# Quick Start

{: .note }
It's generally a good idea to take a look at the [Configuration](/VLATI/Configuration) section to familiarize yourself with the config options.

After downloading VLATI, you're ready to get started. This quick start will use the example config file called `TLI-c-MCC-c-LOI.py`. It's located in the [examples](https://github.com/aarikpokras/VLATI/blob/master/examples/TLI-c-MCC-c-LOI.py) directory in the repository.

{: .note }
Remember to rename the file to `conf.py`. Otherwise VLATI will not recognize it as a configuration file.

The reason for the seemingly weird file name is because it describes roughly what the configuration file tells VLATI to do. First, it puts it on a trans-lunar trajectory (going towards the Moon - **T**rans-**L**unar **I**njection), then coasts for a bit, then executes a **Mid**-**C**ourse **C**orrection to align itself with the Moon's slightly inclined orbital plane, then coasts for a bit again, and executes a **L**unar **O**rbital **I**nsertion.

## Breakdown

First, let's go through the configuration file (called `conf.py`) line by line. Here is the whole thing:

```python
import numpy as np

# Performs a trans-lunar injection, coasts for a bit,
# then executes a mid-course correction before coasting
# for a bit more time, then performing a lunar orbital
# insertion.

### CONFIG ###

conf = {
  "utc_start_date": "2000 JAN 10 03:09:52.816",
  "traj_output_file": "./output.npz",
  "frames_to_simulate": 500000,
  "seconds_timestep": 1,
  "meters_spacecraft_start_vec": [-6537000.0, 0.0, 0.0],
  "meters_per_second_spacecraft_start_v_vec": [0.0, 11000.2, 0.0],
  "burn_array": ( [50000, np.array([0.0, 0.0, -211.0]), 0], [196800, np.array([0.0, -2000.0, -2000.0]), 0] ),

  ### ADVANCED ###
  "ephemeris_file": "de440.bsp",
  "leap_file": "naif0012.tls"
}

##############
```

We'll start after the line where the config dictionary starts (the line we're talking about contains `conf = {`.)

The first configuration option in the example file is the start date of the simulation, with the key `utc_start_date`. It represents the date **and time** in UTC at the start of the simulation. This date is passed directly into NAIF's SPICE software, which has an extremely robust date format detection system. As such, almost any date/time format you can think of will work with this. SPICE will throw an error if the date format is not supported.

The second key is `traj_output_file`. It represents the relative path of the file to which the positions of each body and the spacecraft over time will be written after the simulation is complete. It is primarily for use with VLATI-VIS, but can be easily read with `numpy.load`.

The third key is `frames_to_simulate`. It represents the amount of frames that the simulation will run, which is critically different from the amount of time that the simulation simulates; the formula for the amount of time simulated would be frames simulated ⨉ timestep.

The fourth key is the timestep (`seconds_timestep`). It represents how much time is added to the clock every iteration. The smaller this is, the more accurate the simulation is, but a smaller timestep also makes the simulation more computationally expensive and slow.

The fifth key is the starting position of the spacecraft (`meters_spacecraft_start_vec`). It references the center of the Earth. As such, if this were `[0, 0, 0]`, the spacecraft would start right at the center of the Earth.

The sixth key is the starting velocity vector of the spacecraft (`meters_per_second_spacecraft_start_v_vec`).

The seventh is the burn tuple. It contains information about instantaneous Δv burns. The first element of the constituent arrays denotes the elapsed time at which to execute the burn; the second is the Δv vector, and the third should just be a zero. This is an element that VLATI modifies when the burn has been executed.

{: .important }
Due to the nature of Python tuples, `burn_array` must have either **zero** or **at least two** arrays within. If there is only one, there will be an error. If you wish to execute just one burn, add the array `[0, 0, 1]` to `burn_array`. It will not execute any burn (except for the one you specify), but it will keep the error from happening.

We now have the advanced options. The `ephemeris_file` and `leap_file` keys denote the relative paths of the files that contain ephemerides and leap seconds. You usually don't need to change these.

## Running the simulation

Now that the config file is written, we need to run the simulation. First, ensure that conf.py is in the same directory as VLATI. Then, run the simulation:

Either:

```console
python3 main.py
```

or

```console
./VLATI_TRAJ
```

This will start the simulation. It should start with an `In progress` readout, then periodically (every 5% of `frames_to_simulate` iterated over) it will output another readout that contains the position vector of the spacecraft and its distance from Earth.

When it is finished, a final readout reading `Writing trajectories to file...` will appear for a few seconds before a window opens showing a static 3D plot of the spacecraft's and bodies' paths over time. When you are ready, close this out.

Congratulations! You've just run your first VLATI simulation. As a next step, you can try out [VLATI-VIS](/VLATI/VLATI-VIS).
