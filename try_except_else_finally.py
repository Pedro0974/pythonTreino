"""
TODA ENTRADA DEVE SER TRATADA
"""

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor Incorreto')
else:
    print(f'Voce digitou {num}')
