"""
Decoradores

o que sao deorators?

- Decorator sao funções
- decorators envolvem outras funções e aprimoram seus comportamentos;
- decorators tambem sao exempos de HOF
- decorators te uma sintaxe propria, usando @


"""

# decorators como funções


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('foi um prazer conhecer voce')
        funcao()
        print('tenha um exelente dia')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando

apresentando()



