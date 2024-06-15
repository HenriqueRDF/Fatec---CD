import time

A = [[2,-1,3],[0,4,-6],[-6,10,-5]]
B = [[4,7,-8],[9,3,5],[1,-1,2]]
S = [[0,0,0],[0,0,0],[0,0,0]]

temp_start = time.time()

for k in range(1):
  for i in range(3):
    for j in range(3):
      S[i][j] = 0
      S[i][j] = A[i][j] + B[i][j]

temp_finish = time.time()

print(S)
print(f'Tempo de Processamento: {temp_finish - temp_start}')

temp_start = time.time()

for k in range(1):
  for i in range(3):
    for j in range(3):
      S[i][j] = 0
      for l in range(3):
        S[i][j] = S[i][j] + A[i][l] * B[l][j]

temp_finish = time.time()

print(S)
print(f'Tempo de Processamento: {temp_finish - temp_start}')
