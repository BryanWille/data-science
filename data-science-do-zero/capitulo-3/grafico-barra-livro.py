from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

#plote as barras com coordenadas x a esqeurda, alturas
plt.bar(range(len(movies)), num_oscars)

plt.title("Meus Filmes favoritos")
plt.ylabel("# of Academy Awards")

#rotule o eixo x com os nomes dos filmes no centro das barras
plt.xticks(range(len(movies)), movies)
plt.show()