temperature = 46
if temperature < 25:
    print("It is cold")
elif temperature > 25:
    print("It is hot")
else:
    print("Normal Temperature")

# A simple program to return the largest number among three numbers
first = 90
second = 45
third = 69
if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second, "is the largest number")
else:
    print(third, "is the largest number")

# Python program that checks whether a number is odd or even
number = int(65)
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")
number = int(58)
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")