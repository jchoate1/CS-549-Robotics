"""
Lab 3: Reactive Stop - Starter Code

The robot drives forward and automatically stops when
an obstacle is detected.

Complete the TODO sections.
"""

from arduino_alvik import ArduinoAlvik
import time

STOP_THRESHOLD = 15  # cm - stop if obstacle closer than this
DRIVE_SPEED = 8      # cm/s - slow speed for safety

def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Lab 3: Reactive Stop")
    print(f"Robot will drive forward and stop at {STOP_THRESHOLD} cm")
    print("Press OK button to start, Ctrl+C to quit")
    print("-" * 50)
    
    # Wait for button press
    while not alvik.get_touch_ok():
        time.sleep(0.1)
    
    print("Starting in 2 seconds...")
    time.sleep(2)
    
    try:
        running = True
        
        while running:
            # TODO: Read distance sensor
            # Get the center distance reading
            
            # TODO: Check if obstacle is too close
            # If center < STOP_THRESHOLD:
            #     Stop the robot
            #     Set LEDs to red
            #     Print message
            #     Set running = False
            # Else:
            #     Drive forward
            #     Set LEDs to green
            
            time.sleep(0.05)  # 20 Hz update rate
        
        print("\nObstacle detected! Stopped.")
        
        # Wait a moment before cleanup
        time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nManual stop...")
    finally:
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        alvik.stop()
        print("Done.")

if __name__ == "__main__":
    main()
