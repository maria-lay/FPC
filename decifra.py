# leitura da entrada do usuario
seq_cripto = input()  # "zcbedfghljkinmypqrutsvwxoa"
frase_cripto = input()  # "bzedzeymziluz"

alfabeto = "abcdefghijklmnopqrstuvwxyz"
dicio_descriptografado = dict()

# dicionário descriptografando a permutação inicial
for i in range(len(alfabeto)):
    dicio_descriptografado[seq_cripto[i]] = alfabeto[i]


# retorna o valor do dicionário para cada letra na frase criptografada
def descriptografar(dicio, frase_criptografada):
    frase = str()
    for j in frase_criptografada:
        frase = frase + dicio[j]
    return frase


print(descriptografar(dicio_descriptografado, frase_cripto))
