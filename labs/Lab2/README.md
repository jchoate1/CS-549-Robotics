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

Compare CW vs CCW results:

| What You Observe | What It Means | Possible Fix |
|------------------|---------------|--------------|
| CW and CCW drift in **same direction** | Systematic error (e.g., wheel diameter mismatch) | Calibrate wheel ratio |
| CW and CCW drift in **opposite directions** | Random error (slip, surface) | Need external sensors |
| Consistent rotation error | Wheelbase measurement wrong | Calibrate wheelbase |
| Error grows with distance | Normal odometry drift | Use landmarks/sensors |
| Large variance between runs | Surface or grip problems | Use better surface |

**Key insight**: Systematic errors can be calibrated out. Random errors require sensor feedback to correct.

### Questions to Answer in Your Analysis

1. What was your average position error? How does it compare to the distance traveled?
2. Did CW and CCW drift in the same or opposite directions? What does this tell you?
3. Was heading (angle) error larger or smaller than position error?
4. Based on your results, when would you need to add sensor feedback?

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
