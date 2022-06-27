user = input("Digite um numero Inteiro: ")

try:
  user = int(user)
  resto= user % 2
  if resto == 0 :
    print('O numero e par')
  else:
    print('O numero e impar')
except:
  print('Nao e um numero inteiro')