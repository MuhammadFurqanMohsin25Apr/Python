start = int(input("enter starting value: "))
end = int(input("enter ending value: "))

for i in range(start, end + 1):
    for j in range(start, end + 1):
        print(i * j, end=" ")
    print()
