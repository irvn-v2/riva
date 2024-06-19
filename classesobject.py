# Class is a blueprint of an object
# Object is an instance of a class

class Person:
    # Properties/Attributes?Variables/Characteristics
    name = "James"
    age = 45
    gender = "Male"

    # Methods/Functions/Behaviors
    def move(self):
        print("Person is walking")

farmer = Person()
farmer.move()
print(farmer.gender)

doctor = Person()