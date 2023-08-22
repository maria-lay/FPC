"""Usando o problema da mochila"""
num_canos, tamanho_max = [int(i) for i in input().split()]
tamanho_canos = []  # tamanho do cano
valores_canos = []  # valores do cano
for _ in range(num_canos):
    comp_cano, valor_cano = [int(i) for i in input().split()]
    tamanho_canos.append(comp_cano)
    valores_canos.append(valor_cano)

n_itens = len(tamanho_canos)  # tabela da prog dinâmica

T = [[0 for j in range(tamanho_max + 1)] for i in range(n_itens + 1)]  # caso base

for j in range(1, tamanho_max + 1):  # começa o range em 1 devido ao caso base
    for i in range(1, n_itens + 1):
        if tamanho_canos[i - 1] > j:
            # não coube, volta para o anterior
            T[i][j] = T[i - 1][j]
        else:
            # cabe e precisa decidir
            # tira para colocar o novo ou fica com o que tinha
            T[i][j] = max(T[i - 1][j], T[i - 1][j - tamanho_canos[i - 1]] + valores_canos[i - 1])
print(T[n_itens][tamanho_max])
