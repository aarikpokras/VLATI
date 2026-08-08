#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
import mplcursors
import sys
import conf
import spiceypy as spice

burn_arr = conf.conf["burn_array"]

spice.kclear()
spice.furnsh(conf.conf["leap_file"])
spice.furnsh(conf.conf["ephemeris_file"])

START_ET_ = conf.conf["utc_start_date"]
ET = spice.str2et(START_ET_)

AXIS_REFR = "ECLIPJ2000"

# How many iterations of the
# simulator are to be run.
# The higher the value, the
# less frequently terminal
# outputs will be made.
until = conf.conf["frames_to_simulate"]

G = 6.6743 * (10**-11) # m^3 kg^-1 s^-2

### R VECS ###

r_moon = np.array([384398861.0, 0.0, 0.0])
r_earth = np.array([0.0, 0.0, 0.0])
r_sun = np.array([149599999999.7966, 0.0, 0.0])

# Position vector of the spacecraft
#r_sc = np.array([6537000.0, 0.0]) # LEO
r_sc = np.array(conf.conf["meters_spacecraft_start_vec"])

# Mass scalars (somewhat needed to
# rewrite tuples in bds)
m_moon = 7.34767309 * (10**22)
m_sun = 1.989 * (10**30)

##############

### ARRAY OF BODIES ###

# The second part of each tuple is the weight, in kilograms, of each body.

bds = [ (r_earth, 5.972 * (10**24)), (r_moon, m_moon), (r_sun, m_sun) ]

#######################

dt = conf.conf["seconds_timestep"]
v = np.array(conf.conf["meters_per_second_spacecraft_start_v_vec"])
_iter = 0

traj = []

modulo = until // 20

print("In progress")

def acceleration_vec(r_sc):
  a = np.zeros(3) # Init the accel vector which will be repeatedly added to

  for r_body, wt in bds:
    r12 = r_sc - r_body
    a += -G * wt * r12 / np.linalg.norm(r12)**3

  return a

a = acceleration_vec(r_sc) # Pre-compute accel vector

moon_traj_debug = []
sun_traj = []

t = 0

while _iter < until:

  r_sc += v*dt + 0.5*a*(dt**2)  # Compute new position based on accel

  ### COMPUTE NEW POS OF PLANETS ###
  _iter += 1
  t = _iter * dt
  ET += dt

  r_moon = spice.spkpos("MOON", ET, AXIS_REFR, "NONE", "EARTH")[0] * 1000 # returns NumPy array in km
  bds[1] = (r_moon, m_moon)

  r_sun = spice.spkpos("SUN", ET, AXIS_REFR, "NONE", "EARTH")[0] * 1000
  bds[2] = (r_sun, m_sun)

  ##################################

  a_new = acceleration_vec(r_sc)

  v += 0.5 * (a + a_new) * dt   # New vel for next loop, avg of a and a_new
                                # vel production

# ( [ burn_met, delta_v, executed?changeifyes ], ... )

  for burn in burn_arr:
    if (t >= burn[0]):
      if (burn[2] == 0):
        v += burn[1]
        burn[2] = 1
        print("\n++++++++++++++++++++++++++++++++++\n")
        print("T +" + str(t) + "s Burn executed " + str(burn[1]))

  if (_iter % modulo == 0):
    print("\n===============================================\n")
    print("r_sc        = " + str(r_sc))
    print("|r_scearth| = " + str(np.linalg.norm(r_earth - r_sc)))
    print("Iter " + str(_iter) + "/" + str(until) + " (" + str(_iter*100/until) + ")%")

  traj.append(r_sc.copy())

  moon_traj_debug.append(r_moon.copy())
  sun_traj.append(r_sun.copy())

  a = a_new

traj = np.array(traj)
moon_traj_debug = np.array(moon_traj_debug)
sun_traj = np.array(sun_traj)

print("Writing trajectories to file...")

np.savez(conf.conf["traj_output_file"], sun=sun_traj, moon=moon_traj_debug, sc=traj)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim(-120000000, 120000000)
ax.set_ylim(-120000000, 120000000)
ax.set_zlim(-120000000, 120000000)
ax.set_aspect('equal')

### MPL BODY COLORS ###

# Change the last argument of ax.plot to change how
# each of the bodies appears in the plot. The 'o',
# or the first character of the last arg, dictates
# the shape of the point, and the first character
# dictates the color. For more info, google "mpl
# format strings".
dote = ax.plot([r_earth[0]], [r_earth[1]], 'bo')
dots = ax.scatter(r_sun[0], r_sun[1], r_sun[2], c='#ffd343', marker='o', s=40)
dotm = ax.scatter(r_moon[0], r_moon[1], r_moon[2], c='black', marker='o')

# Traj start marker
ax.plot([traj[0][0]], [traj[0][1]], '^g')

#######################

fig.canvas.manager.set_window_title('VLATI')

ax.grid(False)
line_traj = ax.plot(traj[:,0], traj[:,1], traj[:,2], 'm-')
ax.plot(moon_traj_debug[:,0], moon_traj_debug[:,1], moon_traj_debug[:,2], 'g-')
ax.plot(sun_traj[:,0], sun_traj[:,1], sun_traj[:,2], 'k-')

#crsr = mplcursors.cursor(line_traj)
#crsr.connect("add", lambda sel: sel.annotation.set_text("t = " + str(int(sel.index * dt))))

ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

ax.tick_params(axis='x', colors='red')
ax.tick_params(axis='y', colors='green')
ax.tick_params(axis='z', colors='blue')

cust_spines = {
  "+z": {
    "x": [0, 0],
    "y": [0, 0], 
    "z": [0, 120000000]
  },
  "+y": {
    "x": [0, 0],
    "y": [0, 120000000],
    "z": [0, 0]
  },
  "+x": {
    "x": [0, 120000000],
    "y": [0, 0],
    "z": [0, 0],
  }
}

ax.plot(cust_spines["+z"]["x"], cust_spines["+z"]["y"], cust_spines["+z"]["z"], 'b-', linewidth=0.5)
ax.plot(cust_spines["+y"]["x"], cust_spines["+y"]["y"], cust_spines["+y"]["z"], 'g-', linewidth=0.5)
ax.plot(cust_spines["+x"]["x"], cust_spines["+x"]["y"], cust_spines["+x"]["z"], 'r-', linewidth=0.5)

plt.show()
