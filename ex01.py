#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 28/06/2022
#
# 1 – gere tupla dinamicamente de tamanho 5, de
# tamanho aleatório entre 1 e 20
#
# importa a biblioteca random para gerar os valores da tupla
from random import randint

# gera a tupla de tamanho 5 com valores aleatório
t1 = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
print(t1)

# ou
# gera a tupla de tamanho 5 com valores aleatório
t2 = tuple(randint(1, 20) for i in range(5))
print(t2)

# ou
# gera a tupla de tamanho aleatorio, com valores sempre entre 1 e 20
t3 = tuple(range(randint(1, 20)))
print(t3)

