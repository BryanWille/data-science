#importnato o plyplot do matplotlib

from matplotlib import pyplot as plt

#fazendo os eixos x e y de um gráfico

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]


#criando um grafinho de linhas, anos no eixo x, gdp no eixo y.

# plt.plot(eixo x, eixo y, cor, marcado, estilo de linha)
plt.plot(years, gdp, color='green', marker='o', linestyle="solid")

#adicionar o titulo
plt.title("PIB Nominal")

#adiciona um rotulo ao eixo y

plt.ylabel("Bilhões de Doláres")

# adiciona um rótulo ao eixo x
plt.xlabel("Décadas")

#abre a biblioteca
plt.show()