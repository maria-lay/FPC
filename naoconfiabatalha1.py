tabuleiro = []
navios = []
navios_encontrados = 0


# entradas do usuario
def main():
    linhas, colunas = map(int, input().split())
    for i in range(linhas):
        linha = list(input())
        tabuleiro.append(linha)

    encontrar_navio(linhas, colunas)
    num_disparos = int(input())
    for _ in range(num_disparos):
        l_disparo, c_disparo = map(int, input().split())
        navios_destruidos(l_disparo - 1, c_disparo - 1)

    qtd_destruidos = navios.count(0)
    print(qtd_destruidos)


# verifica se há navio nas coordenadas do usuario
def navios_destruidos(linhas, coluna):
    alvo = tabuleiro[linhas][coluna]
    if alvo != ".":
        navios[alvo] -= 1


# verifica onde tem um navio
def encontrar_navio(linhas, colunas):
    navios_encontrados = 0
    for n in range(len(tabuleiro)):
        for m in range(len(tabuleiro[0])):
            if tabuleiro[n][m] == "#":
                navios.append(0)
                tamanho(n, m, navios_encontrados, linhas, colunas)
                navios_encontrados += 1


# calcular o tamanho do navio
def tamanho(linha, coluna, navios_id, linhas, colunas):
    if tabuleiro[linha][coluna] == '#':
        tabuleiro[linha][coluna] = navios_id
        navios[navios_id] += 1

        # faz a verificação para os 4 pontos próximos da coordenada atual
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= linha + i < linhas and 0 <= coluna + j < colunas:
                tamanho(linha + i, coluna + j, navios_id, linhas, colunas)


main()
