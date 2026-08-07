#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
from pathlib import Path
import conf
import spiceypy as spice

spice.kclear()
spice.furnsh(conf.conf["leap_file"])

if (len(sys.argv) != 5):
  print("VLATI-VIS: Error: Too many or too few arguments.")
  sys.exit(2)

if (not Path(sys.argv[1]).is_file()):
  print("VLATI-VIS: Error: trajectory file should be an existing file.")
  sys.exit(1)

START_ET = spice.str2et(conf.conf["utc_start_date"])

start_frame = int(sys.argv[2])
end_frame = int(sys.argv[3])

MULTIPLIER = int(sys.argv[4].replace('x', ''))

trajs = np.load(sys.argv[1])
traj_sc = trajs["sc"]
traj_moon = trajs["moon"]
traj_sun = trajs["sun"]

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection='3d')

ax.set_xlim(-120000000, 120000000)
ax.set_ylim(-120000000, 120000000)
ax.set_zlim(-120000000, 120000000)
ax.set_aspect('equal')

traj_sc_line = ax.plot(traj_sc[:,0], traj_sc[:,1], traj_sc[:,2], 'm-')
traj_moon_line = ax.plot(traj_moon[:,0], traj_moon[:,1], traj_moon[:,2], 'g-')
traj_sun_line = ax.plot(traj_sun[:,0], traj_sun[:,1], traj_sun[:,2], 'k-')

sc_dot, = ax.plot([traj_sc[0][0]], [traj_sc[0][1]], [traj_sc[0][2]], 'g^')
moon_dot, = ax.plot([traj_moon[0][0]], [traj_moon[0][1]], [traj_moon[0][2]], 'ko')
sun_dot, = ax.plot([traj_sun[0][0]], [traj_sun[0][1]], [traj_sun[0][2]], 'yo')
earth_dot = ax.plot([0], [0], [0], 'bo')

moonfmts = "MOON     "
earthfmts = "EARTH    "
sunfmts = "SUN/1000 "

moon_ro = ax.text2D(0.02, 0.02, moonfmts + "ERROR", fontsize=10, transform=ax.transAxes, fontfamily='DejaVu Sans Mono')
earth_ro = ax.text2D(0.02, 0.08, earthfmts + "ERROR", fontsize=10, transform=ax.transAxes, fontfamily='DejaVu Sans Mono')
sun_ro = ax.text2D(0.02, 0.14, sunfmts + "ERROR", fontsize=10, transform=ax.transAxes, fontfamily='DejaVu Sans Mono')
time_ro = ax.text2D(0.02, 0.95, "T = ", fontsize=10, transform=ax.transAxes, fontfamily='DejaVu Sans Mono')
cal_ro = ax.text2D(0.02, 1, "CALENDAR", fontsize=10, transform=ax.transAxes, fontfamily='DejaVu Sans Mono')

ax.set_axis_off()

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

def update(frame):
  et = START_ET + frame
  time_utc = spice.et2utc(et, "C", 3)
  cal_ro.set_text(time_utc)
  t_ = frame * MULTIPLIER
  moon_ro.set_text(f"{moonfmts}{np.linalg.norm(traj_sc[t_] - traj_moon[t_]):.11f}")
  earth_ro.set_text(f"{earthfmts}{np.linalg.norm(traj_sc[t_] - np.array([0, 0, 0])):.11f}")
  sun_ro.set_text(f"{sunfmts}{np.linalg.norm(traj_sc[t_] - traj_sun[t_])/1000:.11f}")
  time_ro.set_text(f"T = {t_}")

  sc_dot.set_data([traj_sc[t_][0]], [traj_sc[t_][1]])
  sc_dot.set_3d_properties([traj_sc[t_][2]])

  moon_dot.set_data([traj_moon[t_][0]], [traj_moon[t_][1]])
  moon_dot.set_3d_properties([traj_moon[t_][2]])

  sun_dot.set_data([traj_sun[t_][0]], [traj_sun[t_][1]])
  sun_dot.set_3d_properties([traj_sun[t_][2]])

  return sc_dot, moon_dot, sun_dot

anim = FuncAnimation(fig, update, frames=range(start_frame, end_frame), interval=0, blit=False, repeat=True)

ax.grid(False)

plt.show()
