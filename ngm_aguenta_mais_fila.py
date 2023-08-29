class No:
    def __init__(self, dado=None):
        self._dado = dado
        self._ant = None
        self._prox = None

    def __str__(self):
        return f"{self._dado}"


class lista:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def is_vazia(self):
        if self._inicio is None:
            return True
        return False

    def inserir_no_fim(self, dado=None):
        novono = No(dado)
        if self.is_vazia():
            self._inicio = self._fim = novono
        else:
            novono._ant = self._fim
            self._fim._prox = novono
            self._fim = novono

    def buscar(self, x):
        i = self._inicio
        while i is not None:
            if x == i._dado:
                break
            else:
                i = i._prox
        return i

    def remover_elemento(self, x):
        no_econtrado = self.buscar(x)
        if no_econtrado is not None:
            if no_econtrado._ant is not None:
                no_econtrado._ant._prox = no_econtrado._prox
            else:
                self._inicio = no_econtrado._prox

            if no_econtrado._prox is not None:
                no_econtrado._prox._ant = no_econtrado._ant
            else:
                self._fim = no_econtrado._ant

        return no_econtrado

    def remover_do_inicio(self):
        no = self._inicio
        if not self.is_vazia():
            if no._prox is None:
                self._fim = None
            else:
                no._prox._ant = None
            self._inicio = no._prox
        return no

    def __str__(self):
        s = ''
        i = self._inicio
        while i is not None:
            s += f"{str(i)}"
            i = i._prox
        return s


def main():
    n_pessoas = int(input())
    fila_inicial = [int(i) for i in input().split()]
    n_saidas = int(input())
    fora_fila = [int(i) for i in input().split()]
    fila = lista()

    for pessoa in fila_inicial:
        fila.inserir_no_fim(pessoa)

    def retirar_fila(fila_atual, saiu_fila):
        for pessoa in saiu_fila:
            fila_atual.remover_elemento(pessoa)
        fila_final = lista()

        while not fila_atual.is_vazia():
            x = fila_atual.remover_do_inicio()
            fila_final.inserir_no_fim(f'{x} ')
        return fila_final

    fila_final = retirar_fila(fila, fora_fila)
    print(fila_final)


if __name__ == '__main__':
    main()
