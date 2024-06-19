# Parent class/Base class/Super class
class Animal:
    Has_scales = True
    def sound(self):
        print("Animal is speaking")

# Child class/Sub class/Derived class
class Duck(Animal):
    Has_wings = True
    def move(self):
        print("Duck is swimming")

class Caterpillar:
    def move(self):
        print("Caterpillar is slithering")

a = Animal()

d = Duck()
print(d.Has_wings)

c = Caterpillar()