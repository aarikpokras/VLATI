import numpy as np
import math
import matplotlib.pyplot as plt
import mplcursors
import sys
import conf

burn_executed = False

# How many iterations of the
# simulator are to be run.
# The higher the value, the
# less frequently terminal
# outputs will be made.
until = conf.conf["frames_to_simulate"]

G = 6.6743 * (10**-11) # m^3 kg^-1 s^-2

### R VECS ###

# Adjust each of these to change the
# positions of each of the bodies.

r_moon = np.array([384398861.0, 0.0])
r_earth = np.array([0.0, 0.0])
r_sun = np.array([149599999999.7966, 0.0])

# Position vector of the spacecraft
#r_sc = np.array([6537000.0, 0.0]) # LEO
r_sc = conf.conf["meters_spacecraft_start_vec"]

# Mass scalar Moon (somewhat needed to
# rewrite tuple in bds)
m_moon = 7.34767309 * (10**22)

##############

moon_orb_r = 384398861.0
moon_omega = 2 * math.pi / 2360000
moon_sta = conf.conf["degrees_moon_start_angle_N"]
def r_moon_vec(t):
  x = moon_orb_r * math.sin(moon_sta + moon_omega * t)
  y = moon_orb_r * math.cos(moon_sta + moon_omega * t)
  return np.array([x, y])

### ARRAY OF BODIES ###

# The second part of each tuple is the weight, in kilograms, of each body.

bds = [ (r_earth, 5.972 * (10**24)), (r_moon, m_moon), (r_sun, 1.989 * (10**30)) ]

#######################

dt = conf.conf["seconds_timestep"]
#v = np.array([0.0, 11000.0]) # was 7800, good start for LEO
v = conf.conf["meters_per_second_spacecraft_start_v_vec"]
_iter = 0

traj = []

modulo = until // 20

print("In progress")

def acceleration_vec(r_sc):
  a = np.zeros(2) # Init the accel vector which will be repeatedly added to

  for r_body, wt in bds:
    r12 = r_sc - r_body
    a += -G * wt * r12 / np.linalg.norm(r12)**3

  return a

a = acceleration_vec(r_sc) # Pre-compute accel vector

moon_traj_debug = []

t = 0

while _iter < until:

  r_sc += v*dt + 0.5*a*(dt**2)  # Compute new position based on accel

  ### COMPUTE NEW POS OF PLANETS ###
  _iter += 1

  r_moon = r_moon_vec(t)
  bds[1] = (r_moon, m_moon)

  ##################################

  t = _iter * dt

  a_new = acceleration_vec(r_sc)

  v += 0.5 * (a + a_new) * dt   # New vel for next loop, avg of a and a_new
                                # vel production

  if (t >= conf.conf["seconds_burn_time_elapsed"]):
    if (not burn_executed and conf.conf["bool_burn"]):
      v += conf.conf["meters_per_second_delta_v_burn"]
      burn_executed = True
      print("----")
      print("T +" + str(t) + "s Burn executed " + str(conf.conf["meters_per_second_delta_v_burn"]))
      print("----")

  if (_iter % modulo == 0):
    print("r_sc        = " + str(r_sc))
    print("|r_scearth| = " + str(np.linalg.norm(r_earth - r_sc)))
    print("Iter " + str(_iter) + "/" + str(until) + " (" + str(_iter*100/until) + ")%")

  traj.append(r_sc.copy())

  moon_traj_debug.append(r_moon.copy())

  a = a_new

traj = np.array(traj)
moon_traj_debug = np.array(moon_traj_debug)

fig, ax = plt.subplots()
ax.set_xlim(-120000000, 120000000)
ax.set_ylim(-120000000, 120000000)
ax.set_aspect('equal')

### MPL BODY COLORS ###

# Change the last argument of ax.plot to change how
# each of the bodies appears in the plot. The 'o',
# or the first character of the last arg, dictates
# the shape of the point, and the first character
# dictates the color. For more info, google "mpl
# format strings".
dote = ax.plot([r_earth[0]], [r_earth[1]], 'bo')
dots = ax.plot([r_sun[0]], [r_sun[1]], 'yo')  
dotm = ax.plot([r_moon[0]], [r_moon[1]], 'ko')

# Traj start marker
ax.plot([traj[0][0]], [traj[0][1]], '^g')

if (burn_executed):
  ax.text(
    0.05,
    0.95,
    'Burn @ T +' + str(conf.conf["seconds_burn_time_elapsed"]) + '\n' + str(conf.conf["meters_per_second_delta_v_burn"]),
    transform = ax.transAxes,
    fontsize = 10,
    verticalalignment = 'top'
  )

#######################

fig.canvas.manager.set_window_title('VLATI')

plt.grid(True)
line_traj = plt.plot(traj[:,0], traj[:,1], 'm-')
plt.plot(moon_traj_debug[:,0], moon_traj_debug[:,1], 'g-')

crsr = mplcursors.cursor(line_traj)
crsr.connect("add", lambda sel: sel.annotation.set_text("t = " + str(int(sel.index)) * dt))

plt.show()
