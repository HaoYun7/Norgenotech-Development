class CodeReader:

    def __init__(self):
        self.lines = self.read_file()

    # Just a reader which read the g_code file in GCODE folder
    def read_file(self):
        with open('C:\\University\\Programming project\\python\\pythonProject\\Norgenotech-Development\\PC_END\\GCODE\\test1') as f:
            lines = [line.rstrip() for line in f]
        return lines


# reader = CodeReader()
# a = reader.read_file()
# test = a[0]
# print(test.split())
