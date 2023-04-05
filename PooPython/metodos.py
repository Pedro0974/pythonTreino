"""
POO - Mwtodos

- Metodos (funcoes) -> Representam os comportamentos do objeto. Ouseja, as ações que este objeto
pode realizar no seu sistema.

Em Pyhton, dividimos os metodos, em 2 grupos: Metodos de instancia e metodos de Classe.

# Metodos de Instancia


# O metodo construtor "__init__"

# Os metodos com duplo underline no inicio e duplo underline no final sao chamados de Metodos MAGICOS

# Nunca crie metodos proprios seus com duplo underline antes e depois do nome do metodo
"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos{cls.contador} usuario no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('Usuario Criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado!')

print(f'Senha User Criptografada: {user._Usuario__senha}')
