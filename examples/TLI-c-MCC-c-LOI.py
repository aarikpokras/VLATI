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
