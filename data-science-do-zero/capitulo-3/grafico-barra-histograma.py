from matplotlib import pyplot as plt
from collections import Counter
# Importando a funçaõ Counter, que conta quantas vezes determinado elemento repete em uma lista.

# Criando uma lista das matérias.
array = [90, 70, 30, 23, 59, 39, 94, 44, 100, 57, 49,5]

# Agora vai dividir o numero por 10 e pegar a parte inteira:
# Ex 39 // 10 = 3 * 10 = 30, 90 é o limite, então vai fazer isso com todos os números
histograma = Counter(min(nota // 10 * 10, 90) for nota in array)
# o Counter por definição cria um dicionário. Com valores entre 90~0.


plt.bar([x + 5 for x in histograma.keys()], # Vai mover em 5 a legenda x, ou seja em vez de estar na metade (quando não poe nada), quando se coloca 5 vai pro inicio.
        histograma.values(), #Aqui seta os valores
        10, #Aqui coloca o tamanho de cada coluna
        edgecolor=(0,0,0)) #Aqui a cor do contorno da barra.

#plt.axis([xInicial, xFinal, yInicial, yFinal])
plt.axis([-5, 105, 0, 5]) #Seta os valores das colunas. basicamente liimita o tamanho em 5, e a largura de -5 a 105 para não encostar nas bordas.

#Colocar label de cada coluna
#opção 1:
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
#opção 2: (mais pythonica)
plt.xticks([x * 10 for x in range(11)])

plt.ylabel("N° de Estudantes") #Legenda de Y
plt.xlabel("Notas") #Legenda de X

plt.title("Distribuição de notas da 1° Avaliação") #Título

plt.show()
print(histograma)