a = [[2, 5, 10],
     [8, 6, 7],
     [3, 4, 9]]

b = [[5, 6, 8],
     [3, 2, 1],
     [6, 7, 4]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        result[i][j] = a[i][j] + b[i][j]

for x in result:
    print(x)
