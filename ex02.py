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


#############################################################################
print("--------------------------------------------------------------------")
#############################################################################
# Python enumerate()
# O enumerate()método adiciona um contador a um iterável e o retorna (o objeto enumerate).
# O enumerate() é um objeto que representa um contador.
# exemplo:
# linguagens = ['Python', 'Java', 'JavaScript']
#
# enumerate_prime = enumerate(linguagens)
#
# # converte o objeto enumerate_prime em uma lista
# print(list(enumerate_prime))
#
# # saida: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


# Sintaxe de enumerar():
# enumerate(iterável, start=0)
# enumerate() Parâmetros:
# O método recebe dois parâmetros:
# # iterável - uma sequência, um iterador ou objetos que suportam iteração
# start (opcional) - enumerate()inicia a contagem a partir deste número. Se start for omitido,
# 0 é tomado como start.

t2 = enumerate(t1) # cria um enumerate para a tupla t1
print(t2) # imprime o enumerate da tupla t1 (indice, elemento)
print(list(t2)) # converte o enumerate em lista (indice, elemento)

# loop para imprimir o enumerate da tupla t1 (indice, elemento)
for i, valor in enumerate(t1): # enumerate retorna um iterador de pares (indice, valor) da tupla
   print(f"indice[{i}] -> {valor}") # imprime o indice e o valor do elemento da tupla