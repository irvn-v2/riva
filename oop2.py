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

car2 = Car("cayenne", "red", "Porsche", 2019)
car2.speed()

car3 = Car("harrier", "black", "Toyota", 2021)
car3.speed()

car4 = Car("vogue", "beige", "Range Rover", 2015)
car4.speed()

car5 = Car("bentayga", "yellow", "Bentley", 2015)
car5.speed()
