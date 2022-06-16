import random as r

r.seed(10) # determina que os números gerados, vão ser sempre iguais, diferindo da quantidade de vezes na qual random é chamado

quatro_randomicos = (r.random() for _ in range(4)) # como não temos um vamos usar nenhum variavel colocamos _ mesmo.

for aleatorio in quatro_randomicos:
    print(aleatorio)

r.seed(10) # define a seed em 10
print(r.random())
r.seed(10) # essa seed é universal e sempre se repete
print(r.random())

# randrange, pega um limite de inicio e final e faz aleatorio entre eles
# se tiver apenas um argumento é o de final.

print(r.randrange(10))
print(r.randrange(2, 200))

# Outros métodos podemos usar em casos de teste, como por exemplo o shuffle() que reorganiza em ordem aleatória

ate_dez = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r.shuffle(ate_dez)
print(ate_dez)

# pode-se também usar o choice para selecionar aleatoriamente um elemento da lista

meu_melhor_amigo = r.choice(["Bryan", "Wille", "Souto", "Braga"])
print(meu_melhor_amigo)

#podemos usar a função range para criar valores de 0 até x.
#Pode-se usar o sample para pegar uma amostra aleatória com tamanho definido, de uma quantidade de numeros
#Esse não vai ter substituição, ou seja os números vão se manter

mega_sena = range(60)
resultado_mega_sena = r.sample(mega_sena, 6)
print(resultado_mega_sena)

#Agora para selecionar com substituição:

quatro_com_troca = [r.choice(range(10)) for _ in range(4)] #vai escolher quatro numero aleatorios de 0 a 10
print(quatro_com_troca)
