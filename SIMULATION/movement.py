import component
import numpy as np
from vpython import *


class Movement:
    robot = component.Component()

    # This is the speed which object is moving in the simulation
    delta = .01

    # To check which movement function to use
    # bar = True
    # hand = False
    finger = False

    # This function is used to move the middle bar of the robot
    def move_bar(self, target):
        x_pos = self.robot.mid_bar.pos.x

        if float("{0:.2f}".format(x_pos)) < target.x:
            x_pos = x_pos + self.delta
            # print(x_pos)
        elif float("{0:.2f}".format(x_pos)) > target.x:
            x_pos = x_pos - self.delta
            # print(x_pos)
        elif float("{0:.2f}".format(x_pos)) == target.x:
            print("target reached")
            # self.bar = False
            # self.hand = True

        self.robot.mid_bar.pos = vector(x_pos, self.robot.mid_bar.pos.y, self.robot.mid_bar.pos.z)
        self.robot.hand.pos = vector(x_pos, self.robot.hand.pos.y, self.robot.hand.pos.z)
        self.robot.finger.pos = vector(x_pos, self.robot.finger.pos.y, self.robot.finger.pos.z)

    # This function is used to move the hand of the robot
    def move_hand(self, target):
        z_pos = self.robot.hand.pos.z

        if float("{0:.2f}".format(z_pos)) < target.z:
            z_pos = z_pos + self.delta
            # print(z_pos)
        elif float("{0:.2f}".format(z_pos)) > target.z:
            z_pos = z_pos - self.delta
            # print(z_pos)
        elif float("{0:.2f}".format(z_pos)) == target.z:
            # print("target reached")
            # self.hand = False
            self.finger = True
        self.robot.hand.pos = vector(self.robot.hand.pos.x, self.robot.hand.pos.y, z_pos)
        self.robot.finger.pos = vector(self.robot.finger.pos.x, self.robot.finger.pos.y, z_pos)

    # This function is used to move the finger of the robot
    def move_finger(self, target):
        y_pos = self.robot.finger.pos.y

        if float("{0:.2f}".format(y_pos)) < target.y:
            y_pos = y_pos + self.delta
            # print(y_pos)
        elif float("{0:.2f}".format(y_pos)) > target.y:
            y_pos = y_pos - self.delta
            # print(y_pos)
        elif float("{0:.2f}".format(y_pos)) == target.y:
            # print("target reached")
            self.finger = False
        self.robot.finger.pos = vector(self.robot.finger.pos.x, y_pos, self.robot.finger.pos.z)

    # This function controls the whole movement, bar -> hand -> finger
    # def make_move(self, target):
    #     if self.bar:
    #         self.move_bar(target)
    #     elif self.hand:
    #         self.move_hand(target)
    #     elif self.finger:
    #         self.move_finger(target)

    def make_move2(self, target):
        # self.move_bar(target)
        # self.move_hand(target)
        self.move_finger(target)





