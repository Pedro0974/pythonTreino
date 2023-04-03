# Lançando alerta de erro com a função do python Raise

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


# Exemplo sem erro
colore('Pedro', 'azul')

# Exemplo com erro
colore('Victor A.', 'preto')

# OBS: O raise, assim como return, finaliza a função.
