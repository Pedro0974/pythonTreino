"""
Escrevendo em arquivos

# ao abrir um arquivo para escrita nao podemos ler ele

Passos para escrever em arquivos:

1 - Abrir o arquivo usando a funcao open()
open('nome_do_arquivo.txt', 'w') usanmos o mode "w" para dizer que iremos escrever no arquivo

# OBS: Ao abrir um arquivo para escrita o arquivo é criado no SO, caso ele ja exista
# o arquivo anterior sera apagado e um novo sobrescrito e assim todo conteudo anterior será perdido

2 - Escrever no Arquivo usando funcao write()
write('mensagem a ser escrita no arquivo')

"""

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Ja estamos escrevendo no arquivo.\n')
    arquivo.write('Muito mais facil do que em outras linguagens.\n')
    arquivo.write('Ja podemos parar de escrever no arquivo.\n')


# exemplo recebendo dados do usario e escrevendo no arquivo

with open('produtos.txt', 'w') as arquivo:
    while True:
        produto = input('Informe o nome do produto ou digite sair: ')
        if produto != 'sair':
            arquivo.write(produto)
            arquivo.write('\n')
        else:
            break
