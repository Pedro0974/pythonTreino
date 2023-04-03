musicas = [
    {"Titulo": "Human", "Tocou": 30},
    {"Titulo": "Felina", "Tocou": 589},
    {"Titulo": "Coracao de Gelo", "Tocou": 600},
    {"Titulo": "Sweet child o mine", "Tocou": 12}
]

print(sorted(musicas, key=lambda musica: musica["Titulo"]))

print(f'Musica que mais tocou =', max(musicas, key=lambda musica: musica['Tocou']))

print(f'Musica que menos tocou =', min(musicas, key=lambda musica: musica['Tocou']))

