class Car:
    def __init__(self,model,color,manufacturer,yop):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yop = yop


    def speed(self):
        print("The manufacturer of", self.model, "is", self.manufacturer, ".It's color is", self.color, "and was purchased on", self.yop)

car1 = Car("B12", "white", "BMW", 2024)
car1.speed()

car2 = Car("B12", "white", "BMW", 2024)
car3 = Car("B12", "white", "BMW", 2024)
car4 = Car("B12", "white", "BMW", 2024)
car5 = Car("B12", "white", "BMW", 2024)

