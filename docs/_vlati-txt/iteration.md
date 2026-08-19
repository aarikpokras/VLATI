---
parent: VLATI-TXT
title: Iterating with VLATI-TXT and the command line
---

Learn before you start:
* How to use the [stream editor](https://www.geeksforgeeks.org/linux-unix/sed-command-in-linux-unix-with-examples/)
* How to use [VLATI-TXT](/VLATI/VLATI-TXT)
* Simple regex

This tutorial aims to make VLATI-TXT easier to iterate over; with the skills taught in this tutorial, you will be able to have the (very) basic foundations of a bash program that can possibly maximize or minimize certain characteristics, and solve for specific values.

# Iterating with VLATI-TXT and the command line

This page will be based around a pipeline. It will detail different commands that can be added to the pipeline.

The pipeline will have the following format:

```console
VLATI-TXT command | pipe 1 | pipe 2 | ...
```

## Example 1

Here is the first command we'll be working with:

```console
VLATI-TXT output.npz output.pv 200 -s scal -f moon | tail -n2 | head -n1 | sed 's/.*: //'
```

This probably looks daunting at first, but we will deconstruct this and see how each command in the pipeline is applied. At any point, you can check the output of VLATI-TXT before the pipeline is applied (or before any specific part of the pipeline is applied) to see why a specific pipeline command is applied.

**`tail`** gets the last $n$ lines of its input, so `-n2` (or `-n 2`) gets the last two lines of VLATI-TXT's output.

**`head`** gets the first $n$ lines of its input, so `-n1` gets the first line of VLATI-TXT's output.

**`sed`** is the most sophisticated of the commands in the pipeline. It involves a *regex* (REGular EXpression) that removes everything that comes before the first colon of VLATI-TXT's output. Let's break this down a bit more.

The argument that we give to `sed` has six different parts:

1. `s`
2. `/`
3. `.*`
4. `: `
5. `/`
6. `/`

**`s`** tells sed that we want to do a text substitution.

**`/`** tells sed that the regex to substitute is starting.

{: .note }
The following two points select everything up until the colon and space.

**`.*`** tells sed to select everything (until the following character).

**`: `** is a colon and a space. It matches VLATI-TXT's format of `PROPERTY NAME    : NUMERICAL VALUE`.

The next **`/`** tells sed that the regex to substitute has ended. Sed now expects us to give an expression to replace it with. We want to delete it (i.e. replace it with nothing), so we put another `/` to indicate that the replacement string is empty.

## Example 2

The same thing can also be done with only two `sed` segments of the pipeline:

```console
VLATI-TXT output.npz output.pv 200 -s scal -f moon | sed -n '4p' | sed 's/.*: //'
```

### `sed` segment 1

**`-n`** tells sed to disuse its default behavior of printing the entire file.
**`4p`** tells sed to only print the fourth line of VLATI-TXT's output.

### `sed` segment 2

This is that regex that we saw earlier, removing anything that comes before the colon-space sequence that VLATI-TXT produces.
