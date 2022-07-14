#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 14/07/2022
#
# 1 – Gere tupla dinamicamente de tamanho 5, de
# tamanho aleatório entre 1 e 20

from random import randint # Importando a função randint da biblioteca random

# -- Primeira forma --

t1 = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20)) # 5 números randômicos

print(f'Tupla: {t1}') # Imprimindo a tupla no terminal
print(f'\nfim do programa') # Informando ao usuário que o programa terminou

# -- Outra forma --

# t1 = tuple(randint(1, 20) for i in range(5)) # 5 números randômicos usando for
# print(f'Tupla: {t1}') # Imprimindo a tupla no terminal
# print(f'\nfim do programa') # Informando ao usuário que o programa terminou
