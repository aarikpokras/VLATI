# VLATI

<p align="center">
Verlet Leapfrog Astrodynamic Trajectory Integrator
<!--  <img src="https://cdn.jsdelivr.net/gh/aarikpokras/vlati@2228111/images/vlati-out.png" width="700" />
  <img src="https://cdn.jsdelivr.net/gh/aarikpokras/vlati@5791ba1/images/moon_flyby.gif" width="700" />-->
  <img src="https://cdn.jsdelivr.net/gh/aarikpokras/vlati@8a38846/images/vlati-stat-out-new.png" width="700">
  <img src="https://cdn.jsdelivr.net/gh/aarikpokras/vlati@8a38846/images/vlati-vis.gif" width="700">
</p>

VLATI is a restricted four-body problem solver of an Earth-Moon-Sun system, aimed at astrodynamics and trajectory calculation.

It uses a Velocity Verlet integrator, along with the law of universal gravitation and very approximate ephemerides to find the path of a spacecraft through space given an initial state vector.

Notable features:
* Impulsive burns
* Animated and quantitative visualization program
* Real lunar and solar ephemerides

There are plans to increase the accuracy of the ephemerides, as they are currently only sinusoidal (circular).

You can take a look at the documentation directory for VLATI's documentation.

## Installation
To install VLATI, first install its [dependencies](https://github.com/aarikpokras/VLATI/wiki/Dependencies). Then you can either download its zip from the Code tab, or git clone it, then enter the directory and run the configure script:

```console
git clone https://github.com/aarikpokras/VLATI.git && cd VLATI && sh configure.sh
```

Additionally, you need to acquire the bsp file for the ephemerides. [Download it](https://ssd.jpl.nasa.gov/ftp/eph/planets/bsp/de440.bsp) and put it into the same directory as VLATI.
