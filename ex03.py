#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 28/06/2022
#
# 3 – inicie a tupla abaixo, e contar os itens, use o # método count().
# ('a','b','b','a','c','c','c','d','d',’e’)
# Obs: explicar a Counter() da collection.

# criar a tupla com valores ('a','b','b','a','c','c','c','d','d','e')
t1 = ('a','b','b','a','c','c','c','d','d','e')
print(t1)

# cast tupla -> set
conjunto = set(t1) # converte a tupla em um conjunto
print(conjunto) # imprime o conjunto
print() # imprime uma linha em branco

for i in set(t1): # percorre o conjunto e imprime os elementos da tupla (sem repetição)
  #set(lista1) - elementos únicos da lista1
  contador = t1.count(i) # conta o número de vezes que o elemento aparece na tupla (sem repetição)
  print(f"{i} : {contador}") # imprime o elemento e o número de vezes que ele aparece na tupla (sem repetição)

# explicando o método counter() de Colections
# Contar vários itens:
# Se você deseja contar vários itens em uma tupla, pode chamar  count() um loop.

# Essa abordagem, entretanto, requer uma passagem separada pela tupla para cada chamada do count();
# o que pode ser catastrófico para o desempenho.
# Em  vez disso, use a classe Couter() da biblioteca collections.
# ex
from collections import Counter
print(Counter(t1)) # imprime o contador da tupla (sem repetição)
# Imprimir Counter({'c': 3, 'a': 2, 'b': 2, 'd': 2, 'e': 1})

print(Counter(t1).items())  # Imprimir um dicionário de items ({'c': 3, 'a': 2, 'b': 2, 'd': 2, 'e': 1})
print(tuple(Counter(t1).items())) # converto o dic em tupla (('c', 3), ('a', 2), ('b', 2), ('d', 2), ('e', 1))
