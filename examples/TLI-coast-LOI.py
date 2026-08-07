import numpy as np

# This no longer works. It's still here for compatibility.
# This config file was written before real ephemerides were added.

### CONFIG ###

conf = {
  "traj_output_file": "./output.npz",
  "frames_to_simulate": 500000,
  "seconds_timestep": 1,
  "degrees_moon_start_angle_N": 24.75684,
  "degrees_sun_start_angle_N": 0,
  "meters_spacecraft_start_vec": [-6537000.0, 0.0, 0.0],
  "meters_per_second_spacecraft_start_v_vec": [0.0, -10976.2, 0.0],
  "burn_array": ( [273000, np.array([100.0, -2000.0, -300.0]), 0], [0, 0, 1] )
}

##############
