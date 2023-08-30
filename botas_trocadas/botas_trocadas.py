def contar_pares(botas):
    n_pares = 0
    for bota in botas:
        pares = min(botas[bota]['D'], botas[bota]['E'])
        n_pares += pares

    return n_pares


def main():
    n_botas = int(input())
    botas = {}
    for i in range(n_botas):
        bota, lado = input().split()

        # para cada bota adicionada vai fazer verificações
        if botas.get(bota):  # a bota existe no dicionário
            botas[bota][lado] += 1
        else:  # não tá no dicionário
            botas[bota] = {'D': 0, 'E': 0}
            botas[bota][lado] += 1

    print(contar_pares(botas))


if __name__ == '__main__':
    main()
