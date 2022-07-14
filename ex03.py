#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 14/07/2022
#
# 3 – inicie a tupla abaixo, e contar os itens, use o # método count().
# ('a', 'b', 'b', 'a', 'c', 'c', 'c', 'd', 'd', 'e')

# -- Entrada de dados --

t1 = ('a','b','b','a','c','c','c','d','d','e') # Criando a tupla pré-definidos
print('Tupla: ', t1) # Imprimindo a tupla no terminal

# -- Processamento e saída de dados --

conjunto = set(t1) # Convertendo a tupla em um conjunto
print('Conjunto: ', conjunto) # Imprimindo o conjunto

print() # Print vazio deixa uma linha no terminal, como um enter do teclado

for i in conjunto: # Percorrendo o conjunto e imprimindo os elementos
  contador = t1.count(i) # Contando o número de vezes que o elemento aparece
  print(f"{i} : {contador}") # Imprimindo o elemento e o número de vezes que aparece

# -- [ Método counter() da Colections ] --
# - Função: contar vários itens
# - Se você deseja contar vários itens em uma tupla, pode chamar count() em um loop.
# - Essa abordagem, entretanto, requer uma passagem separada pela tupla para cada chamada do count();
# - o que pode ser catastrófico para o desempenho.
# - Em  vez disso, use a função Counter() da biblioteca collections.

# Exemplo;
"""from collections import Counter # Importando a função Counter da biblioteca collections

print(f'\nDicionário (Elemento/Repetições): {dict((Counter(t1)))}') # Imprime dicionário com os valores contados
print(f'Tupla (Elemento/Repetições): {tuple(Counter(t1).items())}') # Imprimindo o dic.items em tupla com tuple()"""

print('\nfim do programa') # Informa ao usuário que o programa terminou
