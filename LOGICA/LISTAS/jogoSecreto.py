digitadas = []
secreto = 'perfume'

while True:
  letra = input('Digite uma letra: ').lower()

  if len(letra) > 1:
    print('Ahhh isso não vale, digite apenas uma letra.')
    continue
  digitadas.append(letra)
  
  if letra in secreto:
    print(f'UHULL, a letra letra "{letra}" existe na palavra secreta')
  else:
    print(f'AFFS,  a letra letra "{letra}" nao existe na palavra secreta')
  secreto_temporario =''
  for letra_secreta in secreto:
    if letra_secreta in digitadas:
      secreto_temporario += letra_secreta
    else:
      secreto_temporario +='*'

  print(secreto_temporario)
      
   
  if secreto_temporario == secreto:
     print('Voce ganhou')
     break
 

