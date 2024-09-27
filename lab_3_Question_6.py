# KNOWN:
# Velocity (u) in miles/hour:
u = float(input("Enter the velocity: "))

# Acceleration (a) in miles/hour**2:
a = float(input("Enter the acceleration: "))

# Time (t) in hours:
t = float(input("Enter the time: "))

# We need to find the distance (s) travelled by the car:
s = (u * t) + (1/2) * (a * t**2)

print("The distance covered by the car is:", s, "miles")

