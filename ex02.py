#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 28/06/2022
#
# 2 – verifique se um determinado elemento esta
# contido na tupla ('a','b',1,2,'c',3,4,'d',5)
#
# criana uma tupla com valores ('a','b',1,2,'c',3,4,'d',5)
t1 = ('a', 'b', 1, 2, 'c', 3, 4, 'd', 5)

# imprimir os elementos da tupla
for i in t1:
    print(i)  # imprime os elementos da tupla

# imprimir a tupla
for i in t1:
    print(t1)  # imprime a tupla varias vezes

# verificar se o elemento 'b' esta contido na tupla
print('b' in t1)  # imprime True

print('a' in t1) # True (contido)
print('e' in t1) # False (não contido)
print('e' not in t1) # True (não contido)

for i in range(len(t1)):
  print(i in t1) # imprime True para cada indice contido na tupla

for i in range(len(t1)):
  print(f"{i} = {i in t1}") # imprime True para cada indice contido na tupla

# verifica se o valor 'a' esta contido na tupla
for i, valor in enumerate(t1): # enumerate retorna um iterador de pares (indice, valor) da tupla
   print(f"indice[{i}] -> {valor} = {i in valor}")