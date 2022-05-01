from itertools import count


class CountingClicker:
    """Apenas um teste"""

    def __init__(self, count = 0): # Construtor precisa de ter dois underlines, método dunder
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"
    
    def clicked(self, num_times = 1): # Colocando na assinatura para caso não se passe parametros, começar com 1
        self.count += num_times
    
    def read_count(self):
        return self.count
    
    def reset(self):
        self.count = 0

click1 = CountingClicker()
click2 = CountingClicker(100)
click3 = CountingClicker(count=100)
click1.clicked()
click1.clicked()
click1.read_count() # = 2


#métodos que tem sublinhado na primeira letra do nome, são por convenção métodos "privados", mas da para chamalos

clicker = CountingClicker()
assert clicker.read_count() == 0, "Clicker tem que começar com contador == 0"
clicker.clicked()
clicker.clicked(num_times=3)
assert clicker.read_count() == 4, "depois de dois clicks, o clicker tem que ser 2"
clicker.reset()
assert clicker.read_count() == 0, "Depois de resetar, o clicker tem que voltar para 0"

# Pode-se usar herança aqui e remover o método reset na herança

class NoResetClicker(CountingClicker):
    #O parenteses faz a herança com a classe CountigCLicker

    #Agora vamos fazer com que o metodo reset não faça nada
    def reset(self):
        pass # significa que nada vai ser feito além de declarar o método (pode ser usado em classes também)

clicker2 = NoResetClicker()
assert clicker2.read_count() == 0
clicker2.clicked()
assert clicker2.read_count() == 1
clicker2.reset()
assert clicker2.read_count() == 1, "reset não fez nada"