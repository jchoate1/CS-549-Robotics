# CS-549 Robotics - Original Syllabus

*Adapted from the original 7-week course by Charles N. Stevenson, Rivier University*

## Course Description

This course examines algorithms for motion planning, current technologies for sensing, and methodologies for course correction used in mobile robotics and other autonomous systems.

## Learning Outcomes

Upon completion of this course, the student should learn:

1. Algorithms for motion planning
2. Software methods for trajectory generation and control
3. Serial communication protocols commonly used in mobile robots for sensing
4. Sensing technologies used in autonomous systems
5. Real-time programming methods for integrating motion and sensing
6. Mathematics and algorithms for location estimate and course correction

## Course Topics Overview

| Week | Topics | Labs/Assignments |
|------|--------|------------------|
| 1 | Configuration space, wavefront planning, A* | Lab 1: Path Planning |
| 2 | Incremental planning (LPA*, D* Lite), motor control, encoders | Lab 2: Trajectory Execution, Homework 1 |
| 3 | Robot kinematics, spline curves, homogeneous coordinates | Lab 3: Range Sensor/Spline Path |
| 4 | Velocity kinematics, range sensing, Wokwi simulator | Lab 4: Range Sensor Maze, Quiz 1 |
| 5 | Motion timers, hexapod/mecanum robots | Lab 4 continued, Vision assignment |
| 6 | Interrupts, vision for robotics, serial communications | Lab 5: Student Project, Quiz 2 |
| 7 | Real-time OS, I2C/SPI protocols, asyncio | Lab 5 continued |

## Required Materials

- Mobile robot kit (Arduino Alvik or Pololu 3pi)
- *Introduction to Autonomous Systems* - Nikolaus Correll (free on GitHub)
- *Planning Algorithms* - Steven LaVelle (free at http://lavalle.pl/planning/)

## Original Lab Projects

### Lab 1: Path Planning with Obstacles
Use configuration space and either wavefront planning or A* to generate a path through a grid with obstacles.

### Lab 2: Trajectory Execution
Use the class library for motion and sensing to execute a path on a grid without obstacles. Measure the distance between the desired goal and actual location.

### Lab 3: Range Sensor Interfacing / Spline Path Generation
Interface a range sensor to the robot microcontroller. Write MicroPython code to generate spline motion.

### Lab 4: Range Sensor Maze Exploration
Use the range sensor for maze navigation.

### Lab 5: Student Project
Students select from a list of projects involving advanced topics.

## Additional Assignments

- **Wokwi Program**: Simulate four range sensors using the Wokwi simulator
- **Edge Impulse Program**: Train a neural network using Edge Impulse
- **Quizzes**: Two quizzes covering lecture material

## Grading (Original)

| Component | Weight |
|-----------|--------|
| Lab Projects (5) | 65% |
| Participation | 5% |
| Homework Problems | 10% |
| Wokwi Program | 5% |
| Edge Impulse Program | 5% |
| Quizzes (2) | 10% |

---

*Note: This weekend intensive adapts the above content into a 2-day format. See the Course Plan for the compressed schedule.*
