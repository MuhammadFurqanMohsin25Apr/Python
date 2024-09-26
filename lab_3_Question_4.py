# KNOWN:
# Radius (r) in meters:
r = float(input("Enter the radius (in meters): "))

# Linear Speed (v) in meters/second:
v = float(input("Enter the linear speed (in meters/second): "))

# We need to find Angular Speed:
# FORMULA:
# ω = v / r

# Calculate angular speed
angular_speed = v / r

# Output the result
print("The angular speed is", angular_speed, "radians/second")
