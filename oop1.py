class Student:
    def __init__(self,firstname,course,gender):
        self.firstname = firstname
        self.course = course
        self.gender = gender
    def study(self):
        print(self.firstname, "is studying")

student1 = Student("Sam", "Cybersecurity", "male")
student1.study()

