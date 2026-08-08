import numpy as np

### CONFIG ###

conf = {
  "utc_start_date": "2026-08-06T22:00:00.00",
  "traj_output_file": "./output.npz",
  "frames_to_simulate": 500000,
  "seconds_timestep": 1,
  "meters_spacecraft_start_vec": [-6537000.0, 0.0, 0.0],
  "meters_per_second_spacecraft_start_v_vec": [0.0, -10976.2, 0.0],
  "burn_array": ( [273000, np.array([100.0, -2000.0, -300.0]), 0], [0, 0, 1] ),

  ### ADVANCED ###
  "ephemeris_file": "de440.bsp",
  "leap_file": "naif0012.tls"
}

##############

