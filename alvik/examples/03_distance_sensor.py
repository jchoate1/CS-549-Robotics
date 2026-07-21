"""
03_distance_sensor.py - Reading the ToF Distance Sensor

The Alvik has a Time-of-Flight (ToF) distance sensor on the front.
This program demonstrates how to read distance values.

Sensor API:
- alvik.get_distance() returns a tuple of 5 values in CENTIMETERS:
  (left, center_left, center, center_right, right)

These represent different angular zones of the sensor's field of view,
useful for determining which direction an obstacle is in.
"""

from arduino_alvik import ArduinoAlvik
import time

def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Distance Sensor Demo")
    print("Move your hand in front of the robot to see distance readings")
    print("Press Ctrl+C to stop")
    print("-" * 40)
    
    try:
        while True:
            # Get distance readings - returns tuple of 5 values in cm:
            # (left, center_left, center, center_right, right)
            left, center_left, center, center_right, right = alvik.get_distance()
            
            print(f"L:{left:5.1f}  CL:{center_left:5.1f}  C:{center:5.1f}  CR:{center_right:5.1f}  R:{right:5.1f} cm")
            
            # Visual indicator using LEDs based on center distance
            if center < 10:  # Very close (< 10 cm)
                alvik.left_led.set_color(1, 0, 0)  # Red
                alvik.right_led.set_color(1, 0, 0)
            elif center < 30:  # Medium distance (< 30 cm)
                alvik.left_led.set_color(1, 1, 0)  # Yellow
                alvik.right_led.set_color(1, 1, 0)
            else:  # Far
                alvik.left_led.set_color(0, 1, 0)  # Green
                alvik.right_led.set_color(0, 1, 0)
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        alvik.stop()

if __name__ == "__main__":
    main()
