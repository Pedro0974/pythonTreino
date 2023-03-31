while True:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    opcao = int(input('Digite a operação a ser realizada!\n1 - Soma\n2 '
                      '- Subtração\n3 - Multiplicação\n4 - Divisão\n'))

    if opcao == 1:
        soma = num1 + num2
        print(f'O resultado da soma é: {soma}')
    elif opcao == 2:
        subtracao = num1 - num2
        print(f'O resultado da subtração é: {subtracao}')
    elif opcao == 3:
        multiplicacao = num1 * num2
        print(f'O resultado da multiplicação é: {multiplicacao}')
    elif opcao == 4:
        if num2 == 0:
            print('Não é possível dividir por zero!')
        else:
            divisao = num1 / num2
            print(f'O resultado da divisão é: {divisao}')
    else:
        print('Opção inválida. Tente novamente.')
