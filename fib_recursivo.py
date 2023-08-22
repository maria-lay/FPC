# implementação de fibonacci recursivo

def fib_recursivo(n):
    if n <= 1:
        return 1
    return fib_recursivo(n-1) + fib_recursivo(n-2)


def main():
    print('-' * 65)
    num = int(input('Você quer saber a sequência de Fibonacci para qual número? '))
    print('-' * 65)
    print(fib_recursivo(num))


if __name__ == '__main__':
    main()
