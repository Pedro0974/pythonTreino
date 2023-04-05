"""
Entendendo Iterators e Iterable

Iterator ->
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

"""


# Criando sua prorpia versao de loop

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('testando meu for')

