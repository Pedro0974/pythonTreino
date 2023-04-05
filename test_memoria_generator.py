"""
Teste de Memória com Generators

# Sequencia de Fibonacci
1, 2, 3, 5, 8, 13...

"""


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste
for n in fib_lista(100):
    print(n)


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 Geradores
for n in fib_gen(100):
    print(n)
