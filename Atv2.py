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

    def adicionar_posicao(self, valor, posicao):
        if posicao <= 0:  # Se posição for menor ou igual a 0, adiciona no início
            self.adicionar_inicio(valor)
            return
        
        if posicao >= self.tamanho:  # Se posição for maior que o tamanho, adiciona no final
            self.adicionar_fim(valor)
            return
        
        novo_no = No(valor)
        atual = self.cabeca
        contador = 0
        
        # Navega até a posição anterior à desejada
        while contador < posicao - 1 and atual.proximo is not None:
            atual = atual.proximo
            contador += 1
        
        # Insere o novo nó na posição correta
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        self.tamanho += 1

    def adicionar_fim(self, valor):
        novo_no = No(valor)
        
        if self.esta_vazia():  # Se a lista estiver vazia
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            # Navega até o último elemento
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no  # Último elemento aponta para o novo nó
        
        self.tamanho += 1