---
parent: Secondary programs
---

# VLATI-TXT

VLATI-TXT is VLATI's textual analysis program. It displays useful information about the spacecraft's trajectory at the chosen step, like velocity and distance vectors.

Syntax:

```console
VLATI-TXT [-h] [-f FRAME] [-s SHOW [SHOW ...]] trajectory_file velocity_file frame_iq
```

## Command-Line Arguments

|Argument||Purpose|
|--|--|--|
|`trajectory_file`|Required|What file VLATI-TXT draws planetary and spacecraft positions from over time|
|`velocity_file`|Required|What file VLATI-TXT draws planetary and spacecraft velocities from over time|
|`frame_iq`|Required|The simulation frame to analyze|
|`-f/--frame`|Optional|The coordinate origin|
|`-s/--show`|Optional|Specific sections to show in the output|

{: .note }
If you input invalid variables into --show, the program will still run, displaying any valid variables you passed.

## Examples

Display all available information about frame 2501:
```console
VLATI-TXT output.npz output.pv 2501
```

Display velocity and position information from frame 491551:
```console
VLATI-TXT output.npz output.pv 491551 -s vecs
```

Display all available information about frame 2661 relative to the moon:
```console
VLATI-TXT output.npz output.pv 491551 -f moon
```

Display time and position/velocity information relative to the moon in frame 6000:
```console
VLATI-TXT output.npz output.pv 6000 -f moon -s time vecs
```

{: .important }
VLATI-TXT needs to convert between ephemeris time and UTC. To do this, it needs a leap seconds file (naif0012.tls for this). It draws this file from conf.py.
