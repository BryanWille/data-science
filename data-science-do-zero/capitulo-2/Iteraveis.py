#Usamos yields para fazer gerados em python
#Yields param em cada chamada, mas param e voltam pra onde terminaram, não do 0.
#Por isso são usados para fazer gerados em python.

def range_numeros(n):
    i = 0
    while i < n:
        yield i
        i += 1


for i in range_numeros(10):
    print(f"i: {i}")

# Yield basicamente faz uma repetição e para nessa repetição para retornar o número, mas deixa salvo onde parou,
# por isso usamos esse segundo for para ver, uma alternativa abaixo explica melhor, filtrar somente os numeros impares:

print("")

def range_numeros_impares(n):
    i = 0
    while i < n:
        i += 1
        if i % 2 != 0:
            yield i


for i in range_numeros_impares(10):
    print(f"i: {i}") # impares


# gerando uma array com o yield e um for inline

pares_menores_20 = (x for x in range_numeros(20) if x % 2 == 0)


# Extrair apartir do yield

def natural_numbers():
    i = 0;
    while i <= 120:
        yield i
        i += 1

print(" ")
data = natural_numbers()
pares = (x for x in data if x % 2 == 0) # todos os yields vão vir para esse pares
pares_ao_quadrado = (x ** 2 for x in pares) # o quadrado dos yields pares
pares_qudarados_terminados_em_seis = (x for x in pares_ao_quadrado if x % 10 == 6) # quadrdos que terminam em seis
for elementos in pares_qudarados_terminados_em_seis:
    print(elementos)

#Podemos além de obter o os valores obter o indice com a função enumerate:

names = ["Alice", "Bob", "Charlie", "Debbie"]
#   index nome em enumarte(lista ou gerador)
for i, name in enumerate(names):
    print(f"nome {i} is {name}")

