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

    def remover_valor(self, valor):
        if self.esta_vazia():  # Se a lista estiver vazia
            return False
        
        # Caso especial: remover a cabeça
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return True
        
        atual = self.cabeca
        # Procura o valor a ser removido
        while atual.proximo is not None:
            if atual.proximo.valor == valor:
                atual.proximo = atual.proximo.proximo  # Remove o nó
                self.tamanho -= 1
                return True
            atual = atual.proximo
        
        return False  # Valor não encontrado
    
    def imprimir(self):
        if self.esta_vazia():
            print("Lista vazia")
            return
        
        elementos = []
        atual = self.cabeca
        # Coleta todos os valores da lista
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        
        print(" ".join(elementos))  # Imprime os valores separados por espaço

    def inicializar_com_lista(self, valores):
        """Inicializa a lista com uma lista de valores"""
        # Adiciona os valores na ordem inversa para manter a ordem correta
        for valor in reversed(valores):
            self.adicionar_inicio(valor)

def processar_arquivo(nome_arquivo):
    lista = ListaEncadeada()  # Cria uma nova lista vazia
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            
            # Primeira linha: inicialização da lista
            linha_inicial = linhas[0].strip()
            if linha_inicial:
                # Converte os valores para inteiro
                valores_iniciais = list(map(int, linha_inicial.split()))
                lista.inicializar_com_lista(valores_iniciais)
            
            # Segunda linha: quantidade de ações
            if len(linhas) > 1:
                qtd_acoes = int(linhas[1].strip())
            else:
                qtd_acoes = 0
            
            # Processar as ações
            for i in range(2, 2 + qtd_acoes):
                if i < len(linhas):
                    linha = linhas[i].strip()
                    if linha:
                        partes = linha.split()  # Divide a linha em partes
                        acao = partes[0].upper()  # Ação (A, R ou P)
                        
                        if acao == 'A':  # Adicionar
                            if len(partes) >= 3:
                                valor = int(partes[1])
                                posicao = int(partes[2])
                                lista.adicionar_posicao(valor, posicao)
                        
                        elif acao == 'R':  # Remover
                            if len(partes) >= 2:
                                valor = int(partes[1])
                                lista.remover_valor(valor)
                        
                        elif acao == 'P':  # Imprimir
                            lista.imprimir()
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
    
    return lista