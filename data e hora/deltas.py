"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:23:34.912939
data_inicial = dd/mm/yyyy 15:33:34.123412

delta = data_final - data_inicial


"""

import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2024, 2, 5, 0)

tempo_para_aniversario = aniversario - data_hoje

print(tempo_para_aniversario)



