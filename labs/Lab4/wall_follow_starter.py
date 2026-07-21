"""
Lab 4: Wall Following - Starter Code

Implement the right-hand rule for maze navigation.
Complete the TODO sections.

Right-hand rule:
1. If right is clear: turn right to find wall
2. If right has wall AND front clear: go forward
3. If front blocked: turn left
4. If stuck: turn around
"""

from arduino_alvik import ArduinoAlvik
import time

# Tunable parameters
WALL_THRESHOLD = 20     # cm - consider wall present if closer than this
FRONT_THRESHOLD = 15    # cm - consider front blocked if closer than this
SIDE_THRESHOLD = 25     # cm - ideal distance from wall
FOLLOW_SPEED = 8        # cm/s - forward speed
TURN_ANGLE = 45         # degrees - turn increment

class WallFollower:
    def __init__(self, alvik):
        self.alvik = alvik
        self.state = 'FIND_WALL'
    
    def read_sensors(self):
        """Read and return sensor values."""
        left, center_left, center, center_right, right = self.alvik.get_distance()
        return {
            'left': left,
            'center_left': center_left,
            'center': center,
            'center_right': center_right,
            'right': right,
            'left_avg': (left + center_left) / 2,
            'right_avg': (right + center_right) / 2
        }
    
    def has_wall_right(self, sensors):
        """Check if there's a wall on the right side."""
        # TODO: Return True if right_avg < WALL_THRESHOLD
        pass
    
    def has_wall_front(self, sensors):
        """Check if there's a wall in front."""
        # TODO: Return True if center < FRONT_THRESHOLD
        pass
    
    def has_wall_left(self, sensors):
        """Check if there's a wall on the left side."""
        # TODO: Return True if left_avg < WALL_THRESHOLD
        pass
    
    def update_leds(self, sensors):
        """Update LEDs to show sensor status."""
        # TODO: Set LED colors based on sensor readings
        # Green = clear, Red = wall detected
        pass
    
    def execute_state(self, sensors):
        """Execute behavior based on current state."""
        
        if self.state == 'FIND_WALL':
            # TODO: Looking for a wall on the right
            # If wall on right: transition to FOLLOW_WALL
            # If front blocked: turn left
            # Otherwise: turn right and move forward to find wall
            pass
            
        elif self.state == 'FOLLOW_WALL':
            # TODO: Following wall on right side
            # If no wall on right: transition to FIND_WALL (lost wall)
            # If front blocked: turn left
            # Otherwise: drive forward
            pass
            
        elif self.state == 'TURN_LEFT':
            # TODO: Turning left to avoid obstacle
            # Turn left by TURN_ANGLE
            # Transition back to FOLLOW_WALL
            pass
    
    def step(self):
        """Execute one step of the wall following behavior."""
        sensors = self.read_sensors()
        self.update_leds(sensors)
        self.execute_state(sensors)
        
        # Debug output
        print(f"State: {self.state:12s} | "
              f"R:{sensors['right_avg']:5.1f} C:{sensors['center']:5.1f} "
              f"L:{sensors['left_avg']:5.1f} cm")


def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Lab 4: Wall Following")
    print("Press OK to start, Ctrl+C to stop")
    print("-" * 50)
    
    while not alvik.get_touch_ok():
        time.sleep(0.1)
    
    print("Starting in 2 seconds...")
    time.sleep(2)
    
    follower = WallFollower(alvik)
    
    try:
        while True:
            follower.step()
            time.sleep(0.1)  # 10 Hz update rate
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        alvik.stop()
        print("Done.")

if __name__ == "__main__":
    main()
