musicas = [
    {"Titulo": "Human", "Tocou": 30},
    {"Titulo": "Felina", "Tocou": 589},
    {"Titulo": "Coracao de Gelo", "Tocou": 600},
    {"Titulo": "Sweet child o mine", "Tocou": 12}
]

print(sorted(musicas, key=lambda musica: musica["Titulo"]))

print(f'\nMusica que mais tocou = ', max(musicas, key=lambda musica: musica['Tocou'])['Titulo'])

print(f'\nMusica que menos tocou = ', min(musicas, key=lambda musica: musica['Tocou'])['Titulo'])

# sem usar funções min, max e lambda

max = 0
for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == max:
        print(f'\n', musica['Titulo'])

min = 9999
for musica in musicas:
    if musica['Tocou'] < min:
        min = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == min:
        print(f'\n', musica['Titulo'])
