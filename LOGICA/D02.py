

hora = input("Qual Horario? ") 

if hora>=0 and hora<=11:
  print('Bom dia')
elif hora >= 12 and hora <= 17  :
  print('Bom tarde')
elif hora >= 18 and hora <= 23 :
  print('Boa noite')
else:
  print('Digite um numero entre 0 e 23')
