import numpy as np

# A configuration file for a simple lunar flyby with a
# perilune of about 5000km. To calculate this, I used
# Kepler's equations and the vis viva equation (and, 
# of course, VLATI to verify).
### CONFIG ###

conf = {
  "traj_output_file": "./output.npz",
  "frames_to_simulate": 500000,
  "seconds_timestep": 1,
  "degrees_moon_start_angle_N": 24.75684,
  "degrees_sun_start_angle_N": 0,
  "meters_spacecraft_start_vec": [-6537000.0, 0.0],
  "meters_per_second_spacecraft_start_v_vec": [0.0, -10977.0],
  #"burn_array": ( [200000, np.array([1000.0, 0.0]), 0], [300000, np.array([1500.0, 0.0]), 0] )
  "burn_array": ()
}

##############
