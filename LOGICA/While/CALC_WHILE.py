while True:
  num1= input('Digite um numero: ')
  num2= input ('Digite um numero: ')
  op= input ('Digite um operador: ')
  res=0
  sair = input('Deseja Sair? S para sim e N para nao: ')
  
  if sair.lower() == 's':
    break

  if not num1.isnumeric() or not num2.isnumeric():
    print('Voce precisa Digitar um numero')
    continue

  num1= int(num1)
  num2= int(num2)

  if op == '-':
   res = (num1-num2)
  elif op == '+':
   res = (num1+num2)
  elif op == '/':
   res = (num1/num2) 
  elif op == '*':
   res = (num1*num2)
  else:
    print('Digite um operador correto')
  
  print(res)
  
 
 