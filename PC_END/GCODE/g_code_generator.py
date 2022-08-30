import os


class CodeGenerator:

    #Notes: Get a lot of liquid and blow some liquid out with two different speed add one more function

    # implement a simple setting file
    has_tip = False
    tip_pick_up_location = []
    file_path = "C:\\University\\Programming project\\python\\pythonProject\\Norgenotech-Development\\PC_END\\GCODE\\output\\process2.txt"
    write_or_append = "a"

    def __init__(self):
        tip_pick_up_location = []
        tip_trash = [5, 5, 5]
        speed = 30

    def clean_file(self):
        f = open(self.file_path, "w")
        f.close()

    def make_gcode_file(self):
        pre, ext = os.path.splitext("process.txt")
        os.rename('process.txt', pre + '.gcode')

    def pick_up_tip(self, location, xy_speed, z_speed):
    #check z axis first for safety reason
    # add safety 50mm
        self.tip_pick_up_location = location
        f = open(self.file_path, self.write_or_append)

        f.write("G01 " + "Z-200" + " F" + str(z_speed))
        f.write("\n")

        move_to_location = "G01 " + "X" + str(location[0]) + " Y" + str(location[1]) + " F" + str(xy_speed)
        f.write(move_to_location)
        f.write("\n")

        move_down = "G01 " + "Z-400" + " F" + str(z_speed)
        f.write(move_down)
        f.write("\n")

        move_up = "G01 " + "Z-200" + " F" + str(z_speed)
        f.write(move_up)
        f.write("\n")
        self.has_tip = True
        f.close()

    def drop_tip(self, location, xy_speed, z_speed):

        if self.has_tip:
            f = open(self.file_path, self.write_or_append)

            f.write("G01 " + "Z-200" + " F" + str(z_speed))
            f.write("\n")

            move_to_location = "G01 " + "X" + str(location[0]) + " Y" + str(location[1]) + " F" + str(xy_speed)
            f.write(move_to_location)
            f.write("\n")

            if len(location) == 2:
                move_down = "G01 " + "Z-" + str(location[2]) + " F" + str(z_speed)
                f.write(move_down)
                f.write("\n")

                move_up = "G01 " + "Z-200" + " F" + str(z_speed)
                f.write(move_up)
                f.write("\n")
                f.close()
            else:
                move_down = "G01 " + "Z-400" + " F" + str(z_speed)
                f.write(move_down)
                f.write("\n")

                move_up = "G01 " + "Z-200" + " F" + str(z_speed)
                f.write(move_up)
                f.write("\n")
                f.close()
        else:
            print("there is no tip to drop")

    def return_tip_wrong(self, xy_speed, z_speed): # Might be changed later ignore now
        if self.tip_pick_up_location != []:
            f = open("process.txt", self.write_or_append)

            f.write("G01 " + "Z-200" + " F" + str(z_speed))
            f.write("\n")

            move_to_location = "G01 " + "X" + str(self.tip_pick_up_location[0]) + " Y" + str(self.tip_pick_up_location[1]) + " F" + str(xy_speed)
            f.write(move_to_location)
            f.write("\n")
        else:
            print("there was no previous movement")


    def aspirate(self, amount_to_aspirate, speed):
        # g1 command g1 e0 f-speed do not use absolut coord g91 or g92
        pass

    def dispense(self, location, amount_to_dispense, xy_speed, z_speed):
        f = open(self.file_path, self.write_or_append)

        f.write("G01 " + "Z-100" + " F" + str(z_speed))
        f.write("\n")

        move_to_location = "G01 " + "X" + str(location[0]) + " Y" + str(location[1]) + " F" + str(xy_speed)
        f.write(move_to_location)
        f.write("\n")

        move_down = "G01 " + "Z-400" + " F" + str(z_speed)
        f.write(move_down)
        f.write("\n")

        f.write("G01 " + "E" + str(amount_to_dispense) + " F" + str(z_speed))
        f.write("\n")

        move_up = "G01 " + "Z-200" + " F" + str(z_speed)
        f.write(move_up)
        f.write("\n")
        f.close()

    def blow_out(self, air_to_blowout, speed):
        f = open(self.file_path, self.write_or_append)
        f.write("G01 " + "E" + str(air_to_blowout) + " F" + str(speed))
        f.write("\n")
        f.close()

    def touch_tip(self):
        pass

    def mix(self):
        pass

    def air_gap(self):
        pass

    def time_delay(self, second):
        # dwell g04 command
        f = open(self.file_path, self.write_or_append)
        f.write("G04 " + "X" + str(second))
        f.write("\n")
        f.close()

    def pause(self):
        # gcode m25
        pass

    def complex_movement(self, all_locations, xy_speed, z_speed, function):
        f = open(self.file_path, self.write_or_append)
        f.write("G01 " + "Z-200" + " F" + str(z_speed))
        f.write("\n")

        if function == 1:
            for location in all_locations:
                self.dispense(location, 20, 50, 100)

            # if want to do something in between






