---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 2 | Advanced Topics & Wrap-Up'
---

# Advanced Topics
## Where to Go Next

---

# What We've Covered

Day 1:
- ✅ Configuration space
- ✅ A* path planning
- ✅ Robot kinematics
- ✅ Motor control
- ✅ ROS2 introduction

Day 2:
- ✅ Sensors
- ✅ Maze algorithms
- ✅ Nav2 navigation
- ✅ Trajectories

<!-- 
NOTES:
- Review what we've learned
- A lot in two days!
- Foundation for more advanced topics
-->

---

# SLAM Deep Dive

**Simultaneous Localization and Mapping**

We mentioned it briefly. Key approaches:

- **EKF-SLAM**: Extended Kalman Filter
- **Particle Filter SLAM**: FastSLAM
- **Graph-based SLAM**: Pose graph optimization
- **Visual SLAM**: ORB-SLAM, RTAB-Map

Active research area with many open problems!

<!-- 
NOTES:
- SLAM is a deep field
- Entire courses dedicated to it
- Essential for autonomous robots
-->

---

# Sensor Fusion

Combining multiple sensors optimally

**Kalman Filter**: Optimal estimator for linear systems
- Prediction step (motion model)
- Update step (sensor measurement)
- Covariance tracking

**Extended Kalman Filter (EKF)**: For nonlinear systems

**Particle Filters**: For highly nonlinear systems

<!-- 
NOTES:
- Kalman filter is fundamental
- Used everywhere in robotics
- Mathematical but powerful
-->

---

# Odometry vs. Localization

We've been using **odometry** (dead reckoning):
- Integrate wheel encoders over time
- Simple, always available
- **Problem**: Drift accumulates forever

**Localization** uses external references:
- Landmarks, beacons, GPS
- Maps and matching
- **Advantage**: Bounded error

*Odometry tells you where you THINK you are.*
*Localization tells you where you ACTUALLY are.*

<!-- 
NOTES:
- This is a fundamental distinction
- Odometry is short-term; localization is long-term
- SLAM combines both: build map while localizing
-->

---

# Vision for Robotics: Edge Impulse Demo

**Edge Impulse** makes ML on microcontrollers accessible:

1. Collect images (e.g., "obstacle" vs "clear path")
2. Train a neural network in browser
3. Deploy to embedded device
4. Robot classifies what it sees in real-time

```
Camera → NN inference → "obstacle detected" → React
```

**Try it**: edgeimpulse.com (free account)

<!-- 
NOTES:
- This is what the original course included
- Show the website, maybe a quick video
- Position as "exposure" not "mastery"
-->

---

# Vision: What's Possible

Modern vision enables:

- **Object detection**: YOLO sees "chair at (x,y)"
- **Semantic segmentation**: Pixel-wise "this is floor"
- **Visual odometry**: Motion from camera frames
- **Depth estimation**: Single camera → 3D
- **Person following**: Track and follow humans

For Alvik: Could add a camera module for projects!

<!-- 
NOTES:
- Cameras are cheap and information-rich
- Processing is the challenge
- GPU acceleration helps, but Edge Impulse works on MCUs
-->

---

# Multi-Robot Systems

When one robot isn't enough:

- **Swarm robotics**: Simple rules, emergent behavior
- **Multi-robot planning**: Coordination
- **Communication**: Distributed systems
- **Formation control**: Maintaining patterns

<!-- 
NOTES:
- Warehouse robots work in teams
- Coordination is challenging
- Interesting research problems
-->

---

# Robot Manipulation

We focused on mobile robots. Manipulation is another world:

- **Robot arms**: Kinematics, dynamics
- **Grasping**: How to pick things up
- **Motion planning**: In high-dimensional spaces
- **Force control**: Gentle manipulation
- **Mobile manipulation**: Arms on mobile bases

<!-- 
NOTES:
- Manipulation is harder than locomotion
- Different set of challenges
- Growing area with warehouse applications
-->

---

# Real-Time Systems

Robots need real-time guarantees:

- **Real-time OS**: Predictable timing
- **Control loops**: 100Hz - 1kHz
- **Sensor processing**: Low latency
- **Safety systems**: Guaranteed response

ROS2 has real-time capabilities (vs ROS1)

<!-- 
NOTES:
- Real-time != fast
- Real-time = predictable
- Critical for safety
-->

---

# Hardware Platforms

Beyond Alvik, many platforms exist:

- **TurtleBot**: ROS reference platform
- **Clearpath**: Jackal, Husky
- **Boston Dynamics**: Spot, Atlas
- **DJI**: Drones
- **Custom builds**: For specific needs

<!-- 
NOTES:
- Different robots for different tasks
- Alvik is great for learning
- Industry uses more capable platforms
-->

---

# Safety & Failure Modes

Real robots can fail in dangerous ways. Common pitfalls:

| Failure | Cause | Prevention |
|---------|-------|------------|
| **Runaway loop** | No exit condition | Always check sensors |
| **Bad sensor read** | Noise, disconnection | Validate readings |
| **Motor saturation** | Asking for impossible speed | Clamp commands |
| **Timing drift** | Blocking operations | Use non-blocking code |
| **Battery death** | Forgot to monitor | Check voltage |

**Rule**: Never trust a single sensor reading.

<!-- 
NOTES:
- These are REAL bugs students will encounter
- Professional robots have safety systems
- Even our simple maze robot should check for stuck conditions
-->

---

# Defensive Coding for Robots

```python
# BAD: Drives forever if sensor fails
while True:
    if distance > 20:
        drive_forward()

# GOOD: Has timeout and sanity checks
start_time = time.time()
while time.time() - start_time < 60:  # 60 second max
    distance = alvik.get_distance()
    
    # Sanity check sensor
    if distance[2] < 0 or distance[2] > 200:
        alvik.stop()
        print("Sensor error!")
        break
        
    if distance[2] > 20:
        drive_forward()
    else:
        handle_obstacle()
```

<!-- 
NOTES:
- Always have timeouts
- Always validate sensor data
- Always have a way to stop
-->

---

# Resources for Continued Learning

**Books:**
- *Probabilistic Robotics* - Thrun, Burgard, Fox
- *Planning Algorithms* - LaValle (free online)
- *Introduction to Autonomous Mobile Robots* - Siegwart

**Online:**
- ROS2 tutorials: docs.ros.org
- Coursera: Robotics Specialization (UPenn)
- YouTube: Cyrill Stachniss lectures
- Edge Impulse: edgeimpulse.com (vision ML)

<!-- 
NOTES:
- Recommend specific resources
- Probabilistic Robotics is the bible
- LaValle is free and comprehensive
-->

---

# Projects to Try

With your Alvik:
1. Line following with intersections
2. Multi-room exploration
3. Object pushing/sorting
4. Remote control with smartphone
5. Computer vision integration

Beyond Alvik:
1. Build a robot from scratch
2. Contribute to open-source robotics
3. Enter competitions (Micromouse, RoboCup)

<!-- 
NOTES:
- Encourage continued exploration
- Alvik is a great platform to keep learning
- Competitions are fun and educational
-->

---

# The Maze Challenge

## Final Lab!

Rules:
1. Robot starts at marked position
2. Navigate to goal (marked)
3. Fastest time wins
4. Must be autonomous (no remote control)

Prizes: Bragging rights!

<!-- 
NOTES:
- Set up the competition
- Explain rules clearly
- Keep it fun and low-pressure
-->

---

# Competition Format

1. **Practice runs**: 15 minutes to tune
2. **Official runs**: Each team gets 3 attempts
3. **Timing**: Starts when robot crosses start line
4. **Scoring**: Fastest successful run counts

Tips:
- Don't change code between runs
- Slow and steady beats fast and crashed
- Have fun!

<!-- 
NOTES:
- Set expectations
- Allow practice time
- Keep atmosphere positive
-->

---

# Lab 5: Maze Challenge

Time to put it all together!

Your robot should:
1. Start at the entrance
2. Navigate through the maze
3. Reach the goal/exit

Use everything you've learned:
- Sensor readings
- Wall following (or fancier)
- Motor control

<!-- 
NOTES:
- This is the culmination of the course
- Students should feel prepared
- Assist as needed but don't give answers
-->

---

# Course Summary

You've learned:
1. **Theory**: C-space, A*, kinematics
2. **Algorithms**: Path planning, maze solving
3. **Hardware**: Motors, encoders, sensors
4. **Software**: MicroPython, ROS2 concepts
5. **Practice**: Real robot programming!

<!-- 
NOTES:
- Recap all major topics
- Students have accomplished a lot
- These are real skills
-->

---

# Thank You!

You've completed CS-549 Robotics Intensive!

Remember:
- Robotics combines many disciplines
- Theory + practice = understanding
- Keep building and experimenting

Questions? Comments? Feedback?

<!-- 
NOTES:
- Thank students for participation
- Collect feedback if possible
- Encourage continued learning
-->

---

# Contact & Resources

**Course Repository:**
github.com/jchoate1/CS-549-Robotics

**Instructor:** [Your contact info]

**More resources in the repo's docs folder**

Good luck with your robotics journey!

<!-- 
NOTES:
- Share contact information
- Point to continued resources
- Final goodbye
-->
