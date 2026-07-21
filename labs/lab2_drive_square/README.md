# Lab 2: Drive Square & Dead Reckoning Accuracy

## Objectives

1. Program the Alvik to drive in a square using motor encoders
2. Measure dead reckoning accuracy using the University of Michigan Benchmark test
3. Understand sources of odometry error

## Background

**Dead reckoning** is the process of estimating your current position based on a previously known position, plus estimated speeds over elapsed time. For wheeled robots, this typically uses wheel encoder counts to estimate distance traveled.

**Sources of Error:**
- Wheel slippage
- Unequal wheel diameters
- Encoder resolution limits
- Surface irregularities
- Systematic vs. random errors

## Part 1: Drive a Square

### Task

Write a MicroPython program that drives the Alvik in a 30cm x 30cm square, returning to the starting position.

### Starter Code

Use `drive_square_starter.py` as your starting point. Fill in the `TODO` sections.

### Requirements

1. Square should be 30 cm on each side
2. Robot should return close to starting position
3. Use encoder-based movement (`alvik.move()` and `alvik.rotate()`)
4. Add LED indicators to show progress

### Testing

1. Mark your starting position with tape
2. Run the program
3. Observe where the robot ends up relative to the start
4. Measure the error in X and Y directions

## Part 2: UMich Benchmark Test

The University of Michigan Benchmark is a standard test for measuring dead reckoning accuracy.

### Unidirectional Test (CW)

1. Mark starting position
2. Drive a 1m x 1m square (clockwise)
3. Measure final position error (X, Y, θ)
4. Repeat 3 times
5. Record results

### Bidirectional Test (CCW)

1. Same as above, but counter-clockwise
2. Repeat 3 times
3. Record results

### Analysis

Compare CW vs CCW results. Systematic errors (e.g., one wheel slightly larger) will cause consistent drift in one direction, while random errors will show variance.

## Deliverables

1. `drive_square.py` - Your working square-driving code
2. `umich_benchmark.py` - Code for the benchmark test
3. `results.md` - Table of your measurements and brief analysis

## Hints

- Start with a smaller square (10cm) to test your logic
- Use `time.sleep()` between commands to let the robot settle
- The Alvik's `move()` function blocks until complete
- Check battery level - low battery affects motor performance

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Square driving works | 30 |
| Returns close to start (< 5cm error) | 20 |
| UMich benchmark completed | 25 |
| Analysis of results | 15 |
| Code quality & documentation | 10 |
| **Total** | **100** |
