a = 100
i = 0

while i < a:
    i = i + 1
    if i % 2 == 0:
        continue
    else:
        print(i, end=" ")
