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


while True:
    notacao = input().split()
    pilha_atual = pilha()
    operadores = ['+', '-', '*', '/']
    if not notacao:
        break

    def desempilhar_2_operandos(pilha):
        operando_1 = int(pilha.get_item())
        pilha_atual.pop()
        operando_2 = int(pilha.get_item())
        pilha_atual.pop()

        return operando_1, operando_2

    # / + - 837 35 - 332 124 - - 260 605 - 751 463
    for i in range(-1, -len(notacao) - 1, -1):
        token = notacao[i]
        if token == '+':
            operando_1, operando_2 = desempilhar_2_operandos(pilha_atual)
            novo_token = operando_1 + operando_2
            pilha_atual.push(novo_token)
        elif token == '-':
            operando_1, operando_2 = desempilhar_2_operandos(pilha_atual)
            novo_token = operando_1 - operando_2
            pilha_atual.push(novo_token)
        elif token == '*':
            operando_1, operando_2 = desempilhar_2_operandos(pilha_atual)
            novo_token = operando_1 * operando_2
            pilha_atual.push(novo_token)
        elif token == '/':
            operando_1, operando_2 = desempilhar_2_operandos(pilha_atual)
            novo_token = int(operando_1 / operando_2)
            pilha_atual.push(novo_token)
        else:
            pilha_atual.push(token)

    print(pilha_atual.get_item())
