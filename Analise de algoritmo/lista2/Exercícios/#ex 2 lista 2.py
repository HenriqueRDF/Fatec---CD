#ex 2 lista 2

import time

class Node:
    def __init__(self, bairro, esquerda=None, direita=None):
        self.bairro = bairro
        self.esquerda = esquerda
        self.direita = direita

class BinaryTree:
    def __init__(self):
        self.raiz = None

    def insert(self, bairro):
        if not self.raiz:
            self.raiz = Node(bairro)
        else:
            self._insert(self.raiz, bairro)

    def _insert(self, node, bairro):
        if bairro < node.bairro:
            if node.esquerda:
                self._insert(node.esquerda, bairro)
            else:
                node.esquerda = Node(bairro)
        else:
            if node.direita:
                self._insert(node.direita, bairro)
            else:
                node.direita = Node(bairro)

    def traverse(self):
        self._traverse(self.raiz)

    def _traverse(self, node):
        if node:
            self._traverse(node.esquerda)
            print(node.bairro)
            self._traverse(node.direita)

    def search(self, bairro):
        start_time = time.time()
        result = self._search(self.raiz, bairro)
        end_time = time.time()
        print(f"Tempo de busca para {bairro}: {end_time - start_time:.6f} segundos")
        return result

    def _search(self, node, bairro):
        if node:
            if node.bairro == bairro:
                return True
            elif bairro < node.bairro:
                return self._search(node.esquerda, bairro)
            else:
                return self._search(node.direita, bairro)
        return False

    def findHeight(self, node, x):
        if node is None:
            return -1
        if node.bairro == x:
            return 0
        leftHeight = self.findHeight(node.esquerda, x)
        rightHeight = self.findHeight(node.direita, x)
        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1

# Criar a árvore binária
arvore = BinaryTree()

# Inserir os bairros da cidade de Santos
bairros = ["Gonzaga", "Ponta da Praia", "Embaré", "Aparecida", "São Vicente", "Santos Centro", "Vila Mathias", "Vila Belmiro", "Boqueirão", "Campo Grande"]
for bairro in bairros:
    arvore.insert(bairro)

# Desenhar a árvore
print("Árvore binária:")
arvore.traverse()

# Executar o algoritmo de percurso dos nós
start_time = time.time()
arvore.traverse()
end_time = time.time()
print(f"Tempo de percurso: {end_time - start_time:.6f} segundos")

# Executar o algoritmo de pesquisa para cada um dos nós da árvore
for bairro in bairros:
    arvore.search(bairro)

# Verificar o quanto a altura "h" de cada nó influencia no tempo de busca
print("Influência da altura 'h' no tempo de busca:")
for bairro in bairros:
    altura = arvore.findHeight(arvore.raiz, bairro)
    print(f"Bairro: {bairro}, Altura: {altura}, Tempo de busca: {arvore.search(bairro)}")