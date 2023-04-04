"""
modos de abertura de arquivos com o open()

r -> Abre para leitura - modo padrao
w -> Abre para escrita - se ja existir um arquivo com o nome ele sobrescreve
x -> abre para criação exclusiva - falha se ja existir o arquivo
a -> abre para escrita e se ja existir escreve no final do arquivo
+ -> abre para o mode de atualização: Leitura e Escrita. Exemplo = (r+)
"""

try:
    with open('test.txt', 'x') as arquivo:
        arquivo.write('textando modo x.\n')
except FileExistsError:
    print('Arquivo ja existe')

# escrevendo em um arquivo ja existente sem apaga-lo
with open('produtos.txt', 'a') as arquivo:
    while True:
        produto = input('Informe o produto a ser adicionado ou digite sair: ')
        if produto != 'sair':
            arquivo.write(produto)
            arquivo.write('\n')
        else:
            break

