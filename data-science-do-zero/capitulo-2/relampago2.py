from cgitb import small
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

#Boolenas em Python são True e False

# None == null

# assert funciona como um conferidor de código, caso a condição do assert não seja verdadeira ele vai lançar um erro

a = 2

# assert a > 4 AssertionError
assert a < 4

x = None
assert x == None # não é uma boa escrita
assert x is None # é uma boa escrita

# Falsy e Truthy 

# false são valores que não servem para testes lógicos, porque de uma vez vão ser falsos
# Truthy vão ser valores que vão servir para testes lógicos porque são verdadeiros ex

def uma_funcao_que_retorna_string():
    return None
    # return "Hello"

s = uma_funcao_que_retorna_string()

if s:
    primeiro_char = s[0]
else:
    primeiro_char = "None"
    
print(primeiro_char)

#forma breve e complexa
primeiro_char = s and s[0]

#and retorna um segundo valor quando o primeiro é Truthy e o primeiro quando ele não é, por isso x deve ser um número ou None

safe_x = x or 0
print(safe_x)

#x = 2

safe_x = x if x is not None else 0
print(safe_x)


#logo se pode usar diretamente o if para procurar listas, strings, dicionarios vazios...


# funções any e all
#any retorna true se pelo menos um valor é verdadeiro

x = any([2, 3, 1]) # True
y = any([False, None, 1]) # True
z = any([False, None, 0]) # False
print(x, y, z)

# all retorna True somente se todas forem verdadeiras

x = all([2, 3, 1]) # True
y = all([False, None, 1]) # False
z = all([False, None, 0]) # False
print(x, y, z)

### SORT ###
#todo método tem o sort e o sorted

#sort organiza no próprio método
x = [2, 1, 9, 33, 12, 310, 10]
x.sort()
print(x)

# sorted organiza em outro método

y = [2, 1, 1, 3, 2, 3, 1, 2]
z = sorted(y)
print(z)

#reverso é só usar o parametro reversed=true

z = sorted(y, reverse=True)
print(z)

# Compreensão de Listas / Transformar uma lista em outra diretamente

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num_par = [num for num in range(5) if num % 2 == 0]

# coloca-se um for para percorrer os 5 primeiros digitos de num, se esse for par então coloca-se no vetor

print(num_par)

quadrados = [num * num for num in range(10)]
print(quadrados)
# num * num (quadrado) para cada numero de 0 a 10

quadrados_pares = [num * num for num in num_par]
# num * num para todos numeros em num_par

print(quadrados_pares)

#Também podemos usar essa construção na hora de criar um dicionário

dict_quadrados = {num: num * 2 for num in num} # chave num vai receber significado num * num

print(dict_quadrados)

set_quadrados = {num * num for num in [1, -1]} # {1}

print(set_quadrados)

# Quando não se precisa do valor, mas somente da chave podemos usar o underline

zeros = [0 for _ in num_par]

print(zeros)

#Uma compreensão de lista pode conter multiplos fors

pairs = [(num, num_par)
            for num in range(10)
            for num_par in range(num+1, 10)]

print(pairs)

#Assert são feitos para testar o código

assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 devia ser igual a 2"

def menor_item(xs):
    return min(xs)

assert menor_item([10, 20, 5, 40]) == 5, "Não é o menor número"
assert menor_item([1, 0, -1, 2]) == -1

