# KNOWN:
# The initial velocity (u) of stone in ft/s:
u = float(input("Enter the initial velocity: "))

# Acceleration due to gravity (a) in ft/s**2:
a = float(input("Enter the acceleration due to gravity: "))

# Height (h) in feet:
h = float(input("Enter the height: "))

# We need to find the final velocity (v):
# FORMULA:
# v**2 = u**2 + 2*a*h
import math
v = math.sqrt((2 * a * h) + (u**2))

print("The velocity with which the stone hit the ground is:", v, "ft/s")
