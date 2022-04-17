from email.policy import default
from lib2to3.pgen2 import grammar
from multiprocessing.spawn import old_main_modules
from telnetlib import WONT


dois = (lambda x : 2 * x) # função lambda
print(dois)
quatro = dois(2)
print(quatro)

# argumentos padrão
def printar(ola = "Hello, World"):
    print(ola)

printar("Teste")
printar()
# Define um valor padrão para ola, algo parecido com uma sobrecarga em POO

#um exemplo de como pode ser aplicado

def nome_completo(primeiro = "O-primeiro-nome", ultimo = "Alguma-coisa"):
    return primeiro + " " + ultimo

print(nome_completo("Bryan", "Wille"))
print(nome_completo("Bryan"))
print(nome_completo(ultimo="Wille"))

"""
    Comentário em múltiplas linhas, ou string
    de várias linhas.

"""

#F-String
quatro = 5
print(f"Olá {quatro}")
# ou também

primeiro = "Bryan"
segundo = "Wille"
nome1 = primeiro + " " + segundo
# ou
nome2 = "{0} {1}".format(primeiro, segundo)
nome3 = f"{primeiro} {segundo}"

#Exceções, capturar exceções como no Java com o Try Catch
try:
    print(0/0)
except ZeroDivisionError:
    print("Não foi possível dividir por zero")

#lista
#existe a possibilidade de fazer uma lista de um mix de tipos
#e também uma lista de número


teste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(teste[-2]) # penúltimo
print(teste[-1]) # último
#quando se coloca o índice negativo começa na lista os ultimos

# fatiar
primeiros_tres = teste[0:3]
print(primeiros_tres)
tres_pra_frente = teste[3:]
print(tres_pra_frente)
sem_primeiro_e_ultimo = teste[1: -1]
print(sem_primeiro_e_ultimo)

# a cada sequencia
a_cada_tres = teste[::3]
print(a_cada_tres)
ordem_reversa = teste[::-1]
print(ordem_reversa)

# verificar se tal numero está na lista
print(-1 in teste) # false
print(0 in teste) # true
# ATENÇÃO VERIFICA TODOS OS ELEMENTOS DA LISTA TENDO UM TEMPO DE EXECUÇÃO NÃO TÃO BOM


#concatenar listas
x = [1, 2, 3]
x_mais_quatro = [5, 6, 7]
x.extend(x_mais_quatro)
print(x)

# ou se não quiser modificar

y = x + x_mais_quatro
print(y) # no caso colocou dois x_mais_quatro por conta de já ter sido incrementado no x passado

x = [1, 2, 3]
x.append (0) # vai pro final da lista
print(x)

# DESCOMPACTAR A LISTA
um, dois, tres = [11, 22, 33] # um = 11, dois = 22, tres = 33
print(f"{um} + {dois} + {tres}") 

# _ underline é usado para desconsiderar um valor como no caso acima

_, y = [1, 2];


# Tuplas são especies de listas que não podem ser alteradas
minha_lista = [1, 2, 3]
minha_lista[1] = 3 # [1, 3, 3]
minha_tupla = 1, 2, 3 # ou (1, 2, 3)

try:
    minha_tupla[1] = 3
except:
    print("Tuplas são imútaveis") # << linha exexutada

# tuplas são boas para usar em funções que vão ser retornados multiplos valores

def soma_mult(x, y):
    return (x+y), x*y

tupla_soma_mult = soma_mult(3, 4)
print(tupla_soma_mult)

x, y, z = minha_tupla
print(x, y, z)
x, y, z = y, z, x
print("Forma pythonic de mudar", x, y, z)

# Dicionários

dicionario_vazio = {}
dicionario_vazio_nao_legal = dict()
notas = {"Joel" : 22, "Nathan" : 21}
print(notas["Joel"]) # Joel é uma chave, e 22 é o valor da respectiva chave

#erro caso a chave não existe
try:
    notas["Kate"]
except:
    print("Erro chave Kate não existe no dicionário")

# O in assim como na lista pode ser usado para achar um chave

joel_tem_nota = "Joel" in notas # true
kate_tem_nota = "Kate" in notas # false

print(joel_tem_nota, kate_tem_nota)

# o metodo get retorna um valor 0, sem dar erro caso tal chave não exista

nota_joel = notas.get("Joel", 0)
nota_kate = notas.get("Kate", 0)
numero_estudantes = len(notas)
print(nota_joel, nota_kate, numero_estudantes)

# pode-se também mudar o valor diretamente pela chave
notas["Joel"] = 80
notas["Nathan"] = 99
notas["Kate"] = 100
print(len(notas), notas)

# exemplo de dicionário estruturado

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

print(tweet.keys())
print(tweet.values())
print(tweet.items)

tweet_values = tweet.values()
print(tweet_values)

# é possivel fazer abaixo
"user" in tweet.keys() # mas não é recomendável uma vez que não está tão simples, e abre trechos para confusão
"user" in tweet # é a mais correta maneira de verificar uma chave em um dicionário
"joelgrus" in tweet_values # True acaba sendo lento, porém é o único jeito de fazer

# assim como na tabela hash, as chaves devem ter valores unicos, portanto não é recomendado listas como chave, o que pode ser substituido por uma Tupla 
# ou então usar uma String

#
#       EXERCÍCIO PARA CONTAR AS PALAVRAS EM ARRAY COM PALAVRAS
#       VAI SER FEITO UM DICIONÁRIO PARA CONTAR A REPETIÇÃO DE PALAVRAS
#

document = "hoje é um dia belo dia belo belo dia k" 
document = document.split()

contar_palavras = {}


for words in document: #vai pegar cada palavra na lista com as palavras
    if words in contar_palavras: # se a chave da respectiva palavra já existe no dicionário, então o valor da chave é incrementado
        contar_palavras[words] += 1
    else:
        contar_palavras[words] = 1 # se a chave não existir, vai criar uma e já coloca o valor como 1.
print(contar_palavras)

print(contar_palavras.get("hoje", 0))

# uma alternativa para o código acima seria:

contar_palavras2 = {}

for words in document:
    try:
        contar_palavras2[words] += 1
    except KeyError:
        contar_palavras2[words] = 1

# a terceira alternativa seria

contar_palavras3 = {}

for word in document:
    contador_antes = contar_palavras3.get(word, 0) #caso o valor não exista ele vai colocar o 0 (o segundo argumento), caso exista vai pegar a cahve
    contar_palavras3[word] = contador_antes + 1 #caso não exista ele vai pegar o contador 0 e criar um novo, caso existe vai pegar a chave e somar


from collections import defaultdict

contador_palavras = defaultdict(int)

for word in document:
    contador_palavras[word] += 1

dd_list = defaultdict(list) #dd = default dictinorie, um dicionario de lista
dd_list[2].append(1)
print(dd_list)
dd_list[2].append(2)
print(dd_list)

dd_dict = defaultdict(dict) # dict() produz um dicionário dentro de um dicionario
dd_dict["Joel"]["City"] = "Seattle"
print(dd_dict)
dd_dict["Joel"]["Full_Name"] = "Joel Kazhar Mustan"
print(dd_dict)
dd_dict["Bryan"]["City"] = "Belo Horizonte"
dd_dict["Bryan"]["Full_Name"] = "Bryan Wille Souto Braga"
print(dd_dict)

# e também pode ser usados para funções

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1
print(dd_pair)
