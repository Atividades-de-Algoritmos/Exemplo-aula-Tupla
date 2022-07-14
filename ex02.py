#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 14/07/2022
#
# 2 – Verifique se um determinado elemento esta
# contido na tupla ('a','b',1,2,'c',3,4,'d',5)

t1 = ('a', 'b', 1, 2, 'c', 3, 4, 'd', 5) # Criando uma tupla com valores ('a','b',1,2,'c',3,4,'d',5)

print(f'Tupla: {t1}\n') # Imprimindo a tupla no terminal

# Verificando alguns valores
print('"e" na tupla ->', 'e' in t1) # False (não contido)
print('"f" na tupla ->', 'f' in t1) # False (não contido)
print('"g" na tupla ->', 'g' in t1) # False (não contido)

for i in t1: # Para cada item armazenado na tupla
  print(f'"{i}" na tupla -> {i in t1}') # Imprime True or False para o item do ciclo atual

var = input('\nDigite um valor pra ver se tem na tupla: ') # Solicitando valor do usuário

print(f'\n"{var}" na tupla ->', {var} in t1) # Verificando se existe ou não

# -- [ Python enumerate() ] --

# - O enumerate() é um método que quando chamado representa uma tupla sendo o primeiro valor o índice e o segundo o valor real.
# - Exemplo (Único parâmetro):

# 01 - linguagens = ['Python', 'Java', 'JavaScript']

# 02 - enumerate_prime = enumerate(linguagens)

# 03 - print(list(enumerate_prime)) # Convertendo o objeto em uma lista

# Return: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


# -- [ Parâmetros do método enumerate() ] --

# - Sintax: enumerate(iterável, start=0)

# O método recebe dois parâmetros;
# iterável(Primeiro) - Todo objeto que permite que um loop seja executado nele.
# start (opcional) - Quando o start não é informado sub-entende que é 0, quando é informado a iteração começa do que foi chamado.

# Exemplo (Dois parâmetros):

# 01 - linguagens = ['Python', 'Java', 'JavaScript']

# 02 - enumerate_prime = enumerate(linguagens, start = 5)

# 03 - print(list(enumerate_prime)) # Convertendo o objeto em uma lista

# Return: [(5, 'Python'), (6, 'Java'), (7, 'JavaScript')]

"""t2 = enumerate(t1) # Criando um enumerate para a tupla t1
print(t2) # Imprimindo o objeto do enumerate da tupla t1
print(list(t2)) # Convertendo o enumerate em lista (indice, elemento)
"""

print('\nfim do programa') # Informando ao usuário que o programa terminou
