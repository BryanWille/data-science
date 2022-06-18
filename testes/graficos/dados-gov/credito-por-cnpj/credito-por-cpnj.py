import pandas as pd
import numpy as np
from matplotlib import pyplot as pl

path = "C:/Users/bryan/OneDrive/Área de Trabalho/data-science/testes/graficos/credito-por-cnpj.csv"

arquivo = pd.read_csv(path, sep=";", decimal=",")
arquivo['data'] = pd.to_datetime(arquivo['data'], format='%d/%m/%Y')


data = arquivo["data"].to_numpy()
credito = arquivo["valor"].to_numpy()

pl.plot(data, credito)

pl.title("Crédito por Ano (CNPJ)", size="large")

pl.ylabel("Crédito em R$", size="large")
pl.xlabel("Ano", size="large")

pl.show()