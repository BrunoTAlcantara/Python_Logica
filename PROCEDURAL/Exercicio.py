
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def funcao(sau,nome):
  return print(f'{sau} meu nome e {nome}')

funcao('Olá', 'Bruno Theodoro')
"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def soma(a,b,c):
  return (a+b+c)

print(soma(1,2,3))

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""

def perc(dinheiro,porcent):

  return (porcent/100) * dinheiro

print(perc(50,10))

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def FizzBuzz(par):
  if  par%5==0 and par%3==0:
    return print('FizzBuzz')
  elif par%5==0:
    print('buzz')
  elif par%2==0:
    print('fizz')
  else:
    print(par)

FizzBuzz(17)