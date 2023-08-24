movimento = {'N': ['O', 'L'], 'L': ['N', 'S'], 'S': ['L', 'O'], 'O': ['S', 'N']}

while True:
    linhas, colunas, qtd_instrucao = [int(i) for i in input().split()]

    if linhas == 0 and colunas == 0 and qtd_instrucao == 0:
        break

    var_auxiliar = 0
    direcao = ''
    arena = []
    direcoes = ['N', 'S', 'O', 'L']
    pos_lin = None
    pos_col = None
    orientacao = None

    for l in range(0, linhas):
        linha = input()
        if var_auxiliar == 0 and any(direc in linha for direc in direcoes):
            pos_col = [linha.find(direc) for direc in direcoes]
            pos_lin = l
            for num in range(0, len(pos_col)):
                if pos_col[num] != -1:
                    orientacao = direcoes[num]
                    pos_col = pos_col[num]
                    break
            var_auxiliar = 1
        arena.append(linha)

    instrucoes = input()
    pontuacao = 0

    for letra in instrucoes:
        if letra == 'D':
            orientacao = movimento[orientacao][1]
        elif letra == 'E':
            orientacao = movimento[orientacao][0]
        else:
            if orientacao == 'N' and pos_lin > 0:
                if arena[pos_lin - 1][pos_col] == '#':
                    pass
                else:
                    pos_lin -= 1
            elif orientacao == 'L' and pos_col < colunas - 1:
                if arena[pos_lin][pos_col + 1] == '#':
                    pass
                else:
                    pos_col += 1
            elif orientacao == 'S' and pos_lin < linhas - 1:
                if arena[pos_lin + 1][pos_col] == '#':
                    pass
                else:
                    pos_lin += 1
            elif orientacao == 'O' and pos_col > 0:
                if arena[pos_lin][pos_col - 1] == '#':
                    pass
                else:
                    pos_col -= 1

            if arena[pos_lin][pos_col] == '*':
                pontuacao += 1
                i = pos_col
                arena[pos_lin] = arena[pos_lin][0:i] + '.' + arena[pos_lin][i + 1:]

    print(pontuacao)
