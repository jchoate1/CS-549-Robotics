---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 2 | Maze Algorithms'
---

# Maze-Solving Algorithms
## Reactive Navigation

---

# The Maze Problem

Given:
- A robot in a maze
- No map (or partial map)
- Goal: Reach the exit

Different from path planning:
- Don't know the full maze
- Must explore and react

<!-- 
NOTES:
- Path planning assumes known map
- Maze solving often has unknown map
- Reactive behaviors are key
-->

---

# Classes of Maze Algorithms

1. **Memoryless** (no state)
   - Wall follower
   - Random walk

2. **With memory**
   - Pledge algorithm
   - Trémaux's algorithm
   - Flood fill

<!-- 
NOTES:
- Memoryless = simple but limited
- Memory = more capable but complex
- We'll cover several approaches
-->

---

# Algorithm 1: Wall Following

**Rule**: Keep one wall on your side, follow it

```
Right-hand rule:
1. Keep right wall on your right
2. Turn right when possible
3. Turn left when can't go right or forward
4. Turn around if completely blocked
```

<!-- 
NOTES:
- Simplest complete algorithm
- Works for "simply connected" mazes
- Not optimal, but guaranteed to find exit
-->

---

# Wall Following Demo

```
┌─────────────┐
│ S──▶       │
│     ┌───┐  │
│     │   │  │
│     └───┘  │  Robot follows right wall:
│            │  S → down → right → up → right → ...
│        ┌───┤
│        │ E │
└────────┴───┘
```

<!-- 
NOTES:
- Draw the path the robot takes
- Show how it eventually reaches E
- Not the shortest path!
-->

---

# Wall Following Implementation

```python
THRESHOLD = 15  # cm

def wall_follow_right():
    left, cl, center, cr, right = alvik.get_distance()
    
    if right > THRESHOLD:
        # No wall on right - turn right to find it
        turn_right()
        move_forward()
    elif center > THRESHOLD:
        # Wall on right, clear ahead - go forward
        move_forward()
    elif left > THRESHOLD:
        # Blocked right and ahead - turn left
        turn_left()
    else:
        # Blocked everywhere - turn around
        turn_around()
```

<!-- 
NOTES:
- This is the core logic
- Priority: turn right > forward > turn left > turn around
- Students will implement in Lab 4
-->

---

# Wall Following Limitations

Works only for **simply connected** mazes:
- All walls connected to outer boundary
- No isolated islands

**Fails** for:
- Mazes with loops around the goal
- Isolated obstacles in open space

<!-- 
NOTES:
- Draw example where it fails
- Robot circles island forever
- Need smarter algorithms for complex mazes
-->

---

# Algorithm 2: Pledge Algorithm

Modification to handle loops:

1. Pick a direction (e.g., North)
2. Walk toward that direction when possible
3. When hitting a wall, follow it (left or right)
4. **Key**: Track total turning angle
5. Leave wall when facing original direction AND turning = 0°

<!-- 
NOTES:
- The turning counter is crucial
- Prevents getting stuck in loops
- Works on more complex mazes
-->

---

# Pledge Algorithm Example

```
Initial direction: East (→)
Turning counter: 0

1. Walk East until wall       turns: 0
2. Turn left, follow wall     turns: +90°
3. Turn left again            turns: +180°
4. Turn right                 turns: +90°
5. Turn right (facing East)   turns: 0 ← LEAVE WALL!
```

<!-- 
NOTES:
- Walk through step by step
- Turning counter prevents false exits
- More complex than simple wall following
-->

---

# Algorithm 3: Trémaux's Algorithm

**Mark the passages** you've traveled:

1. Pick any passage, mark once
2. At dead end, turn around
3. At junction:
   - Prefer unmarked passages
   - Never enter twice-marked passages
   - Mark passage when leaving

Guaranteed to find exit and explores efficiently

<!-- 
NOTES:
- Requires memory/marking capability
- Optimal for exploring unknown mazes
- Classic CS algorithm (1880s!)
-->

---

# Algorithm 4: Flood Fill

Used by Micromouse competitors:

1. Assign distance values from goal
2. Always move toward lower value
3. Update values as you learn the maze

**Optimal** path once maze is known!

<!-- 
NOTES:
- Micromouse competitions use this
- Two phases: explore and speed run
- Very fast once map is complete
-->

---

# Flood Fill Visualization

```
Initial (goal at bottom-right):

? ? ? ?      5 4 3 2
? ? ? ?  →   4 3 2 1
? ? ? ?      3 2 1 0
? ? ? G      2 1 0 G

Robot at top-left follows decreasing numbers
```

<!-- 
NOTES:
- ? = unknown, fill in as explored
- Numbers = distance to goal
- Like wavefront planning but incremental
-->

---

# Choosing an Algorithm

| Algorithm | Complexity | Optimal | Memory |
|-----------|------------|---------|--------|
| Wall follow | Simple | No | None |
| Pledge | Medium | No | Counter |
| Trémaux | Medium | Explores all | Marks |
| Flood fill | Complex | Yes | Full map |

For our course: **Wall following** is sufficient

<!-- 
NOTES:
- Match algorithm to requirements
- Wall following is fine for simple mazes
- Flood fill is overkill for our maze
-->

---

# Lab 4: Wall Following

Implement wall-following behavior:

```python
while not at_goal():
    left, cl, center, cr, right = alvik.get_distance()
    
    # Your wall-following logic here
    # Use right-hand rule
```

Test in the physical maze!

<!-- 
NOTES:
- Build on Lab 3 sensor code
- Start simple, refine
- Test in maze when ready
-->

---

# Tips for Maze Navigation

1. **Tune thresholds**: What distance is "too close"?
2. **Add hysteresis**: Avoid oscillation
3. **Go slow**: Easier to control
4. **Handle corners**: May need special cases
5. **Test incrementally**: One behavior at a time

<!-- 
NOTES:
- Thresholds depend on maze size
- Too sensitive = jittery behavior
- Start slow, speed up when working
-->

---

# Common Issues

**Robot oscillates at wall:**
- Add dead band to threshold
- Or use PD control for wall distance

**Robot clips corners:**
- Turn earlier
- Add diagonal check

**Robot gets stuck:**
- Add timeout and recovery behavior

<!-- 
NOTES:
- Debugging tips
- Real-world issues you'll encounter
- Ask for help if stuck
-->

---

# Summary

1. **Wall following**: Simple, works for most mazes
2. **Pledge algorithm**: Handles loops
3. **Trémaux**: Systematic exploration
4. **Flood fill**: Optimal but complex

**For Lab 5**: Use wall following (or more advanced if you want!)

<!-- 
NOTES:
- Wall following is the baseline
- Extra credit for fancier algorithms
- Now let's work on the implementation
-->

---

# Lab 4 Time!

Implement wall following on your Alvik:

1. Use distance sensor readings
2. Implement right-hand rule
3. Test in the maze

Ask for help if you get stuck!

<!-- 
NOTES:
- Allocate 45-60 minutes
- Walk around and help
- Have maze set up and ready
-->
