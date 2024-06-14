# Inbuilt functions/Standard Library Functions

y = min(23, 56, 1000, 5647)
print("The minimum number is", y)

x = max(90, 2, 98, 45)
print("The maximum number is", x)

z = pow(2, 3)
print(z)

# User-defined Functions
def school():
    print("eMobilis")

school()  # Calling a function

def multiply():
    num1 = 5
    num2 = 6
    print(num1 * num2)
multiply()

# Parameters and arguments
def add(a, b):
    print(a + b)
add(35, 29)
add(10, 9)
add(30, 24)
add(11, 72)
add(27, 39)

def employee(Fullname, age, salary, phone, position):
    print(Fullname, age, salary, phone, position)

employee("Job Kamau", 45, 115000, 741512929, "Managing Director")
employee("Irene Nzisa", 39, 120000, 724909451, "Project Manager")
employee("Enoch Musili", 32, 95500, 741512929, "AI Engineer")
employee("Kevin Mwendwa", 51, 150000, 768147478, "Software Engineer")
employee("Syelle Brown", 32, 92700, 721274174, "Web Developer")