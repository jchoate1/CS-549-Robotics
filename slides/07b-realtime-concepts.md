---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 2 | Real-Time Concepts'
---

# Real-Time Concepts
## Timers, Interrupts, and Cooperative Scheduling

---

# Why Timing Matters in Robotics

Robots must:
- Read sensors at regular intervals
- Update motor commands consistently
- Respond to events quickly

**Problem**: Your main loop can't do everything at once.

```python
while True:
    read_sensors()      # Takes 10ms
    compute_path()      # Takes 50ms ← sensor data is stale!
    update_motors()     # Takes 5ms
```

<!-- 
NOTES:
- Real-time doesn't mean "fast"
- Real-time means "predictable timing"
- Missed deadlines cause bad behavior
-->

---

# Approach 1: Polling

Check things repeatedly in a loop:

```python
while True:
    # Check everything every iteration
    distance = alvik.get_distance()
    
    if distance[2] < 15:
        stop()
    else:
        drive_forward()
    
    time.sleep(0.05)  # 50ms = 20 Hz
```

**Pros**: Simple, predictable
**Cons**: Wastes time checking things that haven't changed

<!-- 
NOTES:
- This is what we do in the labs
- Fine for simple robots
- Gets complicated with many tasks
-->

---

# Approach 2: Timers

Schedule tasks to run at specific intervals:

```python
from machine import Timer

def read_sensors(timer):
    global distance
    distance = alvik.get_distance()

# Create timer that fires every 100ms
sensor_timer = Timer(0)
sensor_timer.init(period=100, callback=read_sensors)

# Main loop does other work
while True:
    # Navigate using latest distance value
    navigate(distance)
```

**Pros**: Guaranteed timing, parallel-ish behavior
**Cons**: Must be careful with shared data

<!-- 
NOTES:
- Timer runs in background
- Main loop uses latest data
- Be careful: timer callback interrupts main code
-->

---

# Approach 3: Interrupts

Hardware signals trigger immediate response:

```python
from machine import Pin

def button_pressed(pin):
    alvik.stop()  # Emergency stop!
    
# Set up interrupt on button pin
button = Pin(2, Pin.IN)
button.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)
```

**Pros**: Immediate response (microseconds)
**Cons**: Complex, can cause race conditions

<!-- 
NOTES:
- Interrupts are powerful but tricky
- Use for safety-critical responses
- Keep interrupt handlers SHORT
-->

---

# Approach 4: Cooperative Scheduling (asyncio)

Multiple "tasks" take turns:

```python
import asyncio

async def sensor_task():
    while True:
        distance = alvik.get_distance()
        await asyncio.sleep_ms(100)

async def motor_task():
    while True:
        update_motors()
        await asyncio.sleep_ms(50)

# Run both "concurrently"
asyncio.run(asyncio.gather(sensor_task(), motor_task()))
```

**Pros**: Clean code structure, explicit yielding
**Cons**: Tasks must cooperate (no preemption)

<!-- 
NOTES:
- asyncio is powerful for complex robots
- Each task "yields" to let others run
- Original course had asyncio lab
-->

---

# Cooperative vs. Preemptive

| Type | How It Works | Example |
|------|--------------|---------|
| **Cooperative** | Tasks yield voluntarily | asyncio, Arduino loop |
| **Preemptive** | OS forcibly switches tasks | Linux, FreeRTOS |

MicroPython on Alvik: Cooperative (asyncio)
ROS2: Preemptive (runs on Linux)

<!-- 
NOTES:
- Alvik is single-threaded, cooperative
- ROS2 uses real OS scheduling
- Different tradeoffs
-->

---

# Pitfalls: What Can Go Wrong

## Runaway Loops
```python
while True:
    motor.forward()  # Never checks anything!
```
Robot drives forever. Always have exit conditions.

## Blocking Operations
```python
distance = sensor.read()  # Blocks for 50ms
# Meanwhile, robot is still moving!
```

## Timing Drift
```python
while True:
    do_stuff()           # Takes variable time
    time.sleep(0.1)      # Total time > 100ms
```

<!-- 
NOTES:
- These are REAL bugs students encounter
- Safety checks are essential
- Understand what blocks vs. non-blocking
-->

---

# The Alvik Approach

Alvik library handles most timing for you:

```python
# Blocking: waits until motion complete
alvik.move(20, 'cm')  

# Non-blocking: returns immediately
alvik.drive(10, 0)  # You must manage timing

# Reading sensors: quick, non-blocking
distance = alvik.get_distance()  # ~few ms
```

For our labs: Simple polling loops are fine.
For complex robots: Learn asyncio and RTOS.

<!-- 
NOTES:
- Don't over-complicate for this course
- Polling works for maze challenge
- But know these concepts exist
-->

---

# ROS2 and Real-Time

ROS2 was designed with real-time in mind:

- **Callbacks**: Subscribe to sensor topics
- **Timers**: Publish at fixed rates
- **Executors**: Manage callback scheduling
- **DDS QoS**: Quality of Service guarantees

```python
# ROS2 timer example (not MicroPython)
self.timer = self.create_timer(0.1, self.control_callback)
```

<!-- 
NOTES:
- ROS2 is more sophisticated
- Built for complex multi-process robots
- Beyond our scope but good to know
-->

---

# Summary

| Approach | When to Use |
|----------|-------------|
| **Polling** | Simple robots, few tasks |
| **Timers** | Regular sensor reads |
| **Interrupts** | Safety-critical, immediate |
| **asyncio** | Multiple concurrent behaviors |
| **RTOS** | Complex systems, hard real-time |

For our labs: Polling is fine.
Key insight: **Timing matters. Plan for it.**

<!-- 
NOTES:
- Know these exist even if we don't use all of them
- Real robotics jobs require these skills
- Questions before we continue?
-->

---

# Questions?

- Timing concepts clear?
- When would you use interrupts vs. polling?
- Ready for Nav2 overview?

<!-- 
NOTES:
- Quick check for understanding
- Move on to Nav2 next
-->
