# Arithmetic Operators - Simple calculations
num1 = 56
num2 = 8

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)
print(num1 % num2)  # Modulus - Returns the remainder

# Comparison operators - Compare values
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)  # Equal to
print(num1 != num2)  # Not equal to

# Assignment operators - Assign values to variables
a = 200
print(a)

a += 20
print(a)

# Logic operators - and, or, not
x = 100
print(250 > x > 1000)
print(x < 250 or x > 1000)
print(not (x < 250 or x > 1000))

# Operator Predence - Order in which operations get executed
output = (100 - 4 * 3 / 1)
print(output)
print(int(output))

# Write a simple program that returns the area of a trapezium
# A = 1/2 * (A+B) * H
A = 15
B = 10
H = 7
area = 1/2 * (15+10) * 18
print("The area is", area)