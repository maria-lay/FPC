num_canos, tamanho_max = [int(i) for i in input().split()]
tamanho_canos = []  # tamanhos dos canos
valores_canos = []  # valores dos canos
for _ in range(num_canos):
    comp_cano, valor_cano = [int(i) for i in input().split()]
    tamanho_canos.append(comp_cano)
    valores_canos.append(valor_cano)

n_itens = len(tamanho_canos)  # tabela da prog dinâmica

T = [[0 for j in range(tamanho_max + 1)] for i in range(n_itens + 1)]  # caso base

for j in range(1, tamanho_max + 1):  # começa o range em 1 devido ao caso base

    for i in range(1, n_itens + 1):

        if tamanho_canos[i - 1] > j:
            T[i][j] = T[i - 1][j]
        else:
            cont = 0
            tamanho_add = 0
            while tamanho_add + tamanho_canos[i - 1] <= j:
                # cabe e precisa decidir
                # tira para colocar o novo ou fica com o que tinha
                tamanho_add += tamanho_canos[i - 1]
                cont += 1

            T[i][j] = max(T[i - 1][j], T[i - 1][j - tamanho_canos[i - 1] * cont] + valores_canos[i - 1] * cont)

print(T[n_itens][tamanho_max])