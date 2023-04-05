"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos nos conseguimos
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributps de instância;
    - Atributps de classe;
    - Atributps dinamica;

# Atributos de instancia: sõa atributos declarados do metodo construtor.

# OBS: metodo construtor: é um metodo especial utilizado para a construção do objeto.

Em Python por convenção ficou estabelecido que todos os atributos de uma classe é publico
ou seja, pode ser acessado em todas as partes do projeto
caso queira demostrar que ele deve ser tratado como privado, adicionado duplo underscore " __ "
antes do atributo

# Atributos de instancia, cria instancias/objetos de uma classe, todas as instancias terao estes atributos


# Atributos de classes sao atributos que sao declarados diretamente na classe
fora do contrutor. Geralmente ja inicializamos um valor, e ete valor é compartilhado entre
todas as instancias da classe. ou seja, ao invez de cada instancia da classe ter seus
proprios valores como é o caso dos atributos de instancia
com os atributos de classe todas as instancias terao o mesmo valor para este atributo


# Atributos Dinamicos é um atributo de instancia qu epode ser criado em tempo de execução 

"""
# classes com atributos publicos


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha


# classe com atributo privado
# OBS: lembrando que é apenas uma convenção, ou seja
# o python permite o acesso de qualquer atributo


class Produto:
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id
