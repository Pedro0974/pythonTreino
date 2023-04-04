"""
Para ler arquivos usa-se a função in tergrada open()

# ao abrir um arquivo para leitura nao podemos realizar escrita nele

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o
caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/livrary/functions.html#open

# OBS: POr padrãoc a função open() abre o arquivo para leitura. Este arquivo deve existir, se não
teremos o erro FileNotFoundError


Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo
          ela recebe um parametro que indica onde colocar o cursor

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo
funcao open()

2 - Ler o arquivo
funcao read()

3 - Fechar o arquivo
funcao close()

"""

# Exemplo

arquivo = open('texto.txt')

# Para ler o conteúdo de um arquivo, após sua abertura
# devemos utilizar a função read()

print(arquivo.read())

# Movimentando o cursor pelo arquivo com afuncao seek()
arquivo.seek(20)

print(arquivo.read())

arquivo.close()

print(arquivo.closed)  # verifica se o arquivo esta aberto ou fechado e nos retorna um boolean

arquivo = open('texto.txt')

# readLine() -> funcao que le o arquivo linha por linha
print(arquivo.readline())

arquivo.close()


""" 
È utilizado o bloco "with" para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with 
"""
# Forma profissional para se trabalhar com arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)





