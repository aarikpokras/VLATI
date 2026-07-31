## Complete

- [x] Programmatically add bodies
- [x] Planetary motion defined by user-provided functions
- [x] Config file

## Incomplete (Plan, soon to occur)

- [ ] Print absolute velocity in burn info thing in MPL
- [ ] Sun motion
- [ ] Move NumPy conversions into main.py
- [ ] More accurate ephemerides (SPICE/kernel file)
- [ ] Patching of burns (allowing burns @ certain times)
  - [x] Time tooltips for reference
  - [x] Single burn
  - [ ] Multiple burns/programmatically adding
    - [ ] Would need to decrease y-coord with every burn info text box
- [ ] `t` single calculation move directly after `_iter` change

## Incomplete (No plan, distant)

- [ ] True inertial frame
- [ ] RK4? Then we could call it "very laggy" instead of "Verlet leapfrog"
- [ ] Continuous finite burns
