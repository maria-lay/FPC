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


class pilha(lista):
    def push(self, dado):
        novono = No(dado)
        if self.is_vazia():
            self._inicio = novono
            self._fim = novono
        else:
            novono._prox = self._inicio
            self._inicio._ant = novono
        self._inicio = novono

    def pop(self):
        return self.remover_do_inicio()

    def get_item(self):
        if self.is_vazia():
            return
        return self._inicio._dado


def verificar_se_definida(cadeia):
    expressoes = {'(': ')', '[': ']', '{': '}'}
    pilha_atual= pilha()
    if len(cadeia) % 2 == 1:
        return 'N'
    else:
        for i in range(len(cadeia)):
            elemento = cadeia[i]
            if elemento in expressoes.keys():
                pilha_atual.push(elemento)
            else:
                topo_pilha = pilha_atual.get_item()
                if topo_pilha is None:
                    return 'N'
                elif expressoes[topo_pilha] == elemento:
                    pilha_atual.pop()
                else:
                    return 'N'
        if pilha_atual.is_vazia():
            return 'S'


def main():
    instancias = int(input())

    for _ in range(instancias):
        cadeia = input()
        print(verificar_se_definida(cadeia))


if __name__ == '__main__':
    main()
