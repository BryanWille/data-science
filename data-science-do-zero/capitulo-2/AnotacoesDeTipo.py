#Basicamente o python confude tudo porque não precisa anotar o tiop das variavéis
#Dai entra o modo javesco de fazer as anotações de tipo
#basicamente nas funções variavel: Tipo, variavel2: tipo) -> Tipo:
# ao acabar o parenteses tem a seta -> para mostrar qual tipo vai retornar e depois acbaro def com o dois ponto
#x

def multiplicacao(x: int, f: float) -> float:
    return x * f

def concat_texto(quant_vezes: int, texto: str) -> str:
    return texto, "abc"

#Não restrigem o tipo de dado de entrada, apenas avisa antes

def soma(num: typing.List[float]) -> float:
    return sum(num)

#Como anotações são objetos podemos atribuir tipo a elas, exemplo:
Number = int
def soma2(x: Number, y: Number) -> Number:
    return x + y

# e por fim podemos usar módulo Typing que tem varios tipos prontos

from optparse import Option
import typing
def soma2(x: typing.Optional[float]): 
    return x

# e tmbém podemos usar o Callable para funções de primeiro grau, o u seja que pegam de outra função ex

def twice(repeater: typing.Callable[[str, int], str], s: str) -> str:
    return repeater(s,2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type_hints") == "type hints, type hints"