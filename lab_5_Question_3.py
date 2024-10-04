def fact(no):
    if no == 0 or no == 1:
        return 1
    else:
        return no * fact(no - 1)

x = 0
while x <= 10:
    print(f"The factorial of {x} is {fact(x)}")
    x += 1
