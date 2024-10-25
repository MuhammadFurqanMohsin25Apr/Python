sample = [(2, 3), (4, 7), (8, 11), (3, 6)]
A = int(input("Enter the index number: "))
position_1 = []
for i in sample:
    position_1.append(i[A])

min_value = min(position_1)
max_value = max(position_1)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
