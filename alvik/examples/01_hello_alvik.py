"""
01_hello_alvik.py - First Alvik Program

This program tests basic connectivity and LED control.
Run this first to verify your Alvik is properly connected.

Setup:
1. Connect Alvik to your computer via USB-C
2. Open this file in Arduino Lab for MicroPython or Thonny
3. Run the program

Expected behavior:
- LEDs will alternate red/blue 3 times
- "Alvik is ready!" will print to console
"""

from arduino_alvik import ArduinoAlvik
import time

def main():
    # Initialize the Alvik robot
    alvik = ArduinoAlvik()
    alvik.begin()
    
    print("Testing Alvik connection...")
    
    # Flash LEDs to confirm connection
    for i in range(3):
        # Left LED red, right LED blue
        alvik.left_led.set_color(1, 0, 0)
        alvik.right_led.set_color(0, 0, 1)
        time.sleep(0.5)
        
        # LEDs off
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        time.sleep(0.5)
    
    # Green LEDs to indicate success
    alvik.left_led.set_color(0, 1, 0)
    alvik.right_led.set_color(0, 1, 0)
    
    print("Alvik is ready!")
    print("Battery voltage:", alvik.get_battery_charge(), "%")
    
    time.sleep(2)
    alvik.stop()

if __name__ == "__main__":
    main()
