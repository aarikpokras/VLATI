## Complete

- [x] Programmatically add bodies
- [x] Planetary motion defined by user-provided functions
- [x] Config file
- [x] `t` single calculation move directly after `_iter` change
- [x] Sun sinusoidal motion
- [x] Separate "player" program (displays entire path at e.g. 2000x spd)
  - [x] Export trajectories to file

## Incomplete (Plan, soon to occur)

### Next release (v0.3.0)
- [ ] Patching of burns (allowing burns @ certain times)
  - [x] Time tooltips for reference
  - [x] Single burn
  - [ ] Multiple burns/programmatically adding
    - [ ] Would need to decrease y-coord with every burn info text box
    - [ ] Array with all burns `[ (burn time GET, [dv vector]) ]`?
      - [ ] If empty, no burns performed
      - [ ] Still need to think about optimization w/ conditionals
- [ ] Print post (pre too?) absolute velocity in burn info thing in MPL
- [ ] Move NumPy conversions into main.py from conf.py

### Other
- [ ] More accurate ephemerides (SPICE/kernel file)
  - [ ] As a consequence, dates are also a part of the simulation
- [ ] Move main visualizer to separate file

## Incomplete (No plan, distant)

- [ ] True inertial frame
- [ ] On click, option for "make burn here" or something - maybe move away from MPL for this
- [ ] RK4? Then we could call it "very laggy" instead of "Verlet leapfrog"
- [ ] Continuous finite burns
- [ ] 3D (MPL vis (hard part)/calculations)
  - [ ] If we do this, it's much easier to implement the NAIF ephemerides, as the coords they give are 3D
