import math

(x, y) = (0, 0)
x1 = int(input("Enter x-coordinate: "))
y1 = int(input("Enter y-coordinate: "))
(a, b) = (x1, y1)
hits = math.sqrt((x1 - x)**2 + (y1 - y)**2) <= 10

print("Dart at", (a, b), "hits board:", hits)
