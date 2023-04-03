import random


def escolher_palavra():
    palavras = ['python', 'java', 'tailwindcss', 'javascript', 'django', 'css', 'html']
    return random.choice(palavras)


def pedir_letra():
    while True:
        letra = input("Digite uma letra: ")
        if len(letra) == 1 and letra.isalpha():
            return letra.lower()
        else:
            print("Digite apenas uma letra do alfabeto.")


class JogoDaForca:

    def __init__(self):
        self.palavra = escolher_palavra()
        self.palavra_oculta = self.esconder_palavra()
        self.tentativas = 6
        self.letras_erradas = []

    def esconder_palavra(self):
        return '_' * len(self.palavra)

    def verificar_letra(self, letra):
        if letra in self.palavra:
            for i in range(len(self.palavra)):
                if self.palavra[i] == letra:
                    self.palavra_oculta = self.palavra_oculta[:i] + letra + self.palavra_oculta[i + 1:]
            return True
        else:
            self.tentativas -= 1
            self.letras_erradas.append(letra)
            return False

    def verificar_fim_de_jogo(self):
        if self.palavra_oculta == self.palavra:
            print("Parabéns, você ganhou!")
            print(f"A palavra era {self.palavra}.")
            return True
        elif self.tentativas == 0:
            print("Você perdeu! :(")
            print(f"A palavra era {self.palavra}.")
            print(" _________     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      /|\   ")
            print(" |      / \   ")
            print(" |            ")
            print(f"Palavras erradas: {self.letras_erradas}")
            return True
        else:
            return False

    def jogar(self):
        while not self.verificar_fim_de_jogo():
            print(f"Palavra: {self.palavra_oculta}")
            print(f"Tentativas restantes: {self.tentativas}")
            letra = pedir_letra()
            if not self.verificar_letra(letra):
                print(f"A letra '{letra}' não está na palavra.")


jogo = JogoDaForca()
jogo.jogar()
