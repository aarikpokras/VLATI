import numpy as np

### CONFIG ###

conf = {
  "frames_to_simulate": 500000,
  "seconds_timestep": 1,
  "degrees_moon_start_angle_N": 0,
  "meters_spacecraft_start_vec": np.array([6537000.0, 0.0]),
  "meters_per_second_spacecraft_start_v_vec": np.array([0.0, 11200.0]),
  "bool_burn": True,
  "meters_per_second_delta_v_burn": np.array([1000.0, 0.0]),
  "seconds_burn_time_elapsed": 200000,
}

##############
