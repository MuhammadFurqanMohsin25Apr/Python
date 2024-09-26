
# KNOWN:
# Radius (r) in meters:
r = float(input("Enter the radius:"))

# Angular Speed (ω) in radians/second:
ω = float(input("Enter the Angular Speed:"))

# Time (T) in seconds in which the car travels:
T = float(input("Enter the time:"))

# We need to find the distance (d):
# d = v * T since v = r * ω then
d = r * ω * T

# Output the calculated distance
print("The car travels the distance of", d, "in 10 seconds")
