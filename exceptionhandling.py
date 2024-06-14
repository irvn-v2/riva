try:
    x = 8
    print(x)
except:
    print("An error occurred")
finally:
    print("Success")

num1 = 67
num2 = 0

try:
    print(num1 / num2)
except:
    print("ZeroDivision error")
finally:
    print("Success")