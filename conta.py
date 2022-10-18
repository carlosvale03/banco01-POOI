import datetime

class Conta:
    num_contas = 0

    def __init__(self, num, titular, saldo=0):
        self._num = num
        self._titular = titular
        self._saldo = saldo
        self._historico = Historico()
        Conta.num_contas += 1

    @property
    def numero(self):
        return self._num

    @property
    def titular_nome(self):
        return self._titular.nome

    @property
    def titular_sobrenome(self):
        return self._titular.sobrenome

    @property
    def titular_cpf(self):
        return self._titular.cpf

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self):
        self._historico = Historico

    def sacar(self, valor):
        if valor <= self._saldo and valor >= 0.1:
            self._saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        if valor >= 0.1:
            self._saldo += valor
            return True
        else:
            return False

    def listar(self):
        print('==' * 30)
        print(f'O titular da conta é: {self.titular_nome} {self.titular_sobrenome}')
        print(f'O CPF do titular é: {self.titular_cpf}')
        print(f'O número da conta é: {self._num}')
        print(f'Saldo na conta: {self._saldo:0.2f}')
        print('==' * 30)

    def exibir(self):
        self._historico.imprime()


class Cliente:
    def __init__(self, nome, sNome, doc):
        self._cliente = nome
        self._sNome = sNome
        self._cpf = doc
    
    @property
    def nome(self):
        return self._cliente

    @property
    def sobrenome(self):
        return self._sNome

    @property
    def cpf(self):
        return self._cpf


class Historico:
    def __init__(self):
        self._data_criacao = datetime.datetime.now()
        self._transacoes = list()

    @property
    def data_criacao(self):
        return self._data_criacao

    @property
    def transacoes(self):
        return self._transacoes

    def add_transacoes(self, t):
        self._transacoes.append(t)

    def imprime(self):
        print(f'Data de criação da conta: {self._data_criacao}')
        for i in self._transacoes:
            print(i)