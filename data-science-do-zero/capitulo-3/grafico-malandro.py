from matplotlib import pyplot as plt

vezes_que_ouvi = [503, 507]
ano = [2021, 2022]

plt.bar(ano, vezes_que_ouvi, 0.6) #0.6 é a grossura, ano é o eixo x, vezes_que_ouvi eixo y
plt.xticks(ano) # o eixo x recebe o nome do ano

#Nomeando as legendas
plt.ylabel("Vezes que ouvi 'data science'") # Legenda eixo Y
plt.xlabel("Ano") #Legenda eixo X

#Setando onde começam as coordenadas do gráfico
plt.axis([2020.5, 2022.5, 502, 508]) #Coordenadas de onde o gráfico começa

# 

#Pode notar que é um gráfico malandro, pois não começa do 0, então mesmo a diferença sendo pouca passa uma impressão de grande diversidade.

#Consertando o gráfico:
plt.axis([2020.5, 2022.5, 0, 540])
plt.title("Gráfico não tão malandro")
plt.show()