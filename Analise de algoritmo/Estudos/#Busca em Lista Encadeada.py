#Busca em Lista Encadeada

def buscar(L, k):
  # Inicializamos uma variável x com a lista L
  x = L
  # Percorremos a lista L até encontrar o elemento k
  for i in range(len(L)):
    if x[i][1] == k:
      # Quando encontramos o elemento k, retornamos a lista x, o elemento k e sua posição
      return x, x[i][1], i
  # Se não encontramos o elemento k, retornamos None
  return None