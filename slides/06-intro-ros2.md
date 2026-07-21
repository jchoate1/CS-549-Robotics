---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 1 | Introduction to ROS2'
---

# Introduction to ROS2
## The Robot Operating System

---

# What is ROS?

**ROS** = Robot Operating System

Not actually an OS, but a **middleware framework**:
- Communication between components
- Standard interfaces and messages
- Reusable packages and tools
- Active community

<!-- 
NOTES:
- Very important in industry and research
- Used by most robot companies
- Not running on Alvik directly, but important to know
-->

---

# Why ROS2?

**ROS1** (2007-2020s): Great but showing age
- Single point of failure
- Not real-time capable
- Security limitations

**ROS2** (2017-present): Modern rewrite
- Distributed architecture
- Real-time support
- Industry-grade security
- Better Windows/Mac support

<!-- 
NOTES:
- ROS2 is the future
- Most new projects use ROS2
- ROS1 still common in legacy systems
-->

---

# ROS2 Core Concepts

1. **Nodes**: Individual processes
2. **Topics**: Named channels for messages
3. **Messages**: Data structures
4. **Services**: Request/response
5. **Actions**: Long-running tasks

<!-- 
NOTES:
- These are the building blocks
- We'll focus on nodes, topics, and messages
- Services and actions are more advanced
-->

---

# Nodes

A **node** is a process that performs computation

Examples:
- Camera driver node
- Object detection node
- Path planning node
- Motor control node

Nodes communicate via **topics**

<!-- 
NOTES:
- Think of nodes as modules or microservices
- Each does one thing well
- Combine nodes to build systems
-->

---

# Topics

A **topic** is a named communication channel

- Nodes **publish** messages to topics
- Nodes **subscribe** to topics to receive messages
- Many-to-many communication

```
camera_node ─────▶ /camera/image ─────▶ detection_node
                                  ─────▶ display_node
```

<!-- 
NOTES:
- Decoupled communication
- Publishers don't know who subscribes
- Multiple subscribers can receive same data
-->

---

# Messages

**Messages** are structured data types

```
# geometry_msgs/Twist.msg
Vector3 linear    # x, y, z velocities
Vector3 angular   # roll, pitch, yaw rates
```

Standard message types for:
- Sensor data (images, point clouds, IMU)
- Robot state (odometry, joint positions)
- Commands (velocity, goals)

<!-- 
NOTES:
- Standard messages promote reuse
- Define your own for custom data
- Strong typing prevents errors
-->

---

# Example: Robot Architecture

```
                    ┌──────────────┐
                    │  /cmd_vel    │
┌─────────┐         │   (Twist)    │         ┌────────────┐
│ Planner │────────▶│              │────────▶│Motor Driver│
└─────────┘         └──────────────┘         └────────────┘
     ▲
     │
     │              ┌──────────────┐
     │              │   /scan      │
     └──────────────│   (LaserScan)│◀────────┌────────────┐
                    └──────────────┘         │   Lidar    │
                                             └────────────┘
```

<!-- 
NOTES:
- Draw the data flow
- Planner subscribes to sensor, publishes commands
- Motor driver subscribes to commands
- Lidar publishes sensor data
-->

---

# Common ROS2 Commands

```bash
# List running nodes
ros2 node list

# List topics
ros2 topic list

# View messages on a topic
ros2 topic echo /cmd_vel

# Publish a message
ros2 topic pub /cmd_vel geometry_msgs/Twist \
  "{linear: {x: 0.5}, angular: {z: 0.0}}"
```

<!-- 
NOTES:
- These are the basic debugging tools
- Very useful for understanding system state
- Demo if time permits
-->

---

# ROS2 + Simulation

**Gazebo**: Physics simulator that integrates with ROS2

- Test algorithms without real robot
- No risk of damage
- Faster iteration

We'll use Gazebo for maze navigation demos

<!-- 
NOTES:
- Simulation is crucial for development
- Test dangerous scenarios safely
- Can run many experiments quickly
-->

---

# Nav2: Navigation Stack

**Nav2** is the ROS2 navigation package:

- **Costmaps**: Obstacle representation
- **Planners**: Global path planning (like A*!)
- **Controllers**: Path following
- **Recovery behaviors**: Handle failures

<!-- 
NOTES:
- Industrial-strength navigation
- Uses same concepts we learned (C-space, A*)
- Tomorrow we'll see it in action
-->

---

# Why Not ROS2 on Alvik?

Running ROS2 directly on Alvik is complex:
- Requires micro-ROS bridge
- Limited compute on ESP32
- Setup time exceeds our course

Our approach:
- **Simulation**: ROS2 + Gazebo for concepts
- **Hardware**: MicroPython on Alvik

<!-- 
NOTES:
- Practical tradeoff for this course
- Students get exposure to both
- micro-ROS is a thing, but advanced
-->

---

# Demo: ROS2 + Gazebo

Let's see a simulated robot navigate a maze:

```bash
# Launch simulation (if set up)
ros2 launch maze_world maze_navigation.launch.py
```

Observe:
- Costmap visualization
- Planned path
- Robot following path

<!-- 
NOTES:
- Live demo if ROS2 is installed
- Otherwise show video
- Point out key concepts in action
-->

---

# Tomorrow: More ROS2

We'll explore:
- Nav2 architecture in detail
- Costmaps and planners
- SLAM concepts (mapping while navigating)

For now, understand:
- Nodes, topics, messages
- Why ROS2 matters in industry

<!-- 
NOTES:
- Today is just introduction
- Tomorrow goes deeper
- Focus on concepts, not syntax
-->

---

# Summary

1. **ROS2**: Middleware for robot software
2. **Nodes**: Processes that do computation
3. **Topics**: Communication channels
4. **Messages**: Structured data
5. **Nav2**: Navigation stack
6. **Gazebo**: Simulation environment

<!-- 
NOTES:
- ROS2 is essential knowledge for roboticists
- We're just scratching the surface
- Encourage further exploration after course
-->

---

# Day 1 Wrap-Up

Today we covered:
- ✅ Configuration space
- ✅ A* path planning
- ✅ Robot kinematics
- ✅ Motor control & encoders
- ✅ ROS2 introduction

**Tomorrow**: Sensors, maze algorithms, and the maze challenge!

<!-- 
NOTES:
- Recap the day
- Take questions
- Remind about start time tomorrow
-->

---

# Questions?

- Anything unclear from today?
- Questions about tomorrow?
- Issues with your robot?

See you tomorrow!

<!-- 
NOTES:
- Final Q&A
- Make sure students are set for tomorrow
- Encourage them to review materials tonight
-->
