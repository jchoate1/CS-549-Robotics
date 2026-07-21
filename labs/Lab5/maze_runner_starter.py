"""
Lab 5: Maze Runner - Starter Code

This is your starting point for the maze challenge.
Build on your Lab 4 wall-following code and add:
- Start/goal detection
- Timing
- Enhanced behaviors

Press OK to start, the robot will navigate the maze autonomously.
"""

from arduino_alvik import ArduinoAlvik
import time

# Configuration
WALL_THRESHOLD = 20     # cm
FRONT_THRESHOLD = 15    # cm
FOLLOW_SPEED = 10       # cm/s - increase for faster runs
TURN_ANGLE = 45         # degrees

class MazeRunner:
    def __init__(self, alvik):
        self.alvik = alvik
        self.state = 'RUNNING'
        self.start_time = None
        self.step_count = 0
        
    def read_sensors(self):
        """Read all sensor values."""
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
        return sensors['right_avg'] < WALL_THRESHOLD
    
    def has_wall_front(self, sensors):
        return sensors['center'] < FRONT_THRESHOLD
    
    def has_wall_left(self, sensors):
        return sensors['left_avg'] < WALL_THRESHOLD
    
    def detect_goal(self, sensors):
        """
        Detect if we've reached the goal.
        
        TODO: Implement goal detection
        Options:
        - All sides clear (exited maze)
        - Specific distance pattern
        - Color detection (if goal is marked)
        - Time/distance traveled
        
        For now, return False (manual stop with Ctrl+C)
        """
        return False
    
    def navigate(self, sensors):
        """
        Main navigation logic - right-hand wall following.
        
        TODO: Copy and enhance your Lab 4 wall-following code
        """
        # TODO: Implement your navigation logic
        # 
        # Basic right-hand rule:
        # 1. If right clear: turn right, find wall
        # 2. If right wall AND front clear: go forward
        # 3. If front blocked: turn left
        
        pass  # Remove when implemented
    
    def update_leds(self, sensors):
        """Update LEDs to show status."""
        if self.has_wall_front(sensors):
            # Danger ahead
            self.alvik.left_led.set_color(1, 0, 0)
            self.alvik.right_led.set_color(1, 0, 0)
        elif self.has_wall_right(sensors):
            # Following wall
            self.alvik.left_led.set_color(0, 1, 0)
            self.alvik.right_led.set_color(1, 1, 0)
        else:
            # Searching
            self.alvik.left_led.set_color(0, 0, 1)
            self.alvik.right_led.set_color(0, 0, 1)
    
    def step(self):
        """Execute one navigation step."""
        self.step_count += 1
        sensors = self.read_sensors()
        
        # Check for goal
        if self.detect_goal(sensors):
            self.state = 'FINISHED'
            self.alvik.stop()
            return
        
        # Update LEDs
        self.update_leds(sensors)
        
        # Navigate
        self.navigate(sensors)
        
        # Debug output (every 10 steps to reduce spam)
        if self.step_count % 10 == 0:
            elapsed = time.time() - self.start_time
            print(f"[{elapsed:5.1f}s] R:{sensors['right_avg']:4.0f} "
                  f"C:{sensors['center']:4.0f} L:{sensors['left_avg']:4.0f}")
    
    def run(self):
        """Main run loop."""
        print("Maze Runner starting!")
        self.start_time = time.time()
        
        try:
            while self.state != 'FINISHED':
                self.step()
                time.sleep(0.05)  # 20 Hz
                
        except KeyboardInterrupt:
            print("\nManual stop")
        
        # Calculate final time
        elapsed = time.time() - self.start_time
        self.alvik.stop()
        
        # Victory indication
        for _ in range(3):
            self.alvik.left_led.set_color(0, 1, 0)
            self.alvik.right_led.set_color(0, 1, 0)
            time.sleep(0.3)
            self.alvik.left_led.set_color(0, 0, 0)
            self.alvik.right_led.set_color(0, 0, 0)
            time.sleep(0.3)
        
        print(f"\n{'='*40}")
        print(f"Maze completed in {elapsed:.1f} seconds!")
        print(f"Steps taken: {self.step_count}")
        print(f"{'='*40}")
        
        return elapsed


def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("=" * 40)
    print("LAB 5: MAZE CHALLENGE")
    print("=" * 40)
    print("\nPress OK to start the maze run")
    print("Press Ctrl+C to stop at any time")
    print()
    
    # Wait for start
    while not alvik.get_touch_ok():
        time.sleep(0.1)
    
    print("Starting in 3 seconds...")
    for i in range(3, 0, -1):
        print(f"  {i}...")
        alvik.left_led.set_color(1, 1, 0)
        alvik.right_led.set_color(1, 1, 0)
        time.sleep(0.5)
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        time.sleep(0.5)
    
    print("GO!")
    
    # Run the maze
    runner = MazeRunner(alvik)
    elapsed = runner.run()
    
    # Cleanup
    alvik.left_led.set_color(0, 0, 0)
    alvik.right_led.set_color(0, 0, 0)
    alvik.stop()
    
    print("\nDone! Press OK to run again or Ctrl+C to quit")
    
    # Allow reruns
    try:
        while True:
            if alvik.get_touch_ok():
                time.sleep(0.5)  # Debounce
                runner = MazeRunner(alvik)
                runner.run()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    
    print("Goodbye!")

if __name__ == "__main__":
    main()
