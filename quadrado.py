tamanho = int(input())  # 3
entrada_matriz = []  # [[3, 6, 6], [8, 6, 7], [4, 3, 8]]
lista_num = []
for i in range(tamanho):
    lista_num = [int(i) for i in input().split()]
    entrada_matriz.append(lista_num)


# função para somar as colunas da matriz
def somar_colunas_matriz(lista, tamanho_quadrado):
    somas = []
    for j in range(tamanho_quadrado):
        m = 0
        for k in range(tamanho_quadrado):
            m += lista[k][j]
        somas.append(m)
    return somas


# função para somar as linhas da matriz
def somar_linhas_matriz(lista, tamanho_quadrado):
    somas = []
    for j in range(tamanho_quadrado):
        m = 0
        for k in range(tamanho_quadrado):
            m += lista[j][k]
        somas.append(m)
    return somas


# função para procurar a soma errada
def procurar_diferente(lista):
    diferente_idx = 0
    for j in range(len(lista)):
        if lista[j - 2] == lista[j - 1] and lista[j - 2] == lista[j]:
            pass  # todos sao iguais
        elif lista[j - 2] == lista[j - 1] and lista[j - 2] != lista[j]:
            diferente_idx = j
        elif lista[j - 2] == lista[j] and lista[j - 2] != lista[j - 1]:
            diferente_idx = j - 1
        elif lista[j] == lista[j - 1] and lista[j] != lista[j - 2]:
            diferente_idx = j - 2

    return diferente_idx


# definindo listas de soma
somas_linhas = somar_linhas_matriz(entrada_matriz, tamanho)
somas_colunas = somar_colunas_matriz(entrada_matriz, tamanho)
# obtendo o indice do numero errado
linha_idx = procurar_diferente(somas_linhas)
coluna_idx = procurar_diferente(somas_colunas)
# obtendo o numero errado a partir da matriz de entrada
numero_errado = entrada_matriz[linha_idx][coluna_idx]
# calculando o numero certo a partir dos valores obtidos
numero_certo = numero_errado - (somas_linhas[linha_idx] - somas_linhas[linha_idx - 1])
print("{} {}".format(numero_errado, numero_certo))
