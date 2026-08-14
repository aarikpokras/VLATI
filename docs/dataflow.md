---
nav_order: 7
parent: Advanced
---

# Data Flow
The data you input info conf.py takes the following path:

```
conf.py → VLATI_TRAJ → output.npz
                                └ VLATI_VIS
```
<!--┌└ ─│ ┘┐├ ┤ ⎸ ⎹-->

```
Timestep ────────────────────────────────────────────────┐
S ┌ Start date        → ┌       ┐ → J2K Time ┐           │
P │ Ephemeris file    → │ SPICE │ ┐          │           │           ┌────────────────────┐                         ┌ Start position vector
K └ Leap seconds file → └       ┘ ┤          │           │           │ Initial conditions │─────────────────────────┘ Start velocity vector
                                  │          │           │           └────────────────────┘
                                  │          |           │   ┌ INTEGRATION LOOP (VELOCITY VERLET) ┐
                                  │          │           │   ├ Position update                    │
                                  │          └───────────┴───│ Time increment                     │
                                  └──────────────────────────│ Ephemeris calculation              │
Burn array ──────────────────┐                               ├ Vector field query                 │
                             │                               ├ Velocity calculation               │
Trajectory output file ┐     └───────────────────────────────│ ├ Impulsive burn                   │
                       │                                     │ Vector list appends                │
                       │                                     └────────────────────────────────────┘
                       │                                     ┌───────── POST CALCULATION ─────────┐
                       │                                     │ Array conversions                  │
                       └─────────────────────────────────────│ Trajectory (.npz) file save        │
                                                             │ Velocity (.pv) file save           │
                                                             │ MPL Static visualization           │
                                                             └────────────────────────────────────┘
                                                             VLATI-VIS
                                                             VLATI-TXT
```
