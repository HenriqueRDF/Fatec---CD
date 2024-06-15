import time

class Lista:
    def __init__(self, lista, inicio, chave):
        self.L = lista
        self.inicio = inicio
        self.anterior = lista[chave][0]
        self.proximo = lista[chave][4]
        self.dimensao = len(lista)
        self.chave = lista[chave]

def buscar(L, k):
    for i in range(len(L)):
        if L[i][1] == k:
            return L, L[i][1], i
    return None

def buscar_inserir(L, pos, novo):
    L.append(novo)
    for i in range(len(L) - 1, pos - 1, -1):
        L[i], L[i - 1] = L[i - 1], L[i]
    for i in range(1, len(L), 1):
        L[i][0] = i - 1
    for i in range(0, len(L) - 1, 1):
        L[i][4] = i + 1
    return L

def delete(L, k):
    L.pop(k)
    for i in range(1, len(L), 1):
        L[i][0] = i - 1
    for i in range(0, len(L) - 1, 1):
        L[i][4] = i + 1
    return L

L = [[0, 1, 'João Silva', 4500.0, 1],[1, 2, 'Maria Oliveira', 5200.0, 2],[2, 3, 'Carlos Pereira', 4800.0, 3],[3, 4, 'Ana Souza', 5300.0, 4],[4, 5, 'Pedro Costa', 4600.0, 5],[5, 6, 'Fernanda Lima', 4700.0, 6],[6, 7, 'Rafael Almeida', 5100.0, 7],[7, 8, 'Juliana Martins', 4900.0, 8],[8, 9, 'Roberto Gonçalves', 5500.0, 9],[9, 10, 'Patricia Ferreira', 5000.0, 10]]

ele = [10, 11, 'Dor e Sofrimento', '9999.9', 12]

x, chave, pos_chave = buscar(L, 5)
lista = Lista(L, L[0], pos_chave)

print('L padrão: ',x,'\n')

L_novo = buscar_inserir(L, pos_chave, ele)
lista = Lista(L, L[0], pos_chave)
print('L Insert: ',L_novo,'\n')

L_novo = delete(L, 5)
lista = Lista(L, L[0], pos_chave)
print('L Delete: ',L_novo,'\n')

for i in range(len(L)):
    srt = time.time()
    for j in range(100000):
        x, chave, pos_chave = buscar(L, 5)
        lista = Lista(L, L[i], pos_chave)
    fnl = time.time()
    print(f'Tempo de processo da chave {i}: ', fnl-srt)