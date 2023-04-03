prova1 = [29, 13, 10, 30, 28, 18]
prova2 = [30, 14, 9, 21, 19, 26]
alunos = ['Pedro', 'Victor D.', 'Luiz', 'Maycon', 'Victor A.', 'Marazzo']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(f'Maiores notas de cada aluno:\n', final)

# usando o map

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(f'\nMaiores notas de cada aluno com map:\n', dict(final))
