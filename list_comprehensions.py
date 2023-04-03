# Importando o módulo statistics para calcular a mediana
import statistics

# Pedindo ao usuário para inserir uma lista de números separados por vírgulas
numeros = input("Insira uma lista de números separados por vírgulas: ")

# Convertendo a string de entrada em uma lista de floats
numeros = [float(x.strip()) for x in numeros.split(',')]

# Calculando a média usando list comprehension
media = sum(numeros) / len(numeros)

# Calculando a mediana usando a função median do módulo statistics
mediana = statistics.median(numeros)

# Calculando a variância usando list comprehension
variancia = sum((x - media) ** 2 for x in numeros) / len(numeros)

# Calculando o desvio padrão usando a raiz quadrada da variância
desvio_padrao = variancia ** 0.5

# Imprimindo os resultados
print("Média: {:.2f}".format(media))
print("Mediana: {:.2f}".format(mediana))
print("Variância: {:.2f}".format(variancia))
print("Desvio Padrão: {:.2f}".format(desvio_padrao))