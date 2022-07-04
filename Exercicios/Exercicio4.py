#Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

#Se o número for múltiplo de 3, a saída deve ser "Fizz".
#Se o número fornecido for múltiplo de 5, a saída deve ser "Buzz".
#Se o número fornecido for um múltiplo de 3 e 5, a saída deve ser "FizzBuzz".
#Se o número não for um múltiplo de 3 ou 5, o número deve ser gerado sozinho, conforme mostrado nos exemplos abaixo.
#A saída deve ser sempre uma string, mesmo que não seja um múltiplo de 3 ou 5.

def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  else:
    str(num)
