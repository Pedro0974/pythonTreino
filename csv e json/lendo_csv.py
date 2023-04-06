"""
Lendo arquivos CSV

CVS - Comma Separeted Values - Valores Separados por Vírgula

# Separador por Vírgula
1, 2, 3, 4, 5, 6

"pedro", "victor", "python"

# Separador por ponto e vírgula
1; 2; 3; 4; 5; 6

"pedro"; "victor"; "python"

# Separador por espaço
1 2 3 4 5 6

"pedro" "victor" "python"


"""
from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centimetros')
