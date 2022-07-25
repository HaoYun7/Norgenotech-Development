from vpython import *
from PC_END.GCODE import g_code_reader
import component
import movement

robot = component.Component()
movement = movement.Movement()

reader = g_code_reader.CodeReader()

# line = reader.read_file()
# print(line)

# Set your target location here x,y,z
target = vector(1, -4, 2)

# This file runs the whole simulation
while True:
    rate(10)
    movement.make_move(target)
    # print("arm is at:", robot.mid_bar.pos)
