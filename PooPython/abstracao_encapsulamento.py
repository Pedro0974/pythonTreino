"""
POO - Abstração e Encapsulamento

o grande objetivo da POO é encapsular nosso codigo dentro de um grupo logico
e hierarquico utilizando classes.



"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')


# Testando classe
conta1 = Conta('Pedro', 12312, 32323)

conta1.depositar(100)

conta1.sacar(200)

print(conta1.__dict__)

