def ordenar_planos(lista, pacientes):
    planos = ['premium', 'diamante', 'ouro', 'prata', 'bronze', 'resto']
    for i in pacientes:
        plano = i[1]
        for j, k in enumerate(planos):
            if plano == k:
                lista[j].append(i)

    return lista


def ordenar_gravidade(lista):
    # Ordenar as sublistas internas do maior para o menor com base no terceiro elemento de cada sublista
    lista = [sorted(sublista, key=lambda x: x[2], reverse=True) if sublista else sublista for sublista in lista]
    return lista


# nao funcionaaaaaaa
def ordenar_alfabeto(lista):
    for i in range(len(lista)):
        plano = lista[i]
        for j in range(len(plano)):
            if plano[j][2] == plano[j - 1][2] and plano[j][0] > plano[j - 1][0]:
                plano[i][j], plano[i][j - 1] = plano[i][j - 1], plano[i][j]


def main():
    qtd_pacientes = int(input())
    pacientes = []  # [['maria', 'ouro', 999], ['nenio', 'ouro', 999], ['lay', 'ouro', 2], ['ennio', 'ouro', 9999]]
    lista_planos = [[] for _ in range(6)]

    for _ in range(qtd_pacientes):
        nome, plano, gravidade = input().split()
        gravidade = int(gravidade)
        pacientes.append([nome, plano, gravidade])

    lista_planos = ordenar_planos(lista_planos, pacientes)
    lista_ordenada = ordenar_gravidade(lista_planos)

    for i in range(len(lista_ordenada)):
        planos = lista_ordenada[i]
        if len(planos) > 0:
            for j in range(len(planos)):
                print(planos[j][0])

main()
