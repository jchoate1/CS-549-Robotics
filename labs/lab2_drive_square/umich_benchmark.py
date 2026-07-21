"""
Lab 2: University of Michigan Benchmark Test

This program runs the UMich dead reckoning accuracy test:
1. Drive a 1m x 1m square
2. Measure position error
3. Repeat in both directions (CW and CCW)

Reference: Borenstein & Feng, "Measurement and Correction of 
Systematic Odometry Errors in Mobile Robots"
http://www-personal.umich.edu/~johannb/Papers/pos96rep.pdf
"""

from arduino_alvik import ArduinoAlvik
import time

# Test configuration
SQUARE_SIZE = 100  # cm (1 meter)
NUM_TRIALS = 3     # Number of trials per direction
PAUSE_TIME = 0.5   # Pause between movements

def drive_square_cw(alvik):
    """Drive clockwise (right turns)."""
    for i in range(4):
        alvik.move(SQUARE_SIZE, 'cm')
        time.sleep(PAUSE_TIME)
        alvik.rotate(90, 'deg')  # Turn right
        time.sleep(PAUSE_TIME)

def drive_square_ccw(alvik):
    """Drive counter-clockwise (left turns)."""
    for i in range(4):
        alvik.move(SQUARE_SIZE, 'cm')
        time.sleep(PAUSE_TIME)
        alvik.rotate(-90, 'deg')  # Turn left
        time.sleep(PAUSE_TIME)

def run_trial(alvik, direction='cw'):
    """Run a single trial and return the error."""
    alvik.reset_pose()
    
    if direction == 'cw':
        drive_square_cw(alvik)
    else:
        drive_square_ccw(alvik)
    
    x, y, theta = alvik.get_pose()
    distance_error = (x**2 + y**2)**0.5
    
    return x, y, theta, distance_error

def run_benchmark(alvik):
    """Run the complete benchmark test."""
    results = {
        'cw': [],
        'ccw': []
    }
    
    # Clockwise trials
    print("\n=== CLOCKWISE TRIALS ===")
    for i in range(NUM_TRIALS):
        print(f"\nTrial CW-{i+1}: Press OK when ready...")
        while not alvik.get_touch_ok():
            time.sleep(0.1)
        
        print("Starting in 2 seconds...")
        time.sleep(2)
        
        x, y, theta, dist = run_trial(alvik, 'cw')
        results['cw'].append((x, y, theta, dist))
        
        print(f"Result: X={x:.1f}cm, Y={y:.1f}cm, θ={theta:.1f}°, Error={dist:.1f}cm")
        
        # Indicate completion
        alvik.left_led.set_color(0, 1, 0)
        alvik.right_led.set_color(0, 1, 0)
        time.sleep(1)
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
    
    # Counter-clockwise trials
    print("\n=== COUNTER-CLOCKWISE TRIALS ===")
    for i in range(NUM_TRIALS):
        print(f"\nTrial CCW-{i+1}: Press OK when ready...")
        while not alvik.get_touch_ok():
            time.sleep(0.1)
        
        print("Starting in 2 seconds...")
        time.sleep(2)
        
        x, y, theta, dist = run_trial(alvik, 'ccw')
        results['ccw'].append((x, y, theta, dist))
        
        print(f"Result: X={x:.1f}cm, Y={y:.1f}cm, θ={theta:.1f}°, Error={dist:.1f}cm")
        
        alvik.left_led.set_color(0, 0, 1)
        alvik.right_led.set_color(0, 0, 1)
        time.sleep(1)
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
    
    return results

def print_summary(results):
    """Print a summary of the benchmark results."""
    print("\n" + "=" * 50)
    print("BENCHMARK RESULTS SUMMARY")
    print("=" * 50)
    
    for direction in ['cw', 'ccw']:
        trials = results[direction]
        print(f"\n{direction.upper()} ({len(trials)} trials):")
        print("-" * 40)
        print("Trial |   X (cm) |   Y (cm) | θ (deg) | Error (cm)")
        print("-" * 40)
        
        total_x, total_y, total_theta, total_dist = 0, 0, 0, 0
        
        for i, (x, y, theta, dist) in enumerate(trials):
            print(f"  {i+1}   | {x:8.1f} | {y:8.1f} | {theta:7.1f} | {dist:8.1f}")
            total_x += x
            total_y += y
            total_theta += theta
            total_dist += dist
        
        n = len(trials)
        print("-" * 40)
        print(f" Avg  | {total_x/n:8.1f} | {total_y/n:8.1f} | {total_theta/n:7.1f} | {total_dist/n:8.1f}")
    
    print("\n" + "=" * 50)
    print("Copy these results to your lab report!")
    print("=" * 50)

def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("=" * 50)
    print("UNIVERSITY OF MICHIGAN BENCHMARK TEST")
    print("=" * 50)
    print(f"Square size: {SQUARE_SIZE} cm")
    print(f"Trials per direction: {NUM_TRIALS}")
    print("\nThis test measures dead reckoning accuracy.")
    print("Mark your starting position with tape!")
    print("\nPress OK to begin...")
    
    while not alvik.get_touch_ok():
        time.sleep(0.1)
    
    results = run_benchmark(alvik)
    print_summary(results)
    
    alvik.stop()

if __name__ == "__main__":
    main()
