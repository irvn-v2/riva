# A simple python program to demonstrate encapsulation

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.__major = major  # Private attribute

    def display_student_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Major: {self.__major}")

    def get_major(self):
        return self.__major

    def set_major(self, new_major):
        self.__major = new_major


# Creating instances of Student
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 21, "Electrical Engineering")

# Accessing public attributes directly
print(f"{student1.name}'s age is {student1.age}")
print(f"{student2.name}'s age is {student2.age}")

# Accessing private attribute using getter method
print(f"{student1.name}'s major is {student1.get_major()}")

# Trying to set major directly (which won't work due to private attribute)
# Uncomment the line below to see the effect
# student1.__major = "Physics"

# Setting major using setter method
student1.set_major("Information Technology")
print(f"{student1.name}'s updated major is {student1.get_major()}")

# Displaying student information using a method
student2.display_student_info()

