# entradas do usuario
num_pilhas = int(input())
pilhas = [int(i) for i in input().split()]

# calculo do inicio da sequencia
base = (num_pilhas*(num_pilhas + 1))/2  # formula
total_pedras = int()  # total de pedras
for pilha in pilhas:
    total_pedras += pilha

sobra = int(total_pedras - base)
inicio = int((total_pedras - base) / num_pilhas)

if sobra % num_pilhas != 0:  # calcula se é possível transformar em escada perfeita
    print('-1')
else:  # calcula a quantidade de movimentos necessários
    n_movimentos = 0
    for i, coluna in enumerate(pilhas):
        if coluna > (inicio + i + 1):
            n_movimentos += coluna - (inicio + i + 1)
    print(n_movimentos)
