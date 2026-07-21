"""
Lab 2: Drive Square - Starter Code

Your task: Make the Alvik drive in a 30cm x 30cm square and return to start.

Instructions:
1. Fill in the TODO sections below
2. Test with a small square first (10cm)
3. Once working, change to 30cm
4. Measure your accuracy

Useful functions:
- alvik.move(distance, 'cm')  - Move forward/backward
- alvik.rotate(angle, 'deg')  - Turn in place
- alvik.stop()                - Stop all motors
"""

from arduino_alvik import ArduinoAlvik
import time

# Configuration - change these to tune your square
SIDE_LENGTH = 30  # cm - length of each side of the square
TURN_ANGLE = 90   # degrees - how much to turn at each corner
PAUSE_TIME = 0.3  # seconds - pause between movements

def indicate_progress(alvik, step):
    """Flash LEDs to indicate which step we're on."""
    # TODO: Implement LED feedback
    # Suggestion: Different colors for each side of the square
    pass

def drive_square(alvik):
    """
    Drive the Alvik in a square pattern.
    
    The square should be SIDE_LENGTH cm on each side.
    After completing the square, the robot should be
    back at the starting position facing the original direction.
    """
    print(f"Driving a {SIDE_LENGTH}cm square...")
    
    # TODO: Implement the square driving logic
    # 
    # Hint: A square has 4 sides and 4 turns
    # 
    # For each side:
    #   1. Indicate progress (optional)
    #   2. Move forward SIDE_LENGTH cm
    #   3. Pause briefly
    #   4. Turn TURN_ANGLE degrees
    #   5. Pause briefly
    #
    # Your code here:
    
    pass  # Remove this line when you add your code

def main():
    # Initialize robot
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Lab 2: Drive Square")
    print(f"Side length: {SIDE_LENGTH} cm")
    print("Place robot on floor, then press OK to start...")
    
    # Wait for button press
    while not alvik.get_touch_ok():
        time.sleep(0.1)
    
    print("Starting in 2 seconds...")
    time.sleep(2)
    
    # Reset pose tracking
    alvik.reset_pose()
    
    # Drive the square
    drive_square(alvik)
    
    # Get final pose
    x, y, theta = alvik.get_pose()
    
    print("\n--- Results ---")
    print(f"Final position: ({x:.1f}, {y:.1f}) cm")
    print(f"Final heading: {theta:.1f} degrees")
    print(f"Distance from start: {(x**2 + y**2)**0.5:.1f} cm")
    
    # Indicate completion
    alvik.left_led.set_color(0, 1, 0)
    alvik.right_led.set_color(0, 1, 0)
    time.sleep(2)
    
    alvik.stop()
    print("Done!")

if __name__ == "__main__":
    main()
