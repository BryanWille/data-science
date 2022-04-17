from collections import Counter
from tkinter.messagebox import NO
c = Counter([0, 1, 2, 3, 3, 4, 3, 9])
print(c)

# o counter mapeia uma lista ou tupla em algo parecido com um default dict de inteiro, colocando a chave em valores númericos
# e os elementos na ordem que aparecem na array, se elemento repetir ele repete o seu respectivo número no contador

document = ["ola", "ola", "um", "dois", "tres", "tres", "tres", "quatro", "metallica"]
word_counts = Counter(document)
# Maneira fácil de se usar o contador de palavras

print(word_counts)

# também existe um método no Counter que mostra as chaves mais comuns do dicionário, onde pode passar como arguemento o número do top comuns
for word, count in word_counts.most_common(10):
    print(word, count)

### CONJUNTOS ###

primos_abaixo_10 = {2, 3, 5, 7}


s = set()
s.add(1)  # s = {1}
s.add(2) # s = {1, 2}
s.add(2) # s = {!, 2}
x = len(s) # = 2
y = 2 in s # True
z = 3 in s # False

# O in é muito rapido em conjuntos, acha bem rápido, e em um conjunto não se repete uma chave 

stopwords_list = ["a", "an", "at"] + ["yet", "you"]

"zip" in stopwords_list # False, mas vai verificar todos os elementos da lista

stopwords_set = set(stopwords_list) #vai fazer um Conjunto de todos os elementos da lista
"zip" in stopwords_set # verificação muito mais rápido, dando False igual

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6
item_set = set(item_list) # vai criar um Conjunto de 3 itens
numero_itens_distintos = len(item_set) # 3
itens_distintos_lista = list(item_set) # [1, 2, 3]

### Fluxo de Controle ###

x = None
assert x == None #não recomendado
assert x is None # recomendado

#Página 29