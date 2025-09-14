class No:
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.proximo = None  # Referência para o próximo nó

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Primeiro elemento da lista
        self.tamanho = 0    # Quantidade de elementos na lista

    def esta_vazia(self):
        return self.cabeca is None
    
    def adicionar_inicio(self, valor):
        novo_no = No(valor)    # Cria um novo nó
        novo_no.proximo = self.cabeca  # Novo nó aponta para a antiga cabeça
        self.cabeca = novo_no  # Cabeça agora aponta para o novo nó
        self.tamanho += 1      # Incrementa o tamanho da lista