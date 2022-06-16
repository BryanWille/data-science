#Args e Kwargs servem basicamente para funções que necessitaem de outra funções dentro, as vezes queremo mudar a função
# de dentro e simplesmente não funciona

def faz_algo(f): #Iniciamos a função faz_algo que recebe a função soma como parametro
    def g(x):   # Essa função vai receber o x da função que está recebendo como parametro
        return 2 * f(x) #Função retorna o g que é 2 * soma(3) = 8
    return g

def soma(x):
    return 1 + x

algo = faz_algo(soma)
print(algo(3)) 

#Agora imagine que queira mudar para uma função soma que obtenha dos valores como a de baixo

def soma2(x: int, y: int) -> int:
    return x + y

# algo = faz_algo(soma2)
# assert algo(3,2) == 0, "Função g tem precisa de só um argumento"

# Não vai funcionar pois a função g só recebe um argumento e na função soma2 colocamos 2
# Então vamos usar o kwargs e args para fazer essa boa
# E vamos usar a compactação disso

# O que são kwargs e args:
# args são tuplas e kwargs são dicionarios: ex

def magia(*args, **kwargs):
    print("Argumentos não nomeados: ", args)
    print("Palavras chaves não nomeadas: " , kwargs)

magia(1, 2, key="word", key2="word2")
#argumentos que não são keywords viram uma tupla dos args
#arugmetos que passam para o parametro key vão pro dicionario do kwargs

# Podemos fazer o contrário também, retransformar

def magia_de_volta(x, y, z):
    return x + y + z

x_y_lista = [1, 2]
z_dict = {"z": 3}
assert magia_de_volta(*x_y_lista, **z_dict) == 6, "1+2+3 deveria ser 6"

#Esses truques vão ser usados para funções de altas ordens (que tem mais funções dentro uma da outra)

# Corrigindo agora para receber mais de uma

def faz_algo_corrigido(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

g = faz_algo_corrigido(soma2)
assert g(1, 2) == 6, "faz algo funciona agora"