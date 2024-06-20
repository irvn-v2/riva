class Student:
    def __init__(self,firstname,course,gender):
        self.firstname = firstname
        self.course = course
        self.gender = gender
    def study(self):
        print(self.firstname, "is a", self.gender, "and studies", self.course)

student1 = Student("Sam", "Cybersecurity", "male")
student1.study()

student2 = Student("Irvn", "Python", "male")
student2.study()

student3 = Student("Nicole", "Software engineering", "female")
student3.study()
