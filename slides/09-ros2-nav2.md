---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 2 | ROS2 Nav2'
---

# ROS2 Nav2
## Industrial-Strength Navigation

---

# Recap: ROS2 Basics

From yesterday:
- **Nodes**: Processes that compute
- **Topics**: Communication channels
- **Messages**: Data structures

Today: How ROS2 handles navigation

<!-- 
NOTES:
- Quick reminder of ROS2 concepts
- Now we see how it all fits together
- Nav2 is the standard navigation stack
-->

---

# What is Nav2?

**Nav2** = ROS2 Navigation Stack

A complete navigation system:
- Map representation
- Path planning
- Path following
- Obstacle avoidance
- Recovery behaviors

<!-- 
NOTES:
- Production-ready navigation
- Used in industry robots
- Modular and configurable
-->

---

# Nav2 Architecture

```
                    ┌─────────────┐
                    │ BT Navigator│◀── Goal
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
    ┌─────▼─────┐    ┌─────▼─────┐    ┌─────▼─────┐
    │  Planner  │    │ Controller│    │ Recovery  │
    │  Server   │    │  Server   │    │  Server   │
    └─────┬─────┘    └─────┬─────┘    └───────────┘
          │                │
    ┌─────▼─────┐    ┌─────▼─────┐
    │  Costmap  │    │  Costmap  │
    │  (Global) │    │  (Local)  │
    └───────────┘    └───────────┘
```

<!-- 
NOTES:
- Draw and explain the architecture
- Behavior Trees coordinate everything
- Planners and controllers are separate
-->

---

# Costmaps

**Costmap**: Grid-based representation of traversability

Cell values:
- **0**: Free space
- **1-252**: Increasing cost
- **253**: Inscribed (collision possible)
- **254**: Lethal (definite collision)
- **255**: Unknown

<!-- 
NOTES:
- Similar to configuration space!
- But with cost gradients
- Higher cost = less desirable to traverse
-->

---

# Global vs Local Costmap

**Global Costmap:**
- Entire known map
- Updated slowly
- Used for global planning

**Local Costmap:**
- Around the robot
- Updated from live sensors
- Used for local obstacle avoidance

<!-- 
NOTES:
- Two different scales
- Global: where to go (strategy)
- Local: how to avoid obstacles (tactics)
-->

---

# Inflation Layer

Remember configuration space expansion?

Nav2 uses **inflation layer**:
- Obstacles expanded by robot radius
- Gradual cost decrease from obstacle
- Robots prefer paths away from walls

<!-- 
NOTES:
- Same concept as Lab 1!
- But with cost gradients
- Smoother paths result
-->

---

# Global Planner

Finds path from start to goal on global costmap

Planners available:
- **NavFn**: Dijkstra/A* based (like our Lab 1!)
- **Smac**: State lattice planner
- **Theta***: Any-angle paths

```
ros2 param set /planner_server planner_plugins ["GridBased"]
```

<!-- 
NOTES:
- NavFn is essentially A* on costmap
- Same algorithm we implemented!
- Other planners for special cases
-->

---

# Local Controller

Follows the global path while avoiding obstacles

Controllers available:
- **DWB**: Dynamic Window Approach
- **TEB**: Timed Elastic Band
- **MPPI**: Model Predictive Path Integral
- **Pure Pursuit**: Simple geometric following

<!-- 
NOTES:
- Controller tracks the path
- Must react to dynamic obstacles
- Different tradeoffs for each
-->

---

# Recovery Behaviors

What happens when the robot gets stuck?

Recovery behaviors:
- **Spin**: Rotate in place to clear costmap
- **Backup**: Move backward
- **Wait**: Wait for obstacles to clear
- **Clear costmap**: Reset and retry

<!-- 
NOTES:
- Robots get stuck in real life
- Recovery behaviors are essential
- BT Navigator orchestrates these
-->

---

# Behavior Trees

**Behavior Tree**: Coordinates the navigation flow

```
Root
├── NavigateToPose
│   ├── ComputePathToPose
│   ├── FollowPath
│   └── RecoveryFallback
│       ├── Spin
│       ├── Backup
│       └── Wait
```

<!-- 
NOTES:
- Behavior trees are powerful
- Modular and configurable
- Industry standard for robotics
-->

---

# SLAM: Simultaneous Localization and Mapping

**Problem**: Need map to localize, need position to map

**SLAM**: Solve both simultaneously!

Types:
- **Lidar SLAM**: Using laser scans
- **Visual SLAM**: Using cameras
- **Sensor fusion**: Multiple sensors

<!-- 
NOTES:
- Chicken and egg problem
- SLAM is a major research area
- Nav2 can use SLAM-generated maps
-->

---

# Localization: AMCL

**AMCL** = Adaptive Monte Carlo Localization

Particle filter approach:
1. Spread particles across possible positions
2. Weight particles by sensor match
3. Resample toward likely positions
4. Converge on true position

<!-- 
NOTES:
- Used when you have a map already
- Particles represent hypotheses
- Sensor data narrows down options
-->

---

# Demo: Nav2 in Gazebo

Let's see Nav2 in action:

1. Launch Gazebo with maze world
2. Provide goal position
3. Watch the robot:
   - Plan a path
   - Follow the path
   - Avoid obstacles
   - Recover from stuck

<!-- 
NOTES:
- Live demo if possible
- Otherwise show video/screenshots
- Point out the costmaps and path
-->

---

# Nav2 vs Our Alvik Code

| Nav2 (Simulation) | Alvik (MicroPython) |
|-------------------|---------------------|
| Full map available | Unknown maze |
| Global + local planning | Reactive behaviors |
| SLAM/localization | Dead reckoning |
| Complex recovery | Simple backup |
| Many sensors | ToF sensor only |

Both are valid approaches for different contexts!

<!-- 
NOTES:
- Not better/worse, just different
- Nav2 for complex environments
- Reactive for simple, fast
- Understand both approaches
-->

---

# Industry Applications

Nav2 is used in:
- Warehouse robots (picking, delivery)
- Hospital robots (medicine delivery)
- Agriculture (autonomous tractors)
- Inspection robots
- Home robots (cleaning, service)

<!-- 
NOTES:
- Real companies use Nav2
- Amazon, iRobot, etc.
- Skills from this course are relevant
-->

---

# Summary

1. **Nav2**: Complete navigation stack
2. **Costmaps**: Traversability representation
3. **Global planner**: High-level path (A*!)
4. **Local controller**: Path following
5. **Recovery**: Handle stuck situations
6. **SLAM**: Build maps while navigating

<!-- 
NOTES:
- Nav2 brings it all together
- Same concepts we've learned
- Industrial implementation
-->

---

# Questions?

- Nav2 architecture clear?
- Costmap concept understood?
- How it relates to our labs?

<!-- 
NOTES:
- Take questions
- Connect to concepts from Day 1
- Transition to trajectories
-->
