---
parent: Secondary programs
---

# VLATI-TXT

VLATI-TXT is VLATI's textual analysis program. It displays useful information about the spacecraft's trajectory at the chosen step, like velocity and distance vectors.

Syntax:

```console
VLATI-TXT [-h] [-f FRAME] trajectory_file frame_iq
```

The reference frames work similarly to how they do in [VLATI-VIS](/VLATI/VLATI-VIS); as does the trajectory file argument.

Use the frame_iq argument to choose the simulation frame to pass to VLATI-TXT.

{: .important }
VLATI-TXT needs to convert between ephemeris time and UTC. To do this, it needs a leap seconds file (naif0012.tls for this). It draws this file from conf.py.
