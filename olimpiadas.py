def calcular_pontos(paises, modalidades):
    medalhas = [[0, 0, 0] for _ in range(paises)]

    for modalidade in modalidades:
        ouro, prata, bronze = modalidade
        medalhas[ouro - 1][0] += 1
        medalhas[prata - 1][1] += 1
        medalhas[bronze - 1][2] += 1

    classificacao = list(range(1, paises + 1))

    classificar(classificacao, medalhas)

    return classificacao


def classificar(classificacao, medalhas):
    n = len(classificacao)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if comparar_paises(classificacao[j], classificacao[max_idx], medalhas) < 0:
                max_idx = j
        classificacao[i], classificacao[max_idx] = classificacao[max_idx], classificacao[i]


def comparar_paises(pais_1, pais_2, medalhas):
    if medalhas[pais_1 - 1][0] != medalhas[pais_2 - 1][0]:
        return medalhas[pais_2 - 1][0] - medalhas[pais_1 - 1][0]

    if medalhas[pais_1 - 1][1] != medalhas[pais_2 - 1][1]:
        return medalhas[pais_2 - 1][1] - medalhas[pais_1 - 1][1]

    if medalhas[pais_1 - 1][2] != medalhas[pais_2 - 1][2]:
        return medalhas[pais_2 - 1][2] - medalhas[pais_1 - 1][2]

    return pais_1 - pais_2


ent_paises, ent_modalidades = map(int, input().split())
modalidades = [tuple(map(int, input().split())) for _ in range(ent_modalidades)]

classificacao_final = calcular_pontos(ent_paises, modalidades)

print(*classificacao_final)  # imprime a lista de classificação final separando por ''
