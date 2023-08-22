"""Exercício da perça perdida"""
# variáveis de entrada
n_pecas = int(input())
lista_entrada = [int(i) for i in input().split()]  # list comprehension


# função para somar os elementos da lista
def somar(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


# valor da lista total usando soma de gauss
soma_lista_total = int((1 + n_pecas) * n_pecas / 2)

resposta = soma_lista_total - somar(lista_entrada)
print(resposta)
