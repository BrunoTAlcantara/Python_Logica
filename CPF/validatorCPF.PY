cpf = '168.995.350-09'

cont1 = 10
cont2 = 11
f1 = 0
f2=0
print(cpf)
separator = cpf.split('-')

num = separator[0]
dig = separator[1]

numReplace = num.replace('.','')


for i in numReplace:
  soma = int(i) * cont2
  cont2 -=1
  f2 = f2 + soma

for i in numReplace:
  soma = int(i) * cont1
  cont1 -=1
  f1 = f1 + soma
  
dig1 = (11-(f1%11))
dig2 = (11-(f2%11))


if dig1>=11 :
  dig1 = 0

if dig2 >=11:
  dig2 = 0

valitorDig = str(dig1)+ str(dig2)

if(valitorDig==dig):
  print('CPF VALIDO')
else:
  print('CPF INVALIDO')  