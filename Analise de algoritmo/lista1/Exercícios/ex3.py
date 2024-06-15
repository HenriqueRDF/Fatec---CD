import time
import random

A = list(range(1,51))

print('Matriz não ordenada = ', A)
print('Len = ', len(A))

temp_start = time.time()

for k in range(1000):
  for i in range(1,len(A)):
    temp = A[i]
    j = i -1
    while j >= 0 and A[j] > temp:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = temp

temp_finish = time.time()

print('Matriz ordenada = ',A)
print('Tempo Execução = ', temp_finish - temp_start)

A = list(range(50,0,-1))

print('Matriz não ordenada = ', A)
print('Len = ', len(A))

temp_start = time.time()

for k in range(1000):
  for i in range(1,len(A)):
    temp = A[i]
    j = i - 1
    while j >= 0 and A[j] > temp:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = temp

temp_finish = time.time()

print('Matriz ordenada = ',A)
print('Tempo Execução = ', temp_finish - temp_start)

A = list(range(1,51))
random.shuffle(A)

print('Matriz não ordenada = ', A)
print('Len = ', len(A))

temp_start = time.time()

for k in range(1000):
  for i in range(1,len(A)):
    temp = A[i]
    j = i - 1
    while j >= 0 and A[j] > temp:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = temp

temp_finish = time.time()

print('Matriz ordenada = ',A)
print('Tempo Execução = ', temp_finish - temp_start)

A = list(range(1,101))

print('Matriz não ordenada = ', A)
print('Len = ', len(A))

temp_start = time.time()

for k in range(1000):
  for i in range(1,len(A)):
    temp = A[i]
    j = i -1
    while j >= 0 and A[j] > temp:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = temp

temp_finish = time.time()

print('Matriz ordenada = ',A)
print('Tempo Execução = ', temp_finish - temp_start)

A = list(range(100,0,-1))

print('Matriz não ordenada = ', A)
print('Len = ', len(A))

temp_start = time.time()

for k in range(1000):
  for i in range(1,len(A)):
    temp = A[i]
    j = i - 1
    while j >= 0 and A[j] > temp:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = temp

temp_finish = time.time()

print('Matriz ordenada = ',A)
print('Tempo Execução = ', temp_finish - temp_start)

A = list(range(1,101))
random.shuffle(A)

print('Matriz não ordenada = ', A)
print('Len = ', len(A))

temp_start = time.time()

for k in range(1000):
  for i in range(1,len(A)):
    temp = A[i]
    j = i - 1
    while j >= 0 and A[j] > temp:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = temp

temp_finish = time.time()

print('Matriz ordenada = ',A)
print('Tempo Execução = ', temp_finish - temp_start)