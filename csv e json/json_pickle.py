"""
JSON E PICKLE

JSON -> JavaScript Object Notation


"""

import jsonpickle

# ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])
#
# print(ret)


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


garfield = Gato('Garfield', 'De madame')

# ret = jsonpickle.encode(garfield)
#
# print(ret)

with open('garfield.json', 'w') as arquivo:
    ret = jsonpickle.encode(garfield)
    arquivo.write(ret)

with open('garfield.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(ret.nome)
    print(ret.raca)

