"""
POO - Metodos Magicos

Sao todos os metodos que utilizando dunder

dunder init -> __init__

dunder -> Duplo underscore

"""


class Livro:

    def __init__(self, titulo, autor, paginas ):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'


livro1 = Livro('Python', 'Pedro', 203423)

print(livro1)


