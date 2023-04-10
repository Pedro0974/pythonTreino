"""
Manipulando Data e Hora

Python tem um modulo built-in (integrado) para se
trabalhar com data e hora chamado datetime
"""

import datetime

print(dir(datetime))


# Now - Retorna a data e hora corrente

print(datetime.datetime.now())

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)

evento = datetime.datetime(2029, 1, 2, 0)

print(type(evento))

print(type('21/12/2028'))

print(evento)


nascimento = input('informe sua data de nascimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento.year)
print(nascimento.month)
print(nascimento.day)

