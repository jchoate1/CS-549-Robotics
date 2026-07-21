---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 1 | Robot Kinematics'
math: mathjax
---

# Robot Kinematics
## How Robots Move

---

# What is Kinematics?

**Kinematics**: The study of motion without considering forces

- **Forward kinematics**: Given motor commands → where does the robot go?
- **Inverse kinematics**: Given desired position → what motor commands?

<!-- 
NOTES:
- Distinguish from dynamics (which includes forces)
- We focus on kinematics - geometry of motion
- Essential for controlling the robot
-->

---

# Differential Drive

Our Alvik uses **differential drive**:

- Two independently driven wheels
- No steering mechanism
- Turn by running wheels at different speeds

![bg right:40% 90%](https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Differential_wheeled_robot.svg/400px-Differential_wheeled_robot.svg.png)

<!-- 
NOTES:
- Most common mobile robot configuration
- Simple and effective
- Same principle as a tank
-->

---

# Differential Drive Motions

| Left Wheel | Right Wheel | Motion |
|------------|-------------|--------|
| Forward | Forward | Drive straight |
| Backward | Backward | Reverse |
| Forward | Backward | Spin right (in place) |
| Backward | Forward | Spin left (in place) |
| Fast | Slow | Arc right |
| Slow | Fast | Arc left |

<!-- 
NOTES:
- Demonstrate with hands or the actual robot
- Point out: can turn in place (zero turning radius)
- Cars can't do this (Ackermann steering)
-->

---

# Coordinate Frame

Define the robot's pose as:

$$q = (x, y, \theta)$$

- $(x, y)$ = position in world frame
- $\theta$ = heading angle (from x-axis)

Convention: $\theta = 0$ is facing right (+x direction)

<!-- 
NOTES:
- Draw coordinate frame on board
- θ increases counter-clockwise
- This is standard robotics convention
-->

---

# Forward Kinematics Equations

For a differential drive robot:

$$\dot{x} = v \cos(\theta)$$
$$\dot{y} = v \sin(\theta)$$
$$\dot{\theta} = \omega$$

where:
- $v$ = linear velocity (forward speed)
- $\omega$ = angular velocity (rotation rate)

<!-- 
NOTES:
- These are the fundamental equations
- v and ω are what we control
- Gives us x, y, θ over time
-->

---

# Relating Wheel Speeds to v and ω

Given wheel velocities $v_L$ (left) and $v_R$ (right):

$$v = \frac{v_L + v_R}{2}$$

$$\omega = \frac{v_R - v_L}{L}$$

where $L$ = distance between wheels (wheelbase)

<!-- 
NOTES:
- v is average of wheel speeds
- ω depends on difference and wheelbase
- Wider wheelbase = slower rotation for same wheel difference
-->

---

# Example Calculations

**Alvik specs:**
- Wheelbase $L \approx 8$ cm
- Max wheel speed ≈ 20 cm/s

**Drive straight**: $v_L = v_R = 10$ cm/s
- $v = 10$ cm/s, $\omega = 0$

**Spin in place**: $v_L = -10$, $v_R = 10$ cm/s
- $v = 0$, $\omega = 20/8 = 2.5$ rad/s ≈ 143°/s

<!-- 
NOTES:
- Work through the math
- Show how to achieve different motions
- Alvik API abstracts this, but good to understand
-->

---

# Odometry

**Odometry**: Estimating position from wheel encoder measurements

Given encoder counts:
1. Calculate distance each wheel traveled
2. Calculate $\Delta v$ and $\Delta \omega$
3. Update $(x, y, \theta)$ estimate

<!-- 
NOTES:
- Encoders count wheel rotations
- Basic position estimation
- Foundation of dead reckoning
-->

---

# Encoder Basics

**Encoder**: Sensor that measures wheel rotation

- Counts "ticks" as wheel rotates
- Typical: 100-1000 ticks per revolution
- Alvik: Built into motor assembly

Distance per tick = $\frac{\pi \cdot d}{N}$

where $d$ = wheel diameter, $N$ = ticks per revolution

<!-- 
NOTES:
- Show encoder diagram if possible
- More ticks = better resolution
- Alvik encoders are handled by the library
-->

---

# Odometry Update Equations

For small time step $\Delta t$:

$$\Delta s = \frac{\Delta s_L + \Delta s_R}{2}$$

$$\Delta \theta = \frac{\Delta s_R - \Delta s_L}{L}$$

$$x_{new} = x + \Delta s \cdot \cos(\theta + \Delta\theta/2)$$
$$y_{new} = y + \Delta s \cdot \sin(\theta + \Delta\theta/2)$$
$$\theta_{new} = \theta + \Delta \theta$$

<!-- 
NOTES:
- Standard odometry update
- Assumes small steps (otherwise need integration)
- Mid-point approximation for angle
-->

---

# Dead Reckoning

**Dead reckoning**: Position estimate based solely on odometry

Start: $(0, 0, 0)$
→ Move forward 10cm
→ Turn right 90°
→ Move forward 10cm
→ Estimate: $(10, -10, -90°)$

Problem: Errors accumulate!

<!-- 
NOTES:
- "Dead" from "deduced" reckoning
- No external references (like GPS or landmarks)
- Works short-term but drifts over time
-->

---

# Sources of Odometry Error

1. **Wheel slippage** - wheels spin without moving
2. **Uneven wheel diameters** - systematic drift
3. **Encoder resolution** - quantization error
4. **Surface irregularities** - bumps and carpet
5. **Timing errors** - sampling rate

<!-- 
NOTES:
- Slippage is worst - happens with acceleration
- Wheel diameter differences cause consistent drift
- This is why Lab 2 measures accuracy
-->

---

# Systematic vs Random Errors

**Systematic errors**: Consistent bias
- One wheel slightly larger → always drift left
- Can be measured and corrected

**Random errors**: Unpredictable
- Wheel slippage
- Surface variations
- Accumulate over time

<!-- 
NOTES:
- Lab 2 (UMich benchmark) helps identify systematic errors
- CW vs CCW comparison reveals systematic drift
- Random errors need external sensors to correct
-->

---

# The UMich Benchmark Test

Standard test for dead reckoning accuracy:

1. Drive a square (1m × 1m)
2. Return to start
3. Measure position error

Repeat clockwise AND counter-clockwise
- Systematic errors show up in CW/CCW difference

<!-- 
NOTES:
- You'll do this in Lab 2
- Developed at University of Michigan
- Industry standard for comparing robots
-->

---

# Alvik Motion API

The Alvik library handles kinematics for you:

```python
# Move a specific distance
alvik.move(20, 'cm')  # forward 20 cm

# Rotate a specific angle
alvik.rotate(90, 'deg')  # turn right 90°

# Velocity control
alvik.drive(v, omega)  # cm/s, deg/s

# Get current pose estimate
x, y, theta = alvik.get_pose()
```

<!-- 
NOTES:
- High-level API abstracts the kinematics
- move() and rotate() use encoders internally
- get_pose() returns odometry estimate
-->

---

# Lab 2 Preview

You will:
1. Drive the Alvik in a 30cm × 30cm square
2. Measure how close it returns to start
3. Run the UMich benchmark test
4. Analyze your results

<!-- 
NOTES:
- This is the first hands-on robot lab
- Make sure robots are charged and ready
- Bring tape to mark starting positions
-->

---

# Summary

1. **Differential drive**: Two independent wheels
2. **Forward kinematics**: Wheel speeds → robot motion
3. **Odometry**: Encoder counts → position estimate
4. **Dead reckoning**: Pure odometry navigation
5. **Errors**: Systematic (correctable) and random

<!-- 
NOTES:
- These concepts apply to most mobile robots
- Understanding kinematics helps debug problems
- Questions?
-->

---

# Questions?

- Differential drive clear?
- Odometry concept understood?
- Ready to try it on the real robot?

<!-- 
NOTES:
- Take questions
- Short break before motor control section
-->
