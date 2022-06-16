# As vezes precisamos unir duas listas, basta zipálas
lista1 = ['a', 'b', 'c']
lista2 = [3, 2, 1]
zipado = [x for x in zip(lista1, lista2)] #pega elemento por elemento na lista do zip
print(zipado)

# Porém se uma lista for maior que a outra, ele para na menor ex:
lista1 = ['a', 'b', 'c', 'd', 'e']
lista2 = [3, 2, 1]
zipado = [x for x in zip(lista1, lista2)] 
print(zipado)
# Acaba no 1, porque é a lista de menor elemento

#   Descompactar

pares = [('a', 3), ('b', 2), ('c', 1)] # pegamos a lista compactada (podia ser zipado tbm )
letras, numeros = zip(*pares)           # o asterico que executa a descompactação
# isso seria a mesma coisa que >
# letras, numeros = zip(('a', 3), ('b', 2), ('c', 1))
print(letras, numeros)

# A descompactação pode ser usada em qualquer função ex:

def soma(a, b): return a+b

soma(1, 2) # resultado 3
try:
    soma([1, 2]) #vai dar erro pois está sendo passado apenas um argumento
except TypeError: # se der erro (o que vai acontecer)
    print("Soma precisa de dois argumentos")
soma(*[1,2])
print(soma(*[1,2])) # ou seja descompacta a array para argumentos

#Dificilmente ocorre porém é quando usado é interessante