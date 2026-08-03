#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
from pathlib import Path

if (len(sys.argv) != 5):
  print("VLATI-VIS: Error: Too many or too few arguments.")
  sys.exit(2)

if (not Path(sys.argv[1]).is_file()):
  print("VLATI-VIS: Error: trajectory file should be an existing file.")
  sys.exit(1)

start_frame = int(sys.argv[2])
end_frame = int(sys.argv[3])

MULTIPLIER = int(sys.argv[4].replace('x', ''))

trajs = np.load(sys.argv[1])
traj_sc = trajs["sc"]
traj_moon = trajs["moon"]
traj_sun = trajs["sun"]

fig, ax = plt.subplots()

ax.set_xlim(-120000000, 120000000)
ax.set_ylim(-120000000, 120000000)
ax.set_aspect('equal')

traj_sc_line = plt.plot(traj_sc[:,0], traj_sc[:,1], 'm-')
traj_moon_line = plt.plot(traj_moon[:,0], traj_moon[:,1], 'g-')
traj_sun_line = plt.plot(traj_sun[:,0], traj_sun[:,1], 'k-')

sc_dot, = ax.plot([traj_sc[0][0]], [traj_sc[0][1]], 'g^')
moon_dot, = ax.plot([traj_moon[0][0]], [traj_moon[0][1]], 'ko')
sun_dot, = ax.plot([traj_sun[0][0]], [traj_sun[0][1]], 'yo')
earth_dot = ax.plot([0], [0], 'bo')

def update(frame):
  t_ = frame * MULTIPLIER
  plt.xlabel(f"t = {t_}")
  sc_dot.set_data([traj_sc[t_][0]], [traj_sc[t_][1]])
  moon_dot.set_data([traj_moon[t_][0]], [traj_moon[t_][1]])
  sun_dot.set_data([traj_sun[t_][0]], [traj_sun[t_][1]])
  return sc_dot, moon_dot, sun_dot

anim = FuncAnimation(fig, update, frames=range(start_frame, end_frame), interval=0, blit=False, repeat=True)

plt.show()
