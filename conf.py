import numpy as np

### CONFIG ###

conf = {
  "traj_output_file": "./output.npz",
  "frames_to_simulate": 500000,
  "seconds_timestep": 1,
  "degrees_moon_start_angle_N": 0,
  "degrees_sun_start_angle_N": 0,
  "meters_spacecraft_start_vec": [6537000.0, 0.0],
  "meters_per_second_spacecraft_start_v_vec": [0.0, 11200.0],
  "burn_array": ( [200000, np.array([1000.0, 0.0]), 0], [300000, np.array([1500.0, 0.0]), 0] )
}

##############
