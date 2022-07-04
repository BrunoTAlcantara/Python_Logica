# Um trem tem uma capacidade máxima de n passageiros em geral, o que significa
#que a capacidade de cada vagão compartilhará uma proporção igual da capacidade máxima.

#Crie uma função que retorne o índice do primeiro carro que contém 50%
# ou menos de sua capacidade máxima. Se esse carro não existir, retorne -1.

# There are 5 carriages which each have a maximum capacity of 40 (200 / 5 = 40).
# Index 0's carriage is too full (35 is 87.5% of the maximum).
# Index 1's carriage is too full (23 is 57.5% of the maximum).
# Index 2's carriage is good enough (18 is 45% of the maximum).
# Return 2.
def find_a_seat(n, lst):

  size = len(lst)
  vagas = n/size
  for  i,ls in enumerate(lst):
     if ls <= vagas/2:
      return i
  else:
     return -1

find_a_seat(200, [35, 23, 18, 10, 40])
