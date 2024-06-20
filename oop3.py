class Device:
    def __init__(self, model, yom):
        self.model = model
        self.yom = yom

    def crush(self):
        print(self.model, "which was made on", self.yom, "has crushed")

computer = Device("HP", 2008)
computer.crush()

laptop = Device("Dell", 1992)
laptop.crush()

phone = Device("Samsung", 2024)
phone.crush()
