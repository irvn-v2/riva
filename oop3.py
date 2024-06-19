class Device:
    def __init__(self, model, yom):
        self.model = model
        self.yom = yom

    def crush(self):
        print(self.model, "has crushed")

computer = Device("HP", 2008)
computer.crush()

laptop = Device("Dell", 1992)
laptop.crush()