#!/usr/bin/env python3

import numpy as np
from pathlib import Path
import argparse
import sys
import spiceypy as spice
import conf

spice.furnsh(conf.conf["leap_file"])

psr = argparse.ArgumentParser()
psr.add_argument("trajectory_file", help="The file in which the trajectories are stored", type=Path)
psr.add_argument("frame_iq", help="The frame to analyze", type=int)
psr.add_argument("-f", "--frame", help="The inertial reference origin to use")
args = psr.parse_args()

if (not Path(args.trajectory_file).is_file()):
  print("VLATI-TXT C: Error: trajectory file should be an existing file.")
  sys.exit(1)

data = dict(np.load(args.trajectory_file))

velocity_vectors = data['v']
del data['v']

start_et = data['set']
del data['set']

dt = data['dt']
del data['dt']

### USER ERROR HANDLING ###

if (args.frame_iq >= len(data['sc'])):
  print("VLATI-TXT H: Error: Frame out of index.")
  sys.exit(4)

if (args.frame and not args.frame in data):
  print("VLATI-TXT H: Error: Inertial reference frame does not exist.")
  sys.exit(4)

###########################

if (args.frame):
  origin = data[args.frame].copy()
  for trajectory in data:
    data[trajectory] -= origin

# At this point we've performed any origin changes or error handling that
# we need... now relative to our new frame (or not) we can output state
# vectors, etc.
# List:
#  State vector
#  Norms of state vectors
#  Radial velocity relative to chosen origin
#  Distance (which is a norm of state vec)
#  Frame, time, ephemeris time, UTC

print('--- VLATI TEXT BASED ANALYSIS TOOL ---')
print()

SECS_ELAP = dt * args.frame_iq
EPHM_TIME = start_et + SECS_ELAP

fi = {
  "UTC_TIME": spice.et2utc(EPHM_TIME, "C", 3),
  "POS_VECT": data['sc'][args.frame_iq],
  "VEL_VECT": velocity_vectors[args.frame_iq]
}

np.set_printoptions(precision=5, suppress=True)

print(
  "-- TIME --",
  f"SECS ELAP        : {SECS_ELAP}",
  f"EPHEMERIS TIME   : {EPHM_TIME}",
  f"UTC TIME         : {fi['UTC_TIME']}",
  f"DT               : {dt}",
  "",
  "-- VECS --",
  f"R VECTOR         : {fi['POS_VECT']}",
  f"- NORM (DISTANCE): {np.linalg.norm(fi['POS_VECT'])}",
  f"V VECTOR         : {fi['VEL_VECT']}",
  f"- NORM (VELOCITY): {np.linalg.norm(fi['VEL_VECT'])}",
  "",
  "-- SCAL --",
  f"RAD VEL (v dot r): {np.dot(velocity_vectors[args.frame_iq], data['sc'][args.frame_iq])}",
  sep="\n"
)
