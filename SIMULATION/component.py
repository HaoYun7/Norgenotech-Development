from vpython import *


class Component:
    def __init__(self):
        # parameters for ground
        self.ground_location = vector(0, -5, 0)
        self.ground_color = color.white
        self.ground_length = 9
        self.ground_height = .1
        self.ground_width = 5
        self.ground = box(pos=self.ground_location, color=self.ground_color, length=self.ground_length, height=self.ground_height, width=self.ground_width)

        # parameters for right bar
        self.right_bar_location = vector(0, -1, 2.75)
        self.right_bar_color = color.yellow
        self.right_bar_length = 9
        self.right_bar_height = .5
        self.right_bar_width = .5
        self.right_bar = box(pos=self.right_bar_location, color=self.right_bar_color, length=self.right_bar_length, height=self.right_bar_height, width=self.right_bar_width)

        # parameters for left bar
        self.left_bar_location = vector(0, -1, -2.75)
        self.left_bar_color = color.yellow
        self.left_bar_length = 9
        self.left_bar_height = .5
        self.left_bar_width = .5
        self.left_bar = box(pos=self.left_bar_location, color=self.left_bar_color, length=self.left_bar_length, height=self.left_bar_height, width=self.left_bar_width)

        # parameter for mid bar
        self.mid_bar_location = vector(0, -1, 0)
        self.mid_bar_color = color.blue
        self.mid_bar_length = .5
        self.mid_bar_height = .5
        self.mid_bar_width = 5
        self.mid_bar = box(pos=self.mid_bar_location, color=self.mid_bar_color, length=self.mid_bar_length, height=self.mid_bar_height, width=self.mid_bar_width)

        # parameter for hand
        self.hand_location = vector(0, -1.5, 0)
        self.hand_color = color.green
        self.hand_length = 1
        self.hand_height = 1.5
        self.hand_width = 1
        self.hand = box(pos=self.hand_location, color=self.hand_color, length=self.hand_length, height=self.hand_height, width=self.hand_width)

        # parameter for finger
        self.finger_location = vector(0, -2.0, 0)
        self.finger_color = color.red
        self.finger_radius = .5
        self.finger_axis = vector(0, -1, 0)
        self.finger = cone(pos=self.finger_location, color=self.finger_color, axis=self.finger_axis, radius=self.finger_radius)

    # def set_ground(self):
    #     return box(pos=self.ground_location, color=self.ground_color, length=self.ground_length, height=self.ground_height, width=self.ground_width)
    #
    # def set_right_bar(self):
    #     return box(pos=self.right_bar_location, color=self.right_bar_color, length=self.right_bar_length, height=self.right_bar_height, width=self.right_bar_width)
    #
    # def set_left_bar(self):
    #     return box(pos=self.left_bar_location, color=self.left_bar_color, length=self.left_bar_length, height=self.left_bar_height, width=self.left_bar_width)
    #
    # def set_mid_bar(self):
    #     return box(pos=self.mid_bar_location, color=self.mid_bar_color, length=self.mid_bar_length, height=self.mid_bar_height, width=self.mid_bar_width)
    #
    # def set_hand(self):
    #     return box(pos=self.hand_location, color=self.hand_color, length=self.hand_length, height=self.hand_height, width=self.hand_width)
    #
    # def set_finger(self):
    #     return cone(pos=self.finger_location, color=self.finger_color, axis=self.finger_axis, radius=self.finger_radius)
    #

