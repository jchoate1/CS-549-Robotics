---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 1 | Motor Control'
math: mathjax
---

# Motor Control
## Making the Robot Move Precisely

---

# From Planning to Execution

We have a path from A*: [(0,0), (0,1), (0,2), (1,2), ...]

Now we need to:
1. Convert path to motor commands
2. Execute commands accurately
3. **Handle real-world imperfections**

This is where **model meets reality**.

<!-- 
NOTES:
- Path planning was theoretical (model)
- Now we interface with physical hardware (reality)
- The gap between them is THE problem of robotics
-->

---

# The Central Idea: Feedback Control

**Robotics is largely about sensing errors and correcting them.**

```
                    ┌────────────────────┐
     Desired ──────▶│   Compare & Fix    │──────▶ Actual
     State         │  (Error→Correction) │       Outcome
                    └─────────┬──────────┘
                              │
                              │ Measure
                              ▼
                         [  Sensor  ]
```

This pattern appears *everywhere*:
- Motor speed control (encoders)
- Heading control (IMU/gyro)
- Position control (GPS/landmarks)
- Even A* replanning is "feedback" at a higher level

<!-- 
NOTES:
- This is the CORE IDEA of the entire course
- Sense → Compare → Correct → Repeat
- Without feedback, robots fail
-->

---

# DC Motors

The Alvik uses **DC motors** (Direct Current)

- Voltage controls speed
- Polarity controls direction
- Simple and robust

Problem: Open-loop control is imprecise!

<!-- 
NOTES:
- DC motors are common in robotics
- "Open-loop" = no feedback
- Speed varies with load and battery
-->

---

# Open-Loop vs Closed-Loop

**Open-loop**: Send command, hope for the best
```
Set motor to 50% → Robot moves (maybe 10 cm/s?)
```

**Closed-loop**: Measure and correct
```
Want 10 cm/s → Measure actual speed → Adjust motor
```

Encoders enable closed-loop control!

<!-- 
NOTES:
- Open-loop: toaster (timer only)
- Closed-loop: thermostat (measures temperature)
- Robots need closed-loop for accuracy
-->

---

# The Control Loop

```
         ┌─────────────────────────────────┐
         │                                 │
         ▼                                 │
   ┌──────────┐    ┌─────────┐    ┌───────┴──┐
   │ Desired  │───▶│ Compare │───▶│ Controller│
   │  Speed   │    │ (Error) │    │   (PID)   │
   └──────────┘    └────┬────┘    └─────┬─────┘
                        │                │
                        │          ┌─────▼─────┐
                   ┌────┴───┐      │   Motor   │
                   │Encoder │◀─────│           │
                   └────────┘      └───────────┘
```

<!-- 
NOTES:
- Draw the feedback loop on board
- Error = desired - actual
- Controller adjusts motor based on error
-->

---

# PID Control

**P**roportional - **I**ntegral - **D**erivative

$$u(t) = K_p e(t) + K_i \int e(t)dt + K_d \frac{de(t)}{dt}$$

- **P**: React to current error
- **I**: Eliminate persistent error
- **D**: Anticipate future error (damping)

<!-- 
NOTES:
- Most common controller in robotics/industry
- Kp, Ki, Kd are tuning parameters
- Each term has a specific purpose
-->

---

# Proportional (P) Control

Output proportional to error:

$$u = K_p \cdot e$$

- Error large → strong correction
- Error small → gentle correction
- Error zero → no correction

Problem: May never reach target exactly (steady-state error)

<!-- 
NOTES:
- Simplest controller
- Works okay for many cases
- Residual error when load is present
-->

---

# Integral (I) Control

Accumulate error over time:

$$u = K_i \int e \cdot dt$$

- Small persistent error builds up
- Eventually forces correction
- Eliminates steady-state error

Problem: Can cause overshoot ("wind-up")

<!-- 
NOTES:
- Integral of small error eventually becomes large
- Good for eliminating offset
- Need to limit ("anti-windup") to prevent instability
-->

---

# Derivative (D) Control

React to rate of change:

$$u = K_d \frac{de}{dt}$$

- Error decreasing → reduce effort
- Error increasing → increase effort
- Provides damping

Problem: Amplifies noise

<!-- 
NOTES:
- Helps prevent overshoot
- Like shock absorber
- Sensitive to noisy measurements
-->

---

# PID in Action

```
          │
  Error   │    ╱╲
          │   ╱  ╲     P only: oscillates
          │──╱────╲─────────────────
          │        ╲  ╱╲  
          │         ╲╱  ╲
          └─────────────────────── time

          │
  Error   │    ╱╲
          │   ╱  ╲     PID: settles quickly
          │──╱────────────────────
          │
          │
          └─────────────────────── time
```

<!-- 
NOTES:
- Draw actual response curves
- P-only often oscillates
- PID reaches target smoothly
-->

---

# Tuning PID

No universal values - depends on your system

General approach:
1. Start with P only, increase until oscillation
2. Add D to reduce oscillation
3. Add I to eliminate steady-state error
4. Fine-tune each

Alvik: Library handles most tuning for you

<!-- 
NOTES:
- Tuning is part art, part science
- Many formal methods (Ziegler-Nichols, etc.)
- For our course, library does the work
-->

---

# Alvik Motor Control

The library provides high-level control:

```python
# Position control (uses PID internally)
alvik.move(20, 'cm')     # Move 20 cm
alvik.rotate(90, 'deg')  # Turn 90 degrees

# Velocity control
alvik.drive(10, 0)       # 10 cm/s forward
alvik.drive(0, 45)       # Rotate 45 deg/s

# Raw wheel control
alvik.set_wheels_speed(left_rpm, right_rpm)
```

<!-- 
NOTES:
- move() and rotate() block until complete
- drive() is continuous velocity control
- Usually use high-level commands
-->

---

# Motion Primitives

Break complex paths into simple motions:

1. **Straight line**: `alvik.move(distance)`
2. **Point turn**: `alvik.rotate(angle)`
3. **Arc**: `alvik.drive(v, omega)`

Lab 1 output → sequence of these commands

<!-- 
NOTES:
- A* gives waypoints
- Convert to move/turn sequence
- We use "stop and turn" for simplicity
-->

---

# Converting Path to Commands

```python
# Path from A*: [(0,0), (0,1), (0,2), (1,2), (2,2)]
# Grid cells are 10cm

Commands:
  move_forward(20)  # (0,0) → (0,2): 2 cells right
  turn_right()       # face down
  move_forward(20)  # (0,2) → (2,2): 2 cells down
```

<!-- 
NOTES:
- This is what path_to_commands() does
- Combine consecutive moves in same direction
- Turn when direction changes
-->

---

# Execution Considerations

Real-world issues:
- **Acceleration**: Don't start at full speed
- **Deceleration**: Slow down before stopping
- **Settling time**: Wait for motion to complete
- **Error checking**: Did we reach the target?

<!-- 
NOTES:
- Jerky motion is bad for accuracy
- Alvik library handles accel/decel
- Small pauses between commands help
-->

---

# Lab 2: Drive Square & UMich Benchmark

Your task:
1. Drive the robot in a 30cm × 30cm square
2. Return to the starting position
3. **Measure and interpret the error**

```python
for i in range(4):
    alvik.move(30, 'cm')
    alvik.rotate(90, 'deg')
```

Run **both clockwise AND counter-clockwise!**

<!-- 
NOTES:
- Seems simple, but reveals odometry errors
- CW vs CCW comparison reveals SYSTEMATIC vs RANDOM errors
- This is a standard industry test
-->

---

# Interpreting Your Results

| What You Measure | What It Means | Action |
|------------------|---------------|--------|
| CW and CCW drift **same direction** | Systematic error (wheel size, alignment) | Can calibrate out |
| CW and CCW drift **opposite directions** | Random error (slip, surface) | Need sensors |
| Error grows with distance | Odometry drift (expected) | Use landmarks |
| Large heading error | Gyro drift or wheel slip | Check turns |

**The numbers tell you what's wrong and how to fix it.**

<!-- 
NOTES:
- Don't just run the test - INTERPRET it
- Systematic errors are correctable
- Random errors need sensor feedback
- This is real engineering analysis
-->

---

# Tips for Lab 2

1. **Start small**: Test with 10cm first
2. **Add pauses**: `time.sleep(0.3)` between moves
3. **Check battery**: Low battery affects performance
4. **Flat surface**: Avoid carpet if possible
5. **Mark start**: Use tape to measure error

<!-- 
NOTES:
- Common debugging tips
- Most issues are physical, not code
- Ask for help if stuck
-->

---

# Summary

1. **DC motors**: Voltage controls speed
2. **Encoders**: Measure rotation for feedback
3. **Closed-loop control**: Measure and correct
4. **PID**: Proportional + Integral + Derivative
5. **Motion primitives**: move, rotate, drive

**Next**: Let's program the Alvik!

<!-- 
NOTES:
- These concepts apply broadly
- PID is everywhere in control systems
- Now time for hands-on work
-->

---

# Lab 2 Time!

Set up your Alvik:
1. Connect via USB
2. Open Thonny
3. Run `01_hello_alvik.py` to test connection
4. Then work on the drive square lab

<!-- 
NOTES:
- Help students with setup issues
- Make sure everyone can connect
- Walk around during lab time
-->
