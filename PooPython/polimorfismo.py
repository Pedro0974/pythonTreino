"""
POO - Polimorfismo

Poli - muitas
Morfis - formas


"""
from abc import ABC


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este metodo')

    def comer(self):
        print(f'{self.__nome} esta comendo...')


class Cachorro(Animal, ABC):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal, ABC):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Miau')


class Rato(Animal, ABC):

    def __init__(self, nome):
        super().__init__(nome)