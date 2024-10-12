import math

def height(length, angle):
    radian = math.pi * (angle / 180)
    height = length * math.sin(radian)
    return height

# (a) 16 feet and 75 degrees:
print("The height is ", height(length=16, angle=75), "feet")

# (b) 20 feet and 0 degrees:
print("The height is ", height(length=20, angle=0), "feet")

# (c) 24 feet and 45 degrees:
print("The height is ", height(length=24, angle=45), "feet")

# (d) 24 feet and 80 degrees:
print("The height is ", height(length=24, angle=80), "feet")