"""
POO - Objetos

Objetos são instancias da classe
apos o mapeamento do objeto do mundo real para sua representação computacional
devemos poder criar quantos objetos forem necessarios
Podemos pensar nos objetos/instancias de um calsse como variaveis do tipo definido na classe
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostrar_cliete(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instancias/Objetos
lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar()

print(f'A lampada esta ligada? {lamp1.checa_lampada()}')

user1 = Usuario('Pedro', 'Lucas', 'asdfasdf@gmail.com', '12312')

cli1 = Cliente('Pedro', '091.123.123-12')

cc = ContaCorrente(5000, 20000, cli1)

cc.mostrar_cliete()

