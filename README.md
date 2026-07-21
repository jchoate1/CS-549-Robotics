# CS-549 Robotics: Weekend Intensive

A hands-on robotics course covering path planning algorithms, robot kinematics, sensor integration, and autonomous navigation.

## Course Overview

This course combines theoretical foundations with practical implementation using:
- **Arduino Alvik** robot with MicroPython for physical robot programming
- **ROS2/Gazebo** for simulation and industry-standard navigation concepts

## Repository Structure

```
CS-549-Robotics/
├── alvik/                    # Arduino Alvik robot code
│   └── examples/             # Working examples to learn from
├── labs/                     # Lab assignments
│   ├── Lab1/                 # A* path planning (Python)
│   ├── Lab2/                 # Motor control and odometry (Alvik)
│   ├── Lab3/                 # Range sensor interfacing (Alvik)
│   ├── Lab4/                 # Wall-following behavior (Alvik)
│   └── Lab5/                 # Final maze navigation (Alvik)
├── ros2_simulation/          # Gazebo maze worlds and Nav2 config
└── docs/                     # Additional documentation
```

## Prerequisites

### Hardware
- Arduino Alvik robot kit
- USB-C cable (included with Alvik)
- Laptop with USB-C port (or adapter)

### Software
- Python 3.9 or later
- **Thonny IDE** (recommended) or Arduino Lab for MicroPython
- For ROS2 labs: ROS2 Humble + Gazebo (optional VM provided)

## Quick Start: Alvik Setup

### 1. Install Thonny IDE (Recommended)

We recommend **Thonny** over Arduino Lab for MicroPython for this course:

| | Thonny | Arduino Lab for MicroPython |
|---|--------|----------------------------|
| Stability | Mature, stable | Experimental (beta) |
| Interface | Simple, clean | More complex |
| Documentation | Extensive | Limited |
| Error messages | Clear, helpful | Basic |
| Community support | Large | Small |

**Install Thonny:**

1. Download from: https://thonny.org/
2. Install and launch Thonny
3. Go to **Tools → Options → Interpreter**
4. Select **MicroPython (ESP32)** from the dropdown
5. Select your Alvik's port (e.g., `/dev/cu.usbmodem*` on Mac, `COM*` on Windows)
6. Click **OK**

You should see the MicroPython REPL prompt (`>>>`) at the bottom of the window.

**Alternative: Arduino Lab for MicroPython**

If you prefer the official Arduino tool:
- Download from: https://labs.arduino.cc/en/labs/micropython
- Note: This is still experimental software and may have rough edges

### 2. Update Alvik Firmware (if needed)

Visit: https://alvikupdate.arduino.cc/

Connect your Alvik via USB-C and follow the on-screen instructions.

### 3. Install Alvik MicroPython Library

**Option A: Using mip (if Alvik has WiFi)**
```python
import mip
mip.install('github:arduino/arduino-alvik-mpy')
```

**Option B: Using mpremote (recommended)**
```bash
pip install mpremote
# Clone the library
git clone https://github.com/arduino/arduino-alvik-mpy.git
cd arduino-alvik-mpy
# Install to connected Alvik
./install.sh -p /dev/ttyUSB0  # Linux
./install.sh -p /dev/cu.usbmodem*  # macOS
install.bat -p COM3  # Windows
```

### 4. Test Your Setup

Connect Alvik via USB-C, then run this test program:

```python
from arduino_alvik import ArduinoAlvik
import time

alvik = ArduinoAlvik()
alvik.begin()

# Flash LEDs to confirm connection
for i in range(3):
    alvik.left_led.set_color(1, 0, 0)  # Red
    alvik.right_led.set_color(0, 0, 1)  # Blue
    time.sleep(0.5)
    alvik.left_led.set_color(0, 0, 0)
    alvik.right_led.set_color(0, 0, 0)
    time.sleep(0.5)

print("Alvik is ready!")
alvik.stop()
```

## Lab Assignments

| Lab | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | Path Planning | Configuration space, A* algorithm |
| 2 | Drive Square | Motor control, encoders, dead reckoning |
| 3 | Sensors | ToF distance sensor, obstacle detection |
| 4 | Wall Following | Reactive behaviors, state machines |
| 5 | Maze Challenge | Integration of all skills |

## Useful Links

- [Arduino Alvik Documentation](https://docs.arduino.cc/hardware/alvik/)
- [Alvik Getting Started Guide](https://docs.arduino.cc/tutorials/alvik/getting-started/)
- [Alvik MicroPython Library](https://github.com/arduino/arduino-alvik-mpy)
- [ROS2 Humble Documentation](https://docs.ros.org/en/humble/)
- [Nav2 Documentation](https://navigation.ros.org/)

## License

MIT License - See [LICENSE](LICENSE) for details.
