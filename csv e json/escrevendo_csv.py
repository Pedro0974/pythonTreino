"""
Escrevendo em arquivos CSV

writerow() -> escreve uma linha

"""

from csv import writer

with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input('informe nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracao: ')
            escritor_csv.writerow([filme, genero, duracao])
