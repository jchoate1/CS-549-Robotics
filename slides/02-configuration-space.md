---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 1 | Configuration Space'
math: mathjax
---

# Configuration Space
## Representing the Robot's World

---

# The Planning Problem

Given:
- A robot with physical dimensions
- An environment with obstacles
- A start position and goal position

Find:
- A collision-free path from start to goal

<!-- 
NOTES:
- Sounds simple, but the robot has SIZE
- Can't just plan for a point
- Need to account for robot geometry
-->

---

# Workspace vs Configuration Space

## Workspace
The physical space where the robot operates
- 2D floor plan or 3D environment
- Obstacles have physical dimensions
- Robot has physical dimensions

## Configuration Space (C-space)
An abstract space where each point represents a robot configuration
- Robot becomes a **point**
- Obstacles are **expanded**

<!-- 
NOTES:
- Key insight: transform the problem
- Once in C-space, robot is just a point
- Much easier to plan for a point
-->

---

# Configuration

A **configuration** fully specifies the robot's position and orientation.

For a mobile robot on a plane:
$$q = (x, y, \theta)$$

- $x, y$ = position
- $\theta$ = heading angle

For our grid-based planning:
$$q = (row, col)$$

<!-- 
NOTES:
- Configuration = all info needed to place the robot
- For a robot arm, it would be all joint angles
- We'll simplify to just position for now
-->

---

# Why Configuration Space?

![bg right:50% 90%](https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Motion_planning_workspace_vs_configuration_space.svg/400px-Motion_planning_workspace_vs_configuration_space.svg.png)

**Workspace**: Must check if entire robot body collides

**C-space**: Just check if the point is in free space

<!-- 
NOTES:
- Left: workspace with robot body
- Right: C-space with grown obstacles
- Planning in C-space is much simpler
- Trade complexity of collision checking for preprocessing
-->

---

# Building C-space: Obstacle Expansion

For a circular robot with radius $r$:

1. Take each obstacle
2. Expand it by radius $r$ in all directions
3. Robot can now be treated as a point

<!-- 
NOTES:
- This is also called "Minkowski sum"
- Works perfectly for circular robots
- For non-circular, use bounding circle or more complex methods
-->

---

# Example: Obstacle Expansion

```
Original Grid          Expanded Grid (r=1)
                       
. . . . . .           . . . . . .
. . # # . .           . # # # # .
. . # # . .    →      . # # # # .
. . . . . .           . # # # # .
. . . . . .           . . . . . .
```

Robot radius = 1 cell
Each obstacle cell expands to 3x3

<!-- 
NOTES:
- Draw this on the board
- Show how a 2x2 obstacle becomes 4x4
- The robot (as a point) can now safely navigate
-->

---

# Grid-Based Representation

We discretize the environment into a grid:

```python
# 0 = free space, 1 = obstacle
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
```

<!-- 
NOTES:
- Simple but effective representation
- Resolution tradeoff: fine grid = more accuracy but more computation
- Our Alvik is ~10cm, so 10cm grid cells work well
-->

---

# Grid Resolution Tradeoffs

| Fine Grid | Coarse Grid |
|-----------|-------------|
| More accurate paths | Approximate paths |
| More computation | Less computation |
| More memory | Less memory |
| Tight spaces navigable | May miss narrow passages |

Rule of thumb: Cell size ≈ robot radius

<!-- 
NOTES:
- For our course, we use 10cm cells
- Alvik is ~10cm wide, so this works
- In practice, choose based on environment and requirements
-->

---

# Connectivity

How can the robot move between cells?

## 4-Connectivity
Up, down, left, right only
- Simpler
- Paths may be longer

## 8-Connectivity  
Include diagonals
- More natural paths
- Diagonal cost = √2 ≈ 1.414

<!-- 
NOTES:
- Draw both on the board
- 4-connectivity: Manhattan distance
- 8-connectivity: closer to Euclidean
- We'll use 4-connectivity for simplicity, option for 8
-->

---

# Implementing Obstacle Expansion

```python
def expand_obstacles(grid, robot_radius):
    rows, cols = grid.shape
    expanded = grid.copy()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1:  # obstacle
                # Expand in all directions
                for dr in range(-robot_radius, robot_radius + 1):
                    for dc in range(-robot_radius, robot_radius + 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            expanded[nr, nc] = 1
    
    return expanded
```

<!-- 
NOTES:
- This is what students will implement in Lab 1
- Key: check bounds before accessing array
- Could optimize with convolution, but this is clear
-->

---

# Lab 1 Preview: Configuration Space

You will implement `expand_obstacles()`:

```python
# Before expansion
grid = get_simple_grid()  # Has a 3x3 obstacle

# After expansion (robot_radius = 1)
expanded = expand_obstacles(grid, robot_radius=1)
# Obstacle is now 5x5
```

<!-- 
NOTES:
- First part of Lab 1
- Make sure they understand the concept before coding
- Will visualize the results
-->

---

# C-space Limitations

Configuration space expansion assumes:
- **Circular robot** (or bounding circle)
- **Holonomic motion** (can move in any direction)

Our Alvik is:
- Roughly square (~10cm × 10cm)
- Non-holonomic (differential drive)

Approximation is good enough for our purposes.

<!-- 
NOTES:
- Real robots are more complex
- Non-holonomic = can't move sideways
- For precise work, need more sophisticated planning
- Our grid-based approach works well in practice
-->

---

# Summary

1. **Workspace**: Physical environment
2. **Configuration space**: Abstract planning space
3. **Obstacle expansion**: Grow obstacles by robot radius
4. **Grid representation**: Discretize for computation
5. **Connectivity**: 4 or 8 neighbors

**Next**: Path planning algorithms to find routes through C-space

<!-- 
NOTES:
- Make sure these concepts are clear
- Questions before moving on?
- C-space is the foundation for path planning
-->

---

# Questions?

- Configuration space concept clear?
- Obstacle expansion makes sense?
- Grid representation questions?

<!-- 
NOTES:
- Take questions
- Draw examples if helpful
- Transition to path planning
-->
