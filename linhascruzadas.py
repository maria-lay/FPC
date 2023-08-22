# entradas do usuario
vertical = int(input())
horizontal = list(map(int, input().split()))


# contagem dos cruzamentos
def cont_cruzamentos(ord_horizontal):
    cruzamentos = 0

    for i in range(len(ord_horizontal)):
        for j in range(i):
            if ord_horizontal[j] > ord_horizontal[i]:
                cruzamentos += 1

    return cruzamentos


print(cont_cruzamentos(horizontal))
