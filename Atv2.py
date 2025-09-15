import sys 
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def esta_vazia(self):
        return self.cabeca is None
    
    def adicionar_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.tamanho += 1
    
    def adicionar_posicao(self, valor, posicao):
        if posicao <= 0:
            self.adicionar_inicio(valor)
            return
        
        if posicao >= self.tamanho:
            self.adicionar_fim(valor)
            return
        
        novo_no = No(valor)
        atual = self.cabeca
        contador = 0
        
        # Navegar até a posição anterior à desejada
        while contador < posicao - 1 and atual.proximo is not None:
            atual = atual.proximo
            contador += 1
        
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        self.tamanho += 1
    
    def adicionar_fim(self, valor):
        novo_no = No(valor)
        
        if self.esta_vazia():
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        
        self.tamanho += 1
    
    def remover_valor(self, valor):
        if self.esta_vazia():
            return False
        
        # Caso especial: remover a cabeça
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return True
        
        atual = self.cabeca
        while atual.proximo is not None:
            if atual.proximo.valor == valor:
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return True
            atual = atual.proximo
        
        return False
    
    def imprimir(self):
        if self.esta_vazia():
            print("Lista vazia")
            return
        
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        
        print(" ".join(elementos))
    
    def inicializar_com_lista(self, valores):
        """Inicializa a lista com uma lista de valores"""
        for valor in reversed(valores):
            self.adicionar_inicio(valor)

def processar_arquivo(nome_arquivo):
    lista = ListaEncadeada()
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            cont_print = 0
            # Primeira linha: inicialização da lista
            linha_inicial = linhas[0].strip()
            if linha_inicial:
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
                    linha = linhas[i].strip() #remove espaços em branco ou caracteres especificados do início e do fim de uma string.
                    if linha:
                        partes = linha.split() #divide uma string em uma lista de substrings usando um delimitador.
                        acao = partes[0].upper() #converte todos os caracteres de uma string para maiúsculas. 
                        
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
                            cont_print += 1
                            print (f"Lista {cont_print}: ")
                            lista.imprimir()
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
    
    return lista

# Exemplo de uso
if __name__ == "__main__":
    
    if len(sys.argv) <= 1:
        print
        exit(-1)  
    
    nome_arquivo = sys.argv[1]
    
    # Processar o arquivo
    lista_resultante = processar_arquivo(nome_arquivo)
    
    print("Lista final:")
    lista_resultante.imprimir()
