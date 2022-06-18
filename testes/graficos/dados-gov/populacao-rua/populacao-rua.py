from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

path = "C:/Users/bryan/OneDrive/Área de Trabalho/data-science/testes/graficos/dados-gov/populacao-rua/data_set_poprua_cadunico-032022.csv"

df = pd.read_csv(path, delimiter=";")

quant_escolaridade = df.groupby(["GRAU_INSTRUCAO"]).size()
quant_por_escolaridade = quant_escolaridade.array
escolaridade = df.groupby(["GRAU_INSTRUCAO"])
escolaridade = escolaridade.groups.keys()

# df.groupby(['GRAU_INSTRUCAO']).sum().plot(kind='pie', subplots=True)

quant_formacao = []
for formacao in escolaridade:
    quant_formacao.append(formacao)

plt.pie(quant_por_escolaridade, labels=quant_formacao)

plt.title("Escolaridade por População de Rua de BH", weight="bold")

plt.show()

