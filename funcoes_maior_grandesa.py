"""
Higher Order Functions - HOF
Funcoes de Maior Grandeza

o que significa?

- QUando uma linguagem de programação suporta HOF, indica que podemos
ter funcoes que retornam outras funcoes como resultado ou mesmo que podemos
passar funcoes como argumentos para outras funcoes, e até mesmo criar variaveis do tipo
funcoes nos nossos programas.


"""
from random import choice
# Exemplo - Definindo funcoes


def somar(a, b):
    return a + b


def subtrarir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funcoes

print(calcular(4, 3, somar))

print(calcular(4, 3, subtrarir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

# Nested Functions - Funcoes Aninhadas

"""
Em Python podemos tambem ter funções dentro de funcoes, que sao conhecidas por Nested Functions 
ou tambem Inner Functions( funcoes internas)
"""

# Exemplo


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce '))
    return humor() + pessoa


# Testando
print(cumprimento('Pedro'))

print(cumprimento('Victor'))

