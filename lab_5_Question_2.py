#(A)
no = 8
t = 4
i = 0

while i < no:
    while i < t:
        print("************")
        i = i + 1
    
    i = i + 1  

    while i >= 4 and i <= no:
        print(" ************")
        i = i + 1
#(B)
no = 8
row = 0

while row < no:
    stars = row + 1
    while stars > 0:
        print("*", end="")
        stars = stars - 1
    row = row + 1
    print()
#(C)
no = 7
i = 0
while (i < no):
    j = no - i
    while (j >= 1):
        print("*", end="")
        j = j - 1
    i = i + 1
    print()
