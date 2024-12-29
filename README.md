# Hexapod Controller 

## Overview

This project simulates a hexapod robot using Webots, with controllers for basic movement and turning behavior. The robot is equipped with 12 motors, enabling it to perform a variety of motions, including forward/backward movement and turning with distinct control over the legs.

### Project Structure

```
├───controllers
│   ├───drive_robot
│   │       drive_robot.py
│   │
│   └───drive_robot_turn
│           drive_robot_turn.py
│
└───worlds
        hexapod.wbt
```

### Key Files:
- **drive_robot.py**: Defines a controller for basic forward and backward motion for the hexapod.
- **drive_robot_turn.py**: Defines a controller for turning motions, adjusting leg angles based on the direction of turn (clockwise rotation).
- **hexapod.wbt**: The Webots world file containing the environment setup for the hexapod robot.

## Mechanics

### Robot Setup

The hexapod robot has 12 motors, organized as follows:
- 6 motors for the hip joint (3 for the left side and 3 for the right side).
- 6 motors for the knee joint (3 for the left side and 3 for the right side).

Each leg has a corresponding motor at the hip and knee joints, with the following naming convention:
- `"hip_motor_l0"`, `"hip_motor_l1"`, `"hip_motor_l2"` for the left leg hip joints.
- `"hip_motor_r0"`, `"hip_motor_r1"`, `"hip_motor_r2"` for the right leg hip joints.
- `"knee_motor_l0"`, `"knee_motor_l1"`, `"knee_motor_l2"` for the left leg knee joints.
- `"knee_motor_r0"`, `"knee_motor_r1"`, `"knee_motor_r2"` for the right leg knee joints.

### Motion Control

The robot is controlled by a sequence of motor positions corresponding to different states of movement. These states define the positions of the robot's limbs during its motions, allowing it to perform various patterns, such as walking forward, backward, and turning.

#### `drive_robot.py` - Forward and Backward Motion:
- The `drive_robot.py` controller enables the robot to perform basic forward and backward movements.
- **Positions** for each motor are specified in the `pos` list, where each state defines the angle of each motor.
  - **FRONT**: +0.7 (used for forward motion).
  - **BACK**: -0.7 (used for backward motion).
  - **HI** and **LO**: Define small positive and negative angles for fine adjustments.

The robot cycles through states in `pos` and updates its motor positions every 25 steps, creating the motion.

#### `drive_robot_turn.py` - Turning Motion:
- The `drive_robot_turn.py` controller defines a modified behavior for turning, where the robot adjusts the angles of its legs based on the direction of rotation.
- **TURN_OUTER**: +0.7 (larger angle for the outer legs to enable a wider arc).
- **TURN_INNER**: +0.3 (smaller angle for the inner legs for a sharper turn).
- The robot adjusts the motor positions in such a way that the outer legs (left and right sides) are angled more than the inner legs during turns, allowing the robot to rotate in place.

#### State Logic:
- The `state` variable in both scripts determines which set of motor positions is active, cycling through the `pos` list for different movement patterns.
- The robot alternates between these states based on the elapsed time (incremented every 16ms), with each state representing a different leg movement configuration.

### Initialization and Loop
1. **Initialization**: The script initializes the motors and sets their positions to `0.0`.
2. **Main Loop**: Each loop iteration updates the motor positions to match the current state, enabling the robot to perform its intended motion.

## Usage Instructions

1. **Load the Webots World**:
   - Open `hexapod.wbt` in Webots. This file contains the robot and the simulation environment.

2. **Select the Controller**:
   - In Webots, select the robot in the 3D scene.
   - In the "Controller" tab, choose either `drive_robot` or `drive_robot_turn` as the controller for the robot.

3. **Run the Simulation**:
   - Click the "Play" button in Webots to start the simulation. The robot will begin moving according to the selected controller script.

4. **Observe the Motion**:
   - **With `drive_robot.py`**: The robot moves forward and backward using simple leg movements.
   - **With `drive_robot_turn.py`**: The robot turns in place, adjusting leg angles for rotation.

## Conclusion

This project demonstrates basic hexapod locomotion control in Webots, with two controllers for different movement behaviors: forward/backward motion and turning. The mechanics of the robot's movements are based on coordinated changes in the positions of its 12 motors, enabling complex motion patterns.
