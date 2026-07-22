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
├── slides/                   # Lecture slides (Marp markdown format)
│   └── images/               # Images used in slides
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

## Lecture Slides

Slides are written in Markdown using [Marp](https://marp.app/) format and located in the `slides/` directory.

| Slide Deck | Topic |
|------------|-------|
| `01-course-overview.md` | Course overview, robotics landscape |
| `02-configuration-space.md` | Configuration space, obstacles |
| `03-path-planning.md` | BFS, Dijkstra, A*, wavefront |
| `04-robot-kinematics.md` | Differential drive, odometry |
| `05-motor-control.md` | Motors, encoders, PID, feedback control |
| `06-intro-ros2.md` | ROS2 introduction |
| `07-sensors-overview.md` | Sensors, I2C/SPI protocols |
| `07b-realtime-concepts.md` | Timers, asyncio, interrupts |
| `08-maze-algorithms.md` | Wall follower, Pledge, flood fill |
| `09-ros2-nav2.md` | Nav2, costmaps, SLAM |
| `10-trajectories.md` | Splines, smooth motion |
| `11-advanced-topics.md` | Vision/ML, safety, next steps |

**Presenting slides:**
- Install the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension
- Open any `.md` slide file and click the Marp preview icon
- Or use Marp CLI: `marp --preview slides/01-course-overview.md`

**Exporting to PDF/PowerPoint:**
```bash
marp slides/01-course-overview.md -o slides/01-course-overview.pdf
marp slides/01-course-overview.md -o slides/01-course-overview.pptx
```

## Useful Links

- [Arduino Alvik Documentation](https://docs.arduino.cc/hardware/alvik/)
- [Alvik Getting Started Guide](https://docs.arduino.cc/tutorials/alvik/getting-started/)
- [Alvik MicroPython Library](https://github.com/arduino/arduino-alvik-mpy)
- [ROS2 Humble Documentation](https://docs.ros.org/en/humble/)
- [Nav2 Documentation](https://navigation.ros.org/)
- [Marp (Markdown Presentations)](https://marp.app/)

## License

MIT License - See [LICENSE](LICENSE) for details.
