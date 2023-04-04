"""
ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional
o software precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever no arquivo.

StringIO -> utilizado para ler e criar arquivos em memória.
    Ou seja, não vai gravar no disco, apenas na memoria

"""

# primeiro fazemos o import

from io import StringIO

mensagem = 'Esse é apenas um teste'

# Podemos criar um arquivo em memória ja com uma string inserida
# ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# agora tendo o arquivo, podemos utilizar tudo que ja sabemos



