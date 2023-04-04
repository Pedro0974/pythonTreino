"""
Sitema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer o uso do módulo os.

os -> Operating System - Sistema Operacional

"""

# Fazer o Import
import os

# getcwd() -> pega o current work directory - diretorio de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar de diretorio, podemos usar o chdir()

os.chdir('..') # volta um diretorio

print(os.getcwd())

# podemos checar se um diretorio é absoluto ou relativo

print(os.path.isabs('C:\\Desenvolvimento\\pythonTreino'))


