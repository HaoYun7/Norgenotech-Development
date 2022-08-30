import os


class CodeGenerator:

    #Notes: Get a lot of liquid and blow some liquid out with two different speed add one more function

    # Just some default setting will be added to setting file later
    has_tip = False
    tip_pick_up_location = []

    # Change the path to whatever you want the file to be in
    file_path = "C:\\University\\Programming project\\python\\pythonProject\\Norgenotech-Development\\PC_END\\GCODE\\output\\process2.txt"
    write_or_append = "a"
    default_z = 50
    extra_amount_aspirate = 50

    def __init__(self):
        tip_pick_up_location = []
        tip_trash = [5, 5, 5]
        speed = 30

    def clean_file(self):  # function to delete everything from a file
        f = open(self.file_path, "w")
        f.close()

    def make_gcode_file(self):  # ignore this for now
        pre, ext = os.path.splitext("process.txt")
        os.rename('process.txt', pre + '.gcode')

    def pick_up_tip(self, location, xy_speed, z_speed):

        # save the location where the tip is picked up
        self.tip_pick_up_location = location
        f = open(self.file_path, self.write_or_append)

        # move the arm up first for safety reason
        f.write("G1 " + "Z-" + str(self.default_z) + " F" + str(z_speed))
        f.write("\n")

        # move the arm into the given location for x and y coord with speed given
        move_to_location = "G1 " + "X" + str(location[0]) + " Y" + str(location[1]) + " F" + str(xy_speed)
        f.write(move_to_location)
        f.write("\n")

        # move the arm into the given z coord with speed given
        move_down = "G1 " + "Z-" + str(location[2]) + " F" + str(z_speed)
        f.write(move_down)
        f.write("\n")

        # move the arm up into safety z position again
        move_up = "G1 " + "Z-" + str(self.default_z) + " F" + str(z_speed)
        f.write(move_up)
        f.write("\n")

        # will indicate that arm is holding a tip
        self.has_tip = True
        f.close()

    def drop_tip(self, location, xy_speed, z_speed):

        # check if there is a tip on arm
        if self.has_tip:
            f = open(self.file_path, self.write_or_append)

            # move the arm up first for safety reason
            f.write("G1 " + "Z-" + str(self.default_z) + " F" + str(z_speed))
            f.write("\n")

            # move the arm into the given location for x and y coord with speed given
            move_to_location = "G1 " + "X" + str(location[0]) + " Y" + str(location[1]) + " F" + str(xy_speed)
            f.write(move_to_location)
            f.write("\n")

            # perform the action that drop the tip
            self.perform_drop_tip()
        else:
            print("there is no tip to drop")

    def perform_drop_tip(self):  # will be added when the exact movement is known
        pass

    def return_tip_wrong(self, xy_speed, z_speed):  # Might be changed later ignore now

        if self.tip_pick_up_location != []:
            f = open("process.txt", self.write_or_append)

            f.write("G1 " + "Z-" + str(self.default_z) + " F" + str(z_speed))
            f.write("\n")

            move_to_location = "G1 " + "X" + str(self.tip_pick_up_location[0]) + " Y" + str(self.tip_pick_up_location[1]) + " F" + str(xy_speed)
            f.write(move_to_location)
            f.write("\n")
        else:
            print("there was no previous movement")

    def aspirate(self, location, amount_to_aspirate, xy_speed, z_speed):
        # g1 command g1 e0 f-speed do not use absolut coord g90 or g91 and check g92
        f = open(self.file_path, self.write_or_append)

        # move the arm up first for safety reason
        f.write("G1 " + "Z-" + str(self.default_z) + " F" + str(z_speed))
        f.write("\n")

        # move the arm into the given location for x and y coord with speed given
        move_to_location = "G1 " + "X" + str(location[0]) + " Y" + str(location[1]) + " F" + str(xy_speed)
        f.write(move_to_location)
        f.write("\n")

        # move the arm into the given z coord with speed given
        move_down = "G1 " + "Z-" + str(location[2]) + " F" + str(z_speed)
        f.write(move_down)
        f.write("\n")

        # take the liquid in with some extra
        f.write("G91 " + "E-" + str(amount_to_aspirate + self.extra_amount_aspirate) + " F" + str(z_speed))
        f.write("\n")

        # eject the extra liquid out
        f.write("G91 " + "E" + str(self.extra_amount_aspirate) + " F" + str(z_speed))
        f.write("\n")

        # move the arm up again
        move_up = "G1 " + str(self.default_z) + " F" + str(z_speed)
        f.write(move_up)
        f.write("\n")
        f.close()

    def dispense(self, location, amount_to_dispense, xy_speed, z_speed):
        f = open(self.file_path, self.write_or_append)

        # move the arm up first for safety reason
        f.write("G1 " + "Z-" + str(self.default_z) + " F" + str(z_speed))
        f.write("\n")

        # move the arm into the given location for x and y coord with speed given
        move_to_location = "G1 " + "X" + str(location[0]) + " Y" + str(location[1]) + " F" + str(xy_speed)
        f.write(move_to_location)
        f.write("\n")

        # move the arm into the given z coord with speed given
        move_down = "G1 " + "Z-" + str(location[2]) + " F" + str(z_speed)
        f.write(move_down)
        f.write("\n")

        # eject the liquid out
        f.write("G91 " + "E" + str(amount_to_dispense) + " F" + str(z_speed))
        f.write("\n")

        # move the arm up again
        move_up = "G1 " + str(self.default_z) + " F" + str(z_speed)
        f.write(move_up)
        f.write("\n")
        f.close()

    def blow_out(self, air_to_blowout, speed):
        f = open(self.file_path, self.write_or_append)

        # blow the amount of air out
        f.write("G91 " + "E" + str(air_to_blowout) + " F" + str(speed))
        f.write("\n")
        f.close()

    def air_gap(self, air_to_take_in, speed):
        f = open(self.file_path, self.write_or_append)

        # take in the amount of air
        f.write("G91 " + "E-" + str(air_to_take_in) + " F" + str(speed))
        f.write("\n")
        f.close()

    def touch_tip(self):
        pass

    def mix(self):
        pass

    def time_delay(self, second):
        f = open(self.file_path, self.write_or_append)

        # time delayed in seconds
        f.write("G4 " + "X" + str(second))
        f.write("\n")
        f.close()

    def pause(self):
        f = open(self.file_path, self.write_or_append)

        # just pause
        f.write("M25")
        f.write("\n")
        f.close()

    def complex_movement(self, all_locations, xy_speed, z_speed, function):  # Not done ignore for now
        f = open(self.file_path, self.write_or_append)
        f.write("G01 " + "Z-200" + " F" + str(z_speed))
        f.write("\n")

        if function == 1:
            for location in all_locations:
                self.dispense(location, 20, 50, 100)

            # if want to do something in between






