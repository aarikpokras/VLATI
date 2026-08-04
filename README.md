# VLATI
Verlet Leapfrog Astrodynamic Trajectory Integrator

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/aarikpokras/vlati@2228111/images/vlati-out.png" width="700" />
  <img src="https://cdn.jsdelivr.net/gh/aarikpokras/vlati@5791ba1/images/moon_flyby.gif" width="700" />
</p>

VLATI is a 2-dimensional simulation of a Moon-Sun-Earth system.

It uses a Velocity Verlet integrator, along with the law of universal gravitation and very approximate ephemerides to find the path of a spacecraft through space given an initial state vector.

Notable features:
* Impulsive burns
* Animated and quantitative visualization program
* Fast computation of trajectory

There are plans to increase the accuracy of the ephemerides, as they are currently only sinusoidal (circular), but it's worth noting that NAIF provides ephemerides with 3D coordinates, so this is unlikely to happen until I [add another dimension](https://github.com/aarikpokras/VLATI/issues/6) into this simulation.

You can take a look at the [wiki](https://github.com/aarikpokras/VLATI/wiki) for VLATI's documentation.

## Installation
To install VLATI, first install its [dependencies](https://github.com/aarikpokras/VLATI/wiki/Dependencies). Then you can either download its zip from the Code tab, or git clone it, then enter the directory and run the configure script:

```console
git clone https://github.com/aarikpokras/VLATI.git && cd VLATI && sh configure.sh
```
