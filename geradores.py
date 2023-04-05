"""
Geradores

- Geradores (Generators) são Iteradores (Iterators);

OBS: O contrario não é verdadeiro. OU seja, nem todo iterator é um generator.

Outras Informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palabra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions

- Funções {
    Utilizam return
    Retorna uma vez
    Quando executada, retorna um valor
}

- Generators Functions {
    Utilizam yield
    Podem Utilizar yield multiplas vezes
    Qaundo executada, retorna um generator
}
"""

# Exemplo Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
