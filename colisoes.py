""" Exercício das colisões """
# definindo as variaveis de entrada com list comprehension
X0A, Y0A, X1A, Y1A = [int(i) for i in input().split()]
X0B, Y0B, X1B, Y1B = [int(i) for i in input().split()]

# verificando se eles não colidem
if X1A < X0B or X0A > X1B or Y1A < Y0B or Y0A > Y1B:  # testando para o eixo X e Y
    print("0")
else:
    print("1")
