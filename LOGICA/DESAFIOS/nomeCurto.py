 
user = input("Digite seu primeiro nome: ")


try:
  tamanho = len(user)

  if tamanho < 0:
    print("Digite um tamanho mairo que 0")
  elif tamanho <= 4:
    print("Seu nome e curto")
  elif tamanho == 5 and tamanho == 6:
    print("Seu nome e normal")
  else:
    print("Seu nome e muito grande")
except:
  print("O numero tem que ser string ")