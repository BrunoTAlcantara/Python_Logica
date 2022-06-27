
cont=1
acum=1
#pulou o 3 pois se x for igual a 3 soma mais 1 e continue 
while cont<=10:
  if cont >5:
    break
  print(cont,acum)
  acum = acum+cont
  cont += 1
else:
  print('Cheguei no else')

print('DEU BREAK')  

