# Alvik MicroPython API Quick Reference

## Initialization

```python
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()
alvik.begin()  # Always call this first!
```

## Movement Commands

### Basic Movement

```python
# Move a specific distance
alvik.move(distance, unit='cm')  # or 'mm', 'in'

# Rotate a specific angle  
alvik.rotate(angle, unit='deg')  # or 'rad'

# Velocity control (continuous)
alvik.drive(linear_velocity, angular_velocity)
# linear_velocity: cm/s (positive = forward)
# angular_velocity: deg/s (positive = counter-clockwise)

# Stop all motors
alvik.stop()
```

### Motor Control

```python
# Set individual wheel speeds (RPM or percentage)
alvik.set_wheels_speed(left_speed, right_speed)

# Get encoder counts
left, right = alvik.get_wheels_position()
```

### Positioning

```python
# Get current pose estimate (x, y, theta)
x, y, theta = alvik.get_pose()

# Reset pose to origin
alvik.reset_pose()
```

## Sensors

### Distance Sensor (ToF)

```python
# Get distance readings - returns tuple of 5 values in CENTIMETERS
left, center_left, center, center_right, right = alvik.get_distance()

# Example values when hand is ~40cm away:
# (41.6, 37.5, 41.2, 45.0, 37.1)

# The 5 zones cover the sensor's field of view from left to right,
# useful for determining obstacle direction
```

### Line Sensors

```python
# Get line sensor readings
sensors = alvik.get_line_sensors()
# Returns tuple: (left, center, right)
# Low values = dark (line), High values = light (background)
```

### IMU (Inertial Measurement Unit)

```python
# Get accelerometer data (g)
ax, ay, az = alvik.get_accelerations()

# Get gyroscope data (deg/s)
gx, gy, gz = alvik.get_gyros()

# Get orientation (degrees)
roll, pitch, yaw = alvik.get_orientation()
```

### Touch Buttons

```python
# Check if touch buttons are pressed
if alvik.get_touch_any():
    print("Button pressed!")

# Individual buttons
ok = alvik.get_touch_ok()
cancel = alvik.get_touch_cancel()
center = alvik.get_touch_center()
up = alvik.get_touch_up()
down = alvik.get_touch_down()
left = alvik.get_touch_left()
right = alvik.get_touch_right()
```

## LEDs

```python
# Set LED color (RGB, values 0-1 or 0-255)
alvik.left_led.set_color(red, green, blue)
alvik.right_led.set_color(red, green, blue)

# Turn off LED
alvik.left_led.set_color(0, 0, 0)
```

### Common Colors

```python
# Red
alvik.left_led.set_color(1, 0, 0)

# Green
alvik.left_led.set_color(0, 1, 0)

# Blue
alvik.left_led.set_color(0, 0, 1)

# Yellow
alvik.left_led.set_color(1, 1, 0)

# Cyan
alvik.left_led.set_color(0, 1, 1)

# Magenta
alvik.left_led.set_color(1, 0, 1)

# White
alvik.left_led.set_color(1, 1, 1)
```

## Battery

```python
# Get battery charge percentage
charge = alvik.get_battery_charge()
print(f"Battery: {charge}%")
```

## Typical Program Structure

```python
from arduino_alvik import ArduinoAlvik
import time

def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    try:
        # Your code here
        while True:
            # Main loop
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        # Cleanup
        alvik.stop()

if __name__ == "__main__":
    main()
```

## Common Patterns

### Wait for Button Press

```python
print("Press OK to start...")
while not alvik.get_touch_ok():
    time.sleep(0.1)
print("Starting!")
```

### Simple Obstacle Detection

```python
THRESHOLD = 15  # cm

left, center_left, center, center_right, right = alvik.get_distance()

if center < THRESHOLD:
    print(f"Obstacle detected at {center:.1f} cm!")
    alvik.stop()
```

### Proportional Line Following

```python
BASE_SPEED = 8
GAIN = 0.05

left, center, right = alvik.get_line_sensors()
error = right - left
turn = error * GAIN
alvik.drive(BASE_SPEED, turn)
```

## Units Reference

| Parameter | Default Unit | Alternatives |
|-----------|--------------|--------------|
| Distance | cm | mm, in |
| Angle | degrees | radians |
| Linear velocity | cm/s | - |
| Angular velocity | deg/s | - |
| Time | seconds | milliseconds |
