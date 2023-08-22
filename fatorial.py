# implementação de fatorial recursivo

def fatorial(n):
    if n <= 1:
        return n
    return n * fatorial(n-1)


def main():
    print('-' * 40)
    num = int(input("Você deseja o fatorial de qual número? "))
    print('-' * 40)
    print("O fatorial de {} é {}".format(num, fatorial(num)))


if __name__ == '__main__':
    main()
