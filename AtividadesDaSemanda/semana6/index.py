
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")

        self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    def __str__(self):
        return f"Conta {self.numero} - Saldo: R$ {self.saldo:.2f}"


class ContaCorrente(Conta):
    def __init__(self, numero, saldo=0, limite=500):
        super().__init__(numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")

        if valor > self._saldo + self.limite:
            raise ValueError("Saldo e limite insuficientes.")

        self._saldo -= valor

    def __str__(self):
        return f"{super().__str__()} - Conta Corrente"


class ContaPoupanca(Conta):
    def __init__(self, numero, saldo=0, taxa=0.01):
        super().__init__(numero, saldo)
        self.taxa = taxa

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")

        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")

        self._saldo -= valor

    def aplicar_rendimento(self):
        self._saldo += self._saldo * self.taxa

    def __str__(self):
        return f"{super().__str__()} - Conta Poupança"


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"Cliente: {self.nome} - CPF: {self.cpf}"


clientes = []

for i in range(10):
    cliente = Cliente(f"Cliente {i + 1}", f"CPF{i + 1:08d}")

    if i % 2 == 0:
        conta = ContaCorrente(i + 1, 1000)
    else:
        conta = ContaPoupanca(i + 1, 1000)

    cliente.adicionar_conta(conta)
    clientes.append(cliente)

print("RELATÓRIO BANCÁRIO")
print("=" * 40)

for cliente in clientes:
    print(f"\n{cliente}")

    for conta in cliente.contas:
        try:
            conta.depositar(100)
            conta.sacar(50)

            if isinstance(conta, ContaPoupanca):
                conta.aplicar_rendimento()

            print(conta)

        except ValueError as erro:
            print(f"Erro: {erro}")

print("\nTESTE DE EXCEÇÃO")

try:
    clientes[0].contas[0].depositar(-100)
except ValueError as erro:
    print(erro)

print("\nTESTE DE POLIMORFISMO")

for cliente in clientes:
    for conta in cliente.contas:
        print(f"{cliente.nome}: {conta}")
