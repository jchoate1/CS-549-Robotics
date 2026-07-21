"""
04_obstacle_avoider.py - Simple Obstacle Avoidance

This is a reactive behavior: drive forward until an obstacle is detected,
then turn away from it.

This forms the foundation for more complex navigation behaviors
like wall-following and maze solving.

Behavior:
1. Drive forward
2. If obstacle detected within threshold, stop
3. Turn away from obstacle (toward the side with more space)
4. Resume driving forward

Sensor returns: (left, center_left, center, center_right, right) in cm
"""

from arduino_alvik import ArduinoAlvik
import time

# Configuration
OBSTACLE_THRESHOLD = 15  # cm - stop if obstacle closer than this
FORWARD_SPEED = 10  # cm/s

def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Obstacle Avoider Demo")
    print(f"Threshold: {OBSTACLE_THRESHOLD} cm")
    print("Press Ctrl+C to stop")
    print("-" * 40)
    
    try:
        while True:
            # Get distance readings (left, center_left, center, center_right, right) in cm
            left, center_left, center, center_right, right = alvik.get_distance()
            
            # Average the left and right sides to determine which has more space
            left_avg = (left + center_left) / 2
            right_avg = (right + center_right) / 2
            
            if center < OBSTACLE_THRESHOLD:
                # Obstacle detected - stop and turn
                alvik.stop()
                alvik.left_led.set_color(1, 0, 0)  # Red - obstacle
                alvik.right_led.set_color(1, 0, 0)
                
                print(f"Obstacle at {center:.1f} cm - turning...")
                
                # Turn toward the side with more space
                if left_avg > right_avg:
                    # More space on left, turn left (negative angle)
                    alvik.rotate(-45, 'deg')
                else:
                    # More space on right, turn right (positive angle)
                    alvik.rotate(45, 'deg')
                
                time.sleep(0.3)
            else:
                # Path is clear - drive forward
                alvik.left_led.set_color(0, 1, 0)  # Green - clear
                alvik.right_led.set_color(0, 1, 0)
                
                alvik.drive(FORWARD_SPEED, 0)
            
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        alvik.stop()

if __name__ == "__main__":
    main()
