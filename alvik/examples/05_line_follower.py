"""
05_line_follower.py - Line Following Using IR Sensors

The Alvik has IR line sensors on the bottom for detecting
black lines on a white surface.

Line Sensor API:
- alvik.get_line_sensors() - returns tuple of sensor readings
- Values are typically 0-1000+ where:
  - Low values = dark surface (line)
  - High values = light surface (background)

This is a proportional controller that adjusts steering
based on the line position under the sensors.
"""

from arduino_alvik import ArduinoAlvik
import time

# Configuration
BASE_SPEED = 8  # cm/s - base forward speed
TURN_GAIN = 0.05  # How aggressively to turn
LINE_THRESHOLD = 500  # Below this = on the line

def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Line Follower Demo")
    print("Place Alvik on a black line on white background")
    print("Press Ctrl+C to stop")
    print("-" * 40)
    
    try:
        while True:
            # Get line sensor readings
            # Returns (left, center, right) or similar tuple
            line_sensors = alvik.get_line_sensors()
            
            if len(line_sensors) >= 3:
                left, center, right = line_sensors[0], line_sensors[1], line_sensors[2]
            else:
                print("Unexpected sensor format:", line_sensors)
                continue
            
            # Calculate error - positive means line is to the right
            # Weighted average of sensor positions
            error = (right - left)
            
            # Proportional control for turning
            turn_rate = error * TURN_GAIN
            
            # Check if we see the line at all
            sees_line = left < LINE_THRESHOLD or center < LINE_THRESHOLD or right < LINE_THRESHOLD
            
            if sees_line:
                # On the line - drive with correction
                alvik.left_led.set_color(0, 1, 0)  # Green
                alvik.right_led.set_color(0, 1, 0)
                alvik.drive(BASE_SPEED, turn_rate)
            else:
                # Lost the line - stop or search
                alvik.left_led.set_color(1, 1, 0)  # Yellow
                alvik.right_led.set_color(1, 1, 0)
                # Slowly spin to find line
                alvik.drive(0, 30)
            
            # Debug output
            print(f"L:{left:4.0f} C:{center:4.0f} R:{right:4.0f} | Error:{error:6.1f} | Turn:{turn_rate:5.1f}")
            
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        alvik.stop()

if __name__ == "__main__":
    main()
