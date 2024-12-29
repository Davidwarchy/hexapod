from controller import Robot

# Constants
time_step = 16
num_motors = 12
num_states = 6

FRONT = +0.7
BACK = -0.7
HI = +0.02
LO = -0.02

motor_names = [
    "hip_motor_l0", "hip_motor_l1", "hip_motor_l2", 
    "hip_motor_r0", "hip_motor_r1", "hip_motor_r2", 
    "knee_motor_l0", "knee_motor_l1", "knee_motor_l2", 
    "knee_motor_r0", "knee_motor_r1", "knee_motor_r2"
]

# Define the positions for each state
pos = [
    [BACK, FRONT, BACK, -FRONT, -BACK, -FRONT, LO, HI, LO, HI, LO, HI],
    [BACK, FRONT, BACK, -FRONT, -BACK, -FRONT, HI, HI, HI, HI, HI, HI],
    [BACK, FRONT, BACK, -FRONT, -BACK, -FRONT, HI, LO, HI, LO, HI, LO],
    [FRONT, BACK, FRONT, -BACK, -FRONT, -BACK, HI, LO, HI, LO, HI, LO],
    [FRONT, BACK, FRONT, -BACK, -FRONT, -BACK, HI, HI, HI, HI, HI, HI],
    [FRONT, BACK, FRONT, -BACK, -FRONT, -BACK, LO, HI, LO, HI, LO, HI]
]

# Create the Robot instance
robot = Robot()

# Initialize motors
motors = []
for motor_name in motor_names:
    motor = robot.getDevice(motor_name)
    if motor:
        motors.append(motor)
        motor.setPosition(0.0)
    else:
        print(f"Could not find motor: {motor_name}")

# Main loop
elapsed = 0
while robot.step(time_step) != -1:
    elapsed += 1
    state = (elapsed // 25 + 1) % num_states
    for i in range(num_motors):
        motors[i].setPosition(pos[state][i])

