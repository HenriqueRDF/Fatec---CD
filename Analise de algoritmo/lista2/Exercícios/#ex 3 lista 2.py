#ex 3 lista 2

import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def intercalacao(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

A = [6, 6, 7, 8, 0, 1, 5, 9]
B = [15, 22, 39, 44, 51, 55, 67, 83, 44, 50, 61, 72, 74, 83, 96, 98]

# Executar o algoritmo de ordenação por intercalação em A
start_time = time.time()
for _ in range(1000):  # Executar 1000 vezes para que o tempo seja quantificável
    intercalacao(A.copy())  # Copiar a lista A para não alterar a original
end_time = time.time()
print(f"Tempo de ordenação por intercalação em A: {end_time - start_time:.6f} segundos")

# Executar o algoritmo Merge-Sort em B
start_time = time.time()
for _ in range(1000):  # Executar 1000 vezes para que o tempo seja quantificável
    merge_sort(B.copy())  # Copiar a lista B para não alterar a original
end_time = time.time()
print(f"Tempo de ordenação por Merge-Sort em B: {end_time - start_time:.6f} segundos")