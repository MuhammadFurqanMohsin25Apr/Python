import math


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))


D = (b**2) - (4 * a * c)


if a == 0:
    print("The equation cannot be solved as there is a zero in division")
else:
    
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

    
    print("The first and second solutions are: x1 =", x1, ", x2 =", x2)
