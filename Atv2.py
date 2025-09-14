class No:
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.proximo = None  # Referência para o próximo nó

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Primeiro elemento da lista
        self.tamanho = 0    # Quantidade de elementos na lista