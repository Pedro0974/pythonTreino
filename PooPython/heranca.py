"""
POO - Herança (Inheritance)

A ideia de herança é de reaproveitar codigo. tambem extender nossas classes.

Obs: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e metodos da classe herdada

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;



# Sobrescrita de metodo (Overriding)

é quando reescrevemos um metodo da superclasse nas classes filhas
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'



