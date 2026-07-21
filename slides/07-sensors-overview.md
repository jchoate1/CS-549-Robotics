---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 2 | Sensors'
math: mathjax
---

# Day 2: Sensors
## Perceiving the World

---

# Day 1 Recap

Yesterday we covered:
- Configuration space & obstacle expansion
- A* path planning algorithm
- Robot kinematics (differential drive)
- Motor control & encoders
- ROS2 introduction

**Today**: Sensors, maze algorithms, and the maze challenge!

<!-- 
NOTES:
- Quick recap to get everyone on the same page
- Ask if anyone has questions from yesterday
- Make sure all robots are working
-->

---

# Why Sensors?

Dead reckoning alone is not enough:
- Errors accumulate
- No awareness of obstacles
- Can't adapt to changes

Sensors enable:
- **Obstacle detection**
- **Localization correction**
- **Environment mapping**

<!-- 
NOTES:
- We saw dead reckoning drift in Lab 2
- Sensors are essential for autonomy
- Different sensors for different tasks
-->

---

# Sensor Categories

| Category | Examples | Use |
|----------|----------|-----|
| **Proprioceptive** | Encoders, IMU | Internal state |
| **Exteroceptive** | Camera, Lidar | External world |
| **Active** | Ultrasonic, ToF | Emit energy |
| **Passive** | Camera, IR | Receive only |

<!-- 
NOTES:
- Proprioceptive = sensing self
- Exteroceptive = sensing environment
- Active sensors have more control but use power
-->

---

# Sensors on Alvik

| Sensor | Type | Use |
|--------|------|-----|
| Wheel encoders | Proprioceptive | Odometry |
| IMU (Accel + Gyro) | Proprioceptive | Orientation |
| ToF distance | Active, exteroceptive | Obstacle detection |
| Line sensors (IR) | Active, exteroceptive | Line following |

<!-- 
NOTES:
- Point to each sensor on the physical robot
- We'll focus on the ToF sensor today
- Line sensors are bonus if time permits
-->

---

# Time-of-Flight (ToF) Sensors

**Principle**: Measure time for light to reflect back

$$d = \frac{c \cdot t}{2}$$

- $c$ = speed of light
- $t$ = round-trip time
- $d$ = distance

Alvik uses VL53L5CX: 8×8 zone array

<!-- 
NOTES:
- ToF = very fast and accurate
- Alvik sensor gives 5 distance readings
- Left, center-left, center, center-right, right
-->

---

# Alvik Distance Sensor

Returns 5 values in **centimeters**:

```python
left, center_left, center, center_right, right = alvik.get_distance()

# Example output:
# (41.6, 37.5, 41.2, 45.0, 37.1) cm
```

Wide field of view, useful for:
- Obstacle detection
- Determining obstacle direction
- Wall following

<!-- 
NOTES:
- We tested this yesterday
- 5 zones cover ~60° field of view
- Very useful for navigation decisions
-->

---

# Using Distance for Navigation

Simple obstacle avoidance:

```python
THRESHOLD = 15  # cm

left, cl, center, cr, right = alvik.get_distance()

if center < THRESHOLD:
    # Obstacle ahead - decide which way to turn
    if left > right:
        turn_left()
    else:
        turn_right()
else:
    drive_forward()
```

<!-- 
NOTES:
- Basic reactive behavior
- Decide based on which side has more space
- This is the foundation of wall following
-->

---

# Ultrasonic Sensors

**Principle**: Measure time for sound to reflect

$$d = \frac{v_{sound} \cdot t}{2}$$

- Cheaper than ToF
- Wider beam (less precise)
- Range: typically 2cm - 400cm
- Speed of sound ≈ 343 m/s

<!-- 
NOTES:
- Classic robotics sensor (HC-SR04)
- Alvik uses ToF instead
- Good to know about ultrasonic too
-->

---

# Infrared (IR) Line Sensors

Detect surface reflectance:
- **Dark surface**: Low reflection (line)
- **Light surface**: High reflection (background)

```python
left, center, right = alvik.get_line_sensors()

# Low values = dark (on the line)
# High values = light (off the line)
```

<!-- 
NOTES:
- Used for line following
- Simple but effective
- We may demo if time permits
-->

---

# Inertial Measurement Unit (IMU)

Combines:
- **Accelerometer**: Linear acceleration (g)
- **Gyroscope**: Angular velocity (°/s)

```python
# Get acceleration
ax, ay, az = alvik.get_accelerations()

# Get rotation rates
gx, gy, gz = alvik.get_gyros()

# Get orientation (integrated)
roll, pitch, yaw = alvik.get_orientation()
```

<!-- 
NOTES:
- Accelerometer measures tilt and acceleration
- Gyro measures rotation rate
- Combine for orientation estimate
-->

---

# IMU Applications

- **Tilt detection**: Is the robot level?
- **Heading**: Which way are we facing?
- **Collision detection**: Sudden deceleration
- **Complementary filter**: Combine with encoders

IMU + Encoders = Better odometry

<!-- 
NOTES:
- IMU drifts over time (gyro)
- Accelerometer is noisy
- Sensor fusion combines strengths
-->

---

# Sensor Fusion

Combining multiple sensors for better estimates:

```
Encoders:  Good for small movements, drift over time
IMU:       Good for rotation, drift over time
Distance:  Good for obstacle position, no self-localization
```

Together: Complementary information

<!-- 
NOTES:
- No single sensor is perfect
- Kalman filter is the classic fusion technique
- Beyond our scope, but important concept
-->

---

# Sensor Noise

All sensors have noise:

```
Actual distance: 25.0 cm
Readings: 24.8, 25.3, 24.9, 25.1, 25.0, 24.7, ...
```

Mitigation strategies:
- **Averaging**: Take multiple readings
- **Median filter**: Reject outliers
- **Low-pass filter**: Smooth over time

<!-- 
NOTES:
- Real sensors are never perfect
- Filter to reduce noise
- Don't over-filter (introduces lag)
-->

---

# Lab 3: Distance Sensor

Your task:
1. Read distance sensor values
2. Implement obstacle detection
3. Make LED change color based on distance
   - Green: > 30 cm
   - Yellow: 15-30 cm
   - Red: < 15 cm

<!-- 
NOTES:
- Build on example code from yesterday
- Practice with the sensor before maze algorithms
- Should be quick lab (~30 min)
-->

---

# Summary

1. **ToF sensor**: Fast, accurate distance
2. **5-zone array**: Direction information
3. **IR line sensors**: Surface reflectance
4. **IMU**: Orientation and motion
5. **Sensor fusion**: Combine for robustness

**Next**: Maze-solving algorithms!

<!-- 
NOTES:
- Sensors enable reactive behaviors
- Foundation for autonomous navigation
- Questions before maze algorithms?
-->
