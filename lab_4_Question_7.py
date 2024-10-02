A = [[2, 5, 7],
     [3, 6, 4],
     [1, 8, 3]]

B = [[8, 6, 7, 1],
     [5, 4, 3, 9],
     [6, 7, 5, 1]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for i in result:
    print(i)

