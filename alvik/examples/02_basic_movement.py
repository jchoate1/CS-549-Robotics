"""
02_basic_movement.py - Basic Motor Control

This program demonstrates basic movement commands:
- Moving forward/backward
- Turning left/right
- Using encoders for distance

Alvik Movement API:
- alvik.drive(linear_vel, angular_vel) - velocity control (cm/s, deg/s)
- alvik.move(distance, unit='cm') - move specific distance
- alvik.rotate(angle, unit='deg') - rotate specific angle
- alvik.stop() - stop all motors
"""

from arduino_alvik import ArduinoAlvik
import time

def main():
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Basic Movement Demo")
    print("Place Alvik on the floor with space to move")
    time.sleep(2)
    
    # Move forward 20 cm
    print("Moving forward 20 cm...")
    alvik.move(20, 'cm')
    time.sleep(0.5)
    
    # Turn right 90 degrees
    print("Turning right 90 degrees...")
    alvik.rotate(90, 'deg')
    time.sleep(0.5)
    
    # Move forward 20 cm
    print("Moving forward 20 cm...")
    alvik.move(20, 'cm')
    time.sleep(0.5)
    
    # Turn right 90 degrees
    print("Turning right 90 degrees...")
    alvik.rotate(90, 'deg')
    time.sleep(0.5)
    
    # Move forward 20 cm
    print("Moving forward 20 cm...")
    alvik.move(20, 'cm')
    time.sleep(0.5)
    
    # Turn right 90 degrees
    print("Turning right 90 degrees...")
    alvik.rotate(90, 'deg')
    time.sleep(0.5)
    
    # Move forward 20 cm (back to start)
    print("Moving forward 20 cm...")
    alvik.move(20, 'cm')
    time.sleep(0.5)
    
    # Turn right to face original direction
    print("Turning right 90 degrees...")
    alvik.rotate(90, 'deg')
    
    print("Square complete!")
    alvik.stop()

if __name__ == "__main__":
    main()
