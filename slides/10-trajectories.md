---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 2 | Trajectory Generation'
math: mathjax
---

# Trajectory Generation
## Smooth Robot Motion

---

# Paths vs Trajectories

**Path**: Sequence of positions
- $(x_1, y_1) \rightarrow (x_2, y_2) \rightarrow ...$
- No time information
- Just "where"

**Trajectory**: Path + timing
- Position as function of time: $(x(t), y(t))$
- Includes velocities, accelerations
- "Where" and "when"

<!-- 
NOTES:
- Important distinction
- Path planning gives us the route
- Trajectory planning makes it executable
-->

---

# Why Smooth Trajectories?

Jerky motion is bad:
- Mechanical stress
- Wheel slippage
- Uncomfortable (for passengers)
- Inaccurate execution

Smooth motion:
- Gradual acceleration/deceleration
- Continuous velocities
- Easier to track

<!-- 
NOTES:
- Real robots have inertia
- Can't instantly change velocity
- Smooth = better control
-->

---

# Motion Profile: Trapezoidal

Classic approach: Trapezoidal velocity profile

```
Velocity
   │    ┌──────────┐
   │   /            \
   │  /              \
   │ /                \
   └─────────────────────▶ Time
     Accel  Cruise  Decel
```

- Constant acceleration/deceleration
- Cruise phase at max velocity
- Simple to implement

<!-- 
NOTES:
- Draw the profile
- Explain each phase
- Used in many industrial systems
-->

---

# Trapezoidal Profile Math

Given: max velocity $v_{max}$, acceleration $a$, distance $d$

**Acceleration phase**: 
$t_{accel} = \frac{v_{max}}{a}$, $d_{accel} = \frac{v_{max}^2}{2a}$

**Cruise phase** (if distance permits):
$d_{cruise} = d - 2 \cdot d_{accel}$

**Total time**: 
$t_{total} = 2 \cdot t_{accel} + \frac{d_{cruise}}{v_{max}}$

<!-- 
NOTES:
- Work through the math
- Sometimes no cruise phase (short distances)
- Alvik library may handle this internally
-->

---

# S-Curve Profile

Smoother than trapezoidal: limit jerk (derivative of acceleration)

```
Velocity
   │    ╭──────────╮
   │   ╱            ╲
   │  ╱              ╲
   │ ╱                ╲
   └─────────────────────▶ Time
```

- Continuous acceleration
- More complex to compute
- Even smoother motion

<!-- 
NOTES:
- Even smoother than trapezoidal
- Used in high-precision applications
- Trade-off: complexity vs smoothness
-->

---

# Spline Curves

For curved paths, use **splines**:

Mathematical curves that pass through control points

Types:
- **Cubic splines**: C2 continuous
- **Hermite splines**: Specify tangents at endpoints
- **Bézier curves**: Intuitive control points
- **B-splines**: Local control

<!-- 
NOTES:
- Splines create smooth curves
- Different types for different needs
- We'll focus on Hermite splines
-->

---

# Hermite Splines

Define curve by:
- Two endpoints: $P_0$, $P_1$
- Two tangent vectors: $T_0$, $T_1$

$$P(u) = (2u^3 - 3u^2 + 1)P_0 + (-2u^3 + 3u^2)P_1$$
$$+ (u^3 - 2u^2 + u)T_0 + (u^3 - u^2)T_1$$

where $u \in [0, 1]$

<!-- 
NOTES:
- Classic interpolation method
- Control both position and direction
- Used in the original course materials
-->

---

# Hermite Spline Example

```python
def hermite_point(u, p0, p1, t0, t1):
    """Calculate point on Hermite spline at parameter u."""
    u2 = u * u
    u3 = u2 * u
    
    h1 = 2*u3 - 3*u2 + 1    # Blending functions
    h2 = -2*u3 + 3*u2
    h3 = u3 - 2*u2 + u
    h4 = u3 - u2
    
    x = h1*p0[0] + h2*p1[0] + h3*t0[0] + h4*t1[0]
    y = h1*p0[1] + h2*p1[1] + h3*t0[1] + h4*t1[1]
    
    return (x, y)
```

<!-- 
NOTES:
- This is from the original course Lab 3
- Generate points along the curve
- Then robot follows these points
-->

---

# Following a Trajectory

Given trajectory points, robot must:

1. Know current position (odometry)
2. Find closest point on trajectory
3. Compute steering to track trajectory
4. Adjust speed based on curvature

Methods: Pure pursuit, Stanley, MPC

<!-- 
NOTES:
- Path following is a control problem
- Many algorithms exist
- We'll mention pure pursuit
-->

---

# Pure Pursuit

Simple geometric path following:

1. Find "lookahead point" on path
2. Steer toward that point
3. Repeat

```
         lookahead distance
      ◀───────────────────▶
      
Robot ●──────────────────○ Lookahead point
                          ↘
                           Path
```

<!-- 
NOTES:
- Simple and effective
- Lookahead distance is a tuning parameter
- Short = accurate but jittery
- Long = smooth but may cut corners
-->

---

# Trajectory Timing

Assign time to trajectory points:

1. **Constant time**: Equal $\Delta t$ between points
2. **Constant velocity**: Longer segments take more time
3. **Velocity profile**: Match to trapezoidal/S-curve

```python
# Constant velocity approach
for i in range(len(points) - 1):
    distance = compute_distance(points[i], points[i+1])
    time = distance / desired_velocity
    times.append(time)
```

<!-- 
NOTES:
- Timing affects motion quality
- Constant time on curved paths = variable speed
- Usually want constant velocity
-->

---

# Application to Alvik

The Alvik move() function likely uses:
- Trapezoidal velocity profile
- Encoder feedback for position
- PID for velocity control

For complex paths:
- Generate spline points
- Feed points as sequence of moves
- Or use drive(v, ω) for continuous control

<!-- 
NOTES:
- Alvik API abstracts most of this
- Understanding helps with debugging
- Lab 3 in original course was spline motion
-->

---

# Practical Considerations

1. **Sensor rate**: How fast can you update?
2. **Compute time**: Can you calculate in real-time?
3. **Actuation limits**: Max velocity, acceleration
4. **Obstacles**: May need to replan

Simpler is often better for educational robots!

<!-- 
NOTES:
- Real-time constraints matter
- Alvik doesn't need complex trajectories
- Simple move/rotate is usually fine
-->

---

# Summary

1. **Path vs Trajectory**: Position vs position + time
2. **Velocity profiles**: Trapezoidal, S-curve
3. **Splines**: Smooth curved paths
4. **Path following**: Pure pursuit and others
5. **Timing**: Match trajectory to robot capabilities

For Lab 5: Simple waypoint following is sufficient!

<!-- 
NOTES:
- Trajectories matter for advanced applications
- Our maze challenge uses simpler approach
- Good to understand the concepts though
-->

---

# Questions?

- Trajectory concepts clear?
- Spline math make sense?
- How this applies to our robot?

<!-- 
NOTES:
- Take questions
- Transition to advanced topics and wrap-up
-->
