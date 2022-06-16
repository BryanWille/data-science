import re
re_examples = [
    not re.match("a", "cat"), # cat não começa com a
    re.search("a", "cat"), # cat contem um a
    not re.search("c", "dog"), # dog não contém um c
    3 == len(re.split("[ab]", "carbs")), # Divide em a ou b para ['c', 'r', 's'] se for igual a 3
    "R-D-" == re.sub("[0-9]", "-", "R2D2")
]

assert all(re_examples), "Todos os exemplos de regex devem ser verdadeiros"

#re.search verifica se ALGUMA PARTE corresponde
#re.match verifica se o INICIO corresponde

assert 1 > 2, "falso" # se der errado imprime a mensagem
assert 2 > 1, "verdadeiro" # se não só continua e não mostra mensagem, ou seja depurar