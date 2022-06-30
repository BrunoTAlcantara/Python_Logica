from turtle import width


with open('abc.text','w+') as file:
      file.write('Linha 1\n')
      file.write('Linha 2\n')
      file.write('Linha 3\n')

      file.seek(0,0)
      print('Lendo Linhas')
      print(file.read())