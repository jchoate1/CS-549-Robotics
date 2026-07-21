# ROS2 Gazebo Simulation

This directory contains a Gazebo simulation environment for demonstrating ROS2 navigation concepts.

## Purpose

The simulation is used for:
1. Demonstrating Nav2 navigation stack
2. Visualizing path planning in action
3. Showing costmaps and planners
4. Students who want to explore ROS2 further

**Note**: The physical Alvik labs use MicroPython directly. This simulation uses a TurtleBot3 model as a stand-in for demonstrating ROS2 concepts.

## Prerequisites

### Install ROS2 Humble

**Ubuntu 22.04:**
```bash
# Add ROS2 repository
sudo apt update && sudo apt install -y curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS2 Humble
sudo apt update
sudo apt install -y ros-humble-desktop

# Source ROS2
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

**macOS (via Docker):**
```bash
# Pull ROS2 Docker image
docker pull osrf/ros:humble-desktop

# Run with GUI support
docker run -it --rm \
  -e DISPLAY=host.docker.internal:0 \
  -v $(pwd):/workspace \
  osrf/ros:humble-desktop
```

### Install TurtleBot3 Packages

```bash
sudo apt install -y ros-humble-turtlebot3*
sudo apt install -y ros-humble-navigation2 ros-humble-nav2-bringup

# Set TurtleBot3 model
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
```

### Install Gazebo

```bash
sudo apt install -y ros-humble-gazebo-ros-pkgs
```

## Quick Start

### 1. Launch the Maze World

```bash
# Terminal 1: Launch Gazebo with maze
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

# Or use our custom maze world:
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$(pwd)/worlds
ros2 launch gazebo_ros gazebo.launch.py world:=$(pwd)/worlds/maze.world
```

### 2. Launch Navigation

```bash
# Terminal 2: Launch Nav2
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True

# Terminal 3: Launch RViz for visualization
ros2 launch nav2_bringup rviz_launch.py
```

### 3. Set Initial Pose and Goal

In RViz:
1. Click "2D Pose Estimate" and click on the map where the robot is
2. Click "2D Goal Pose" and click where you want the robot to go
3. Watch the robot navigate!

## Files

```
ros2_simulation/
├── README.md           # This file
├── worlds/
│   └── maze.world      # Gazebo maze world file
├── launch/
│   └── maze_nav.launch.py  # Combined launch file
└── config/
    └── nav2_params.yaml    # Nav2 configuration
```

## Custom Maze World

The `worlds/maze.world` file contains a simple maze matching our physical maze dimensions (~1m x 1m). You can modify it to match your actual maze configuration.

## Useful ROS2 Commands

```bash
# List all topics
ros2 topic list

# View sensor data
ros2 topic echo /scan

# View velocity commands
ros2 topic echo /cmd_vel

# Manually send velocity command
ros2 topic pub /cmd_vel geometry_msgs/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"

# View the TF tree
ros2 run tf2_tools view_frames

# Check Nav2 status
ros2 topic echo /navigate_to_pose/_action/status
```

## Troubleshooting

### Gazebo crashes on startup
- Check GPU drivers: `nvidia-smi` or `glxinfo`
- Try software rendering: `export LIBGL_ALWAYS_SOFTWARE=1`

### Robot doesn't move
- Check that Nav2 is running: `ros2 node list`
- Verify localization: initial pose must be set in RViz

### Navigation fails
- Check costmaps in RViz (should show obstacles)
- Verify the map matches the world
- Try increasing inflation radius in config

## Learning Resources

- [Nav2 Documentation](https://navigation.ros.org/)
- [TurtleBot3 Manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)
- [Gazebo Tutorials](https://gazebosim.org/docs)
- [ROS2 Humble Docs](https://docs.ros.org/en/humble/)
