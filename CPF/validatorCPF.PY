cpf = '489.801.338-47'

tam = len(cpf)
p1 = cpf[3]
p2= cpf[7]
p3= cpf[11]


digit1= cpf[12]
cont1 = 10
cont2 = 11
f1 = 0
f2=0

separator = cpf.split('-')



num = separator[0]
num2 = separator[0]
dig = separator[1]

numReplace = num.replace('.','')

numReplace2 = numReplace + digit1


for i in numReplace:
  soma = int(i) * cont1
  cont1 -=1
  f1 = f1 + soma



for i in numReplace2:
  soma = int(i) * cont2

  cont2 -=1
  f2 =  f2 + soma

  
dig1 = (11-(f1%11))
dig2 = (11-(f2%11))




if dig1>=11 :
  dig1 = 0

if dig2 >=11:
  dig2 = 0

valitorDig = str(dig1)+ str(dig2)

if p1 == '.' and p2 == '.' and p3=='-' and tam == 14:
  if(valitorDig==dig):
    print(f'O CPF: {cpf} é um CPF VALIDO')
  else:
    print('CPF INVALIDO') 
else:
  print ('Digite na formatação correta ex:168.995.350-09')