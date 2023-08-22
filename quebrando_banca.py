"""x_qtd_char, y_qtd_apagar = input().split()
￼saldo_entrada = input()"""

qtd_carac = 3
qtd_apagar = "1"
saldo_entrada = "408423492354057318235"
lista_entrada = []

for i in saldo_entrada:
    i = int(i)
    lista_entrada.append(i)

print(lista_entrada)

def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return lista


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1


lista_teste = mergesort(lista_entrada, 0, len(lista_entrada))
print(lista_teste)
