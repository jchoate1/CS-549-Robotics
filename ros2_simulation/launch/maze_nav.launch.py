#!/usr/bin/env python3
"""
Launch file for maze navigation demo.

This launches:
1. Gazebo with the maze world
2. TurtleBot3 robot
3. Nav2 navigation stack
4. RViz for visualization

Usage:
  ros2 launch maze_nav.launch.py
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Get package directories
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')
    pkg_nav2_bringup = get_package_share_directory('nav2_bringup')
    
    # Get the path to our maze world
    # Note: Update this path to your actual workspace location
    maze_world = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'worlds', 'maze.world'
    )
    
    # Launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    # Declare launch arguments
    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation time'
    )
    
    # Launch Gazebo with maze world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={
            'world': maze_world,
            'verbose': 'true'
        }.items()
    )
    
    # Spawn TurtleBot3
    spawn_turtlebot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_turtlebot3_gazebo, 'launch', 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': '0.0',
            'y_pose': '-0.4',  # Start position
            'z_pose': '0.01'
        }.items()
    )
    
    # Launch Nav2
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2_bringup, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'use_sim_time': use_sim_time,
        }.items()
    )
    
    # Launch RViz
    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2_bringup, 'launch', 'rviz_launch.py')
        )
    )
    
    return LaunchDescription([
        declare_use_sim_time,
        gazebo,
        spawn_turtlebot,
        # Uncomment these when you have Nav2 configured:
        # nav2,
        # rviz,
    ])


if __name__ == '__main__':
    generate_launch_description()
