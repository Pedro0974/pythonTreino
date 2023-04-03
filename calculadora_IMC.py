# pedindo os dados do usuario
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))


def calc_IMC():
    imc = peso / altura**2
    print(f'Seu IMC é: {imc}')

    if imc < 18.5:
        print('Voce esta abaixo do peso!')

    elif 18.5 <= imc < 25:
        print('Seu peso esta normal!')

    elif 25 <= imc < 30:
        print('Voce esta com sobrepeso!')

    elif 30 <= imc < 35:
        print('Voce esta com obesidade de grau 1!')

    elif 35 <= imc < 40:
        print('Voce esta com obesidade de grau 2!')

    else:
        print('Voce esta com obesidade de grau 3!')


calc_IMC()
