A = [[5, 8], [1, 0], [2, 7]]
B = [[-4, -3], [2, 0]]

C = [[0, 0], [0, 0], [0, 0]]

for i in range(0, 3):
  for j in range(0, 2):
    C[i][j] = 0
    for k in range(0, 2):
      C[i][j] = C[i][j] + A[i][j] * B[k][j]

print(C)

