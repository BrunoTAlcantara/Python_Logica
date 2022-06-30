
#list, tuples, str -> Sequencia -> Iteravel
nome = 'bruno'
# Iterador sao finitos
iterador = iter(nome)


bruno,amanda = 0,1

print(bruno)

print('espaço')
print('amanda')

for letra in iterador:
  print(letra)
print('NAO RETORNA NADA POIS E UM ITERADOR E JA CONSUMIU OS DADOS')
for letra in iterador:
  print(letra)
print('RETORNA POIS SAO ITERAVEIS ')
for letra in nome:
  print(letra)
for letra in nome:
  print(letra)
for letra in nome:
  print(letra)

