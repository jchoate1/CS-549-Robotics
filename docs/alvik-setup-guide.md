# Arduino Alvik Setup Guide

This guide walks you through setting up your Arduino Alvik robot for the CS-549 course.

## What's in the Box

- Arduino Alvik robot
- USB-C cable
- Quick start guide
- Optional: expansion modules

## Hardware Overview

The Alvik is powered by an **Arduino Nano ESP32** and includes:

| Component | Description |
|-----------|-------------|
| Motors | 2x DC motors with encoders |
| ToF Sensor | Time-of-Flight distance sensor (front) |
| Line Sensors | IR sensors for line following (bottom) |
| IMU | Accelerometer + Gyroscope |
| Touch Buttons | Capacitive touch sensors |
| RGB LEDs | 2x programmable LEDs |
| Battery | Rechargeable LiPo |

**Dimensions:** ~9.6 cm x 9.6 cm (compact square form factor)

## Step 1: Charge the Battery

Before first use, charge Alvik via USB-C for at least 1-2 hours. The power LED indicates charging status.

## Step 2: Install Development Environment

You have two options for programming the Alvik. **We recommend Thonny** for this course.

### Why We Recommend Thonny

| Feature | Thonny | Arduino Lab for MicroPython |
|---------|--------|----------------------------|
| **Stability** | Mature, battle-tested | Experimental (still in beta) |
| **Interface** | Simple, clean, beginner-friendly | More complex |
| **REPL** | Excellent interactive console | Basic |
| **Error messages** | Clear and helpful | Sometimes cryptic |
| **File management** | Built-in, easy to use | Functional but clunkier |
| **Documentation** | Extensive tutorials available | Limited |
| **Community** | Large, active support | Smaller community |

Thonny has been used in education for years and is specifically designed for learning Python and MicroPython. When something goes wrong (and it will), you'll find more help available online.

### Option A: Thonny IDE (Recommended)

1. **Download Thonny** from: https://thonny.org/
   - Choose the installer for your operating system
   - On Mac: Download the `.dmg` file and drag to Applications
   - On Windows: Download the `.exe` installer and run it

2. **Launch Thonny** after installation

3. **Configure the interpreter:**
   - Go to **Tools → Options → Interpreter**
   - Select **MicroPython (ESP32)** from the dropdown
   - In the "Port" dropdown, select your Alvik's port:
     - Mac: Usually `/dev/cu.usbmodem*` or `/dev/cu.usbserial*`
     - Windows: Usually `COM3`, `COM4`, etc.
     - Linux: Usually `/dev/ttyUSB0` or `/dev/ttyACM0`
   - Click **OK**

4. **Verify connection:**
   - You should see the MicroPython REPL prompt (`>>>`) at the bottom
   - Type `print("Hello!")` and press Enter
   - If you see `Hello!` printed back, you're connected!

### Option B: Arduino Lab for MicroPython (Alternative)

If you prefer the official Arduino tool, you can use it, but be aware it's still experimental.

1. Download from: https://labs.arduino.cc/en/labs/micropython
2. Install and launch
3. Connect Alvik via USB-C
4. Click the connection icon and select the correct port
5. You should see the device files appear in the file browser

## Step 3: Update Firmware (If Needed)

If your Alvik has old firmware or behaves unexpectedly:

1. Go to: https://alvikupdate.arduino.cc/
2. Connect Alvik via USB-C
3. Follow the on-screen instructions

## Step 4: Install the Alvik MicroPython Library

The Alvik library provides high-level functions for controlling the robot.

### Method 1: Using mip (if Alvik has WiFi configured)

```python
import mip
mip.install('github:arduino/arduino-alvik-mpy')
```

### Method 2: Using mpremote (Recommended)

First, install mpremote on your computer:

```bash
pip install mpremote
```

Then clone and install the library:

```bash
git clone https://github.com/arduino/arduino-alvik-mpy.git
cd arduino-alvik-mpy

# On macOS/Linux:
./install.sh -p /dev/cu.usbmodem*

# On Windows:
install.bat -p COM3
```

## Step 5: Test Your Setup

Create a new file called `test_alvik.py` and run it:

```python
from arduino_alvik import ArduinoAlvik
import time

alvik = ArduinoAlvik()
alvik.begin()

# Flash LEDs
for i in range(3):
    alvik.left_led.set_color(0, 1, 0)  # Green
    alvik.right_led.set_color(0, 1, 0)
    time.sleep(0.3)
    alvik.left_led.set_color(0, 0, 0)
    alvik.right_led.set_color(0, 0, 0)
    time.sleep(0.3)

print("Battery:", alvik.get_battery_charge(), "%")
print("Alvik is ready!")
alvik.stop()
```

If the LEDs flash green and you see the battery percentage, you're all set!

## Troubleshooting

### "Device not found" / No port available in Thonny

1. **Check the USB cable** - Some USB-C cables are charge-only and don't support data. Try a different cable.
2. **Try a different USB port** - Some ports may have issues.
3. **Check if the device is recognized by your OS:**
   - Mac: Open **System Information → USB** and look for the device
   - Windows: Open **Device Manager → Ports (COM & LPT)** and look for a COM port
   - Linux: Run `ls /dev/ttyUSB* /dev/ttyACM*` in terminal
4. **In Thonny:** Go to **Tools → Options → Interpreter** and click the port dropdown to refresh the list.
5. **Restart Thonny** after connecting the device.

### "Import error: arduino_alvik not found"

The Alvik library isn't installed on the robot. This shouldn't happen with a new Alvik, but if it does:

1. Follow Step 4 above to install the library
2. Or use the firmware update tool at https://alvikupdate.arduino.cc/

### Robot doesn't move

1. **Check battery:** In the REPL, run:
   ```python
   from arduino_alvik import ArduinoAlvik
   alvik = ArduinoAlvik()
   alvik.begin()
   print(alvik.get_battery_charge())
   ```
   If the battery is low (< 20%), charge the robot.

2. **Check initialization:** Make sure you called `alvik.begin()` before any movement commands.

3. **Check physical obstacles:** Make sure wheels aren't blocked and the robot isn't stuck.

### Thonny shows "Backend terminated" or "Device is busy"

1. **Press the Stop/Restart button** (red stop sign) in Thonny
2. **Disconnect and reconnect** the USB cable
3. **Close and reopen Thonny**
4. If the robot is running a program in a loop, you may need to press the **reset button** on the Alvik

### Erratic behavior after uploading Arduino IDE code

If you previously uploaded C++ code via Arduino IDE, MicroPython may have been erased. You need to reflash it:

1. Go to: https://labs.arduino.cc/en/labs/micropython-installer
2. Connect the Alvik and follow the instructions to flash MicroPython
3. Reinstall the Alvik library (Step 4 above)

## Programming Model

### main.py

When Alvik boots, it runs `main.py` automatically. To run your own code on startup:

1. Create your program (e.g., `my_program.py`)
2. Edit `main.py` to import and run your code:

```python
# main.py
from my_program import main
main()
```

### Running Code Interactively

In Thonny or Arduino Lab, you can:
- Run the current file directly (F5 or Run button)
- Use the REPL (Read-Eval-Print Loop) for testing commands

## Next Steps

1. Run the examples in `alvik/examples/` in order
2. Move on to Lab 2: Drive Square
3. Experiment with combining movements and sensors

## Useful Resources

- [Alvik Documentation](https://docs.arduino.cc/hardware/alvik/)
- [Alvik User Manual](https://docs.arduino.cc/tutorials/alvik/user-manual/)
- [MicroPython Library GitHub](https://github.com/arduino/arduino-alvik-mpy)
- [Arduino Forum - Alvik Section](https://forum.arduino.cc/c/hardware/alvik/)
