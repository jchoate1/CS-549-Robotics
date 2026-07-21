"""
Lab 3: Sensor Reader - Starter Code

Complete the TODO sections to:
1. Read distance sensor values
2. Display LED feedback based on distance
3. Indicate obstacle direction with LEDs
"""

from arduino_alvik import ArduinoAlvik
import time

# Thresholds (in centimeters)
DANGER_THRESHOLD = 15   # Red - very close
CAUTION_THRESHOLD = 30  # Yellow - medium distance
# Above CAUTION_THRESHOLD = Green - clear

def get_distance_zone(distance):
    """
    Determine which zone a distance falls into.
    
    Returns: 'danger', 'caution', or 'clear'
    """
    # TODO: Implement threshold checking
    # Return 'danger' if distance < DANGER_THRESHOLD
    # Return 'caution' if distance < CAUTION_THRESHOLD
    # Return 'clear' otherwise
    
    pass  # Remove when implemented

def set_led_color(led, zone):
    """
    Set LED color based on zone.
    
    Args:
        led: alvik.left_led or alvik.right_led
        zone: 'danger', 'caution', or 'clear'
    """
    # TODO: Set LED color based on zone
    # danger = red (1, 0, 0)
    # caution = yellow (1, 1, 0)
    # clear = green (0, 1, 0)
    
    pass  # Remove when implemented

def determine_direction(left_avg, right_avg):
    """
    Determine which side the obstacle is on.
    
    Args:
        left_avg: Average of left and center_left readings
        right_avg: Average of right and center_right readings
    
    Returns: 'left', 'right', or 'center'
    """
    # TODO: Compare left and right averages
    # If left_avg is significantly less than right_avg, obstacle is on left
    # If right_avg is significantly less than left_avg, obstacle is on right
    # Otherwise, obstacle is centered
    # Use a threshold of ~5cm to avoid noise
    
    pass  # Remove when implemented

def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Lab 3: Distance Sensor Reader")
    print("Move your hand in front of the robot")
    print("Press Ctrl+C to stop")
    print("-" * 50)
    
    try:
        while True:
            # TODO: Read distance sensor
            # left, center_left, center, center_right, right = alvik.get_distance()
            
            # TODO: Calculate averages for direction detection
            # left_avg = (left + center_left) / 2
            # right_avg = (right + center_right) / 2
            
            # TODO: Determine zone based on center distance
            # zone = get_distance_zone(center)
            
            # TODO: Determine obstacle direction
            # direction = determine_direction(left_avg, right_avg)
            
            # TODO: Set LED colors
            # Basic version: both LEDs same color based on zone
            # Advanced version: indicate direction with different colors
            
            # TODO: Print sensor values and status
            # print(f"L:{left:5.1f} CL:{center_left:5.1f} C:{center:5.1f} ...")
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        alvik.stop()

if __name__ == "__main__":
    main()
