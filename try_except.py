"""
Sintaxe

try:
    // execução problematica
except:
    // o que deve ser feito em caso de problema
"""

try:
    len(5)
except TypeError as err:
    print(f'deu ruim aqui. {err}')

# try tenta executar a função len, se nao conseguir o except volta uma resposta
