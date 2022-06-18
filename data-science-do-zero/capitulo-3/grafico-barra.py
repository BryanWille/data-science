from matplotlib import pyplot as plt

# One, Unforgiven, Enter Sandman, Fade to Black, Master Of Puppets

musicas = ["One", "Unforgiven", "Enter Sandman",
           "Fade to Black", "Master of Puppets"]
notas = [7, 9, 9, 9, 4]

# criando o gráfico de barra, onde x, y, alinhamento e cor
plt.bar(musicas, notas, align="center", color="red")

# adicionando um titulo
plt.title("Notas Músicas Metallica", size="x-large", fontweight="bold")

# fazendo os marcados de x e y
# coloca um eixo x em baixo plt.xlabel("Músicas Preferidas Metallica", size="x-large")
plt.ylabel("Minha nota", size="x-large")

# Porém como queremos colocar o eixo x como os nomes fazendo abaixo. onde vamos coloca a quantidade de repetição e o nome do vetor
plt.xticks(range(len(musicas)), musicas)

plt.show()