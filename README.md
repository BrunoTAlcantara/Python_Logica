### **If - elif - else**

```python
hora = input("Qual Horario? ") 

if hora>=0 and hora<=11:
  print('Bom dia')
elif hora >= 12 and hora <= 17  :
  print('Bom tarde')
elif hora >= 18 and hora <= 23 :
  print('Boa noite')
else:
  print('Digite um numero entre 0 e 23')
```

### WHILE

```python
cont=1
acum=1 
while cont<=10:
  if cont >5:
    break
  print(cont,acum)
  acum = acum+cont
  cont += 1
else:
  print('Cheguei no else')

print('DEU BREAK')
```

### FOR IN

```python
for n in range(1,10,2):
  print(n)
```

### STRING EM PYTHON

- string.split(”-”) - Corta string com base no valor passado em parametro
- len(string) - retorna o tamanho da string
- ‘,’.join(lista) - junta lista e tranforma em string
- string.replace('.','') - substitu o primeiro parametro pro segundo
- int().string - tranforma em inteiro bool() - tranforma em boll float() - transfroma em float

### LISTAS COMPREHENSION

l1 = [1,2,3,4,5,6,7,8,9,10]

#joga cada elemento da lista acima na primeira variavel criando uma nova lista

l2 = [variavel for variavel in l1]

l3= [v*2 for v in l1] # cada elemento foi multiplicado por 2

lista=['Luiz', 'Mauro', 'Maria']

ex=[v.replace('a','@') for v in l2]

#reposta ['Luiz', 'M@uro', '[M@ria@]']

### LISTAS EM PYTHON

- Deempacotar listas = lista=[1,2,3,4,5]  ; n1,n2 *n = lista ; n1 vale 1 e n2 vale 2 e variavel  n vale [3,4,5]
- lista[0] = primeiro valor ; lista [-1] = ultimo valor
- lista=[1,2,3,4,5]; *lista retrona 1,2,3,4,5
- lista.append(1) - Insere um novo valor na lista no final
- enumerate(lista) - enumera uma lista
- lista.insert(0,'c') - Insere um novo valor no indice informado
- lista.pop() Remove o ultimo elemento da lista
- max(lista) Pega o item maior da lista
- min(lista) Pega o item menor valor  da lista
- lista.sort(key=func) filtra do menor por maior
- Tuplas t1=(1,2,3,’a’,true)  são listas porem que nao podem ser alteradas

# Criando um contador

```python
#CONTADOR SIMPLES
for cont in range(0,10):
    print (cont)

#CRIAR CONTADOR DE TRAS PRA FRENTE E ENUMERAR CADA 1
for i,cont in enumerate(range(0,10)):
    print (i,cont)
```

# FUNÇOES

- *args  são parametros que ainda nao foram enviados
- **kwargs são parametros com valores que ainda nao foram enviados
- a = lambda x,y: x*y é uma função reduzida

```python
def func(*args,**kwargs):
	print(args)

lista = [1,2,3,4,5]

func(*lista, nume=luiz)
#lista sao *args e nome é um **kwargs

a = lambda x,y: x*y

```

# DICIONARIOS - OBJETOS EM JS

### LISTAS COMPREHENSION

- nova_lista = [x for x in lista] copia lista para o primeiro x
- nova_lista = [x for x in lista if x>5 ] retorna apenas os maiores que 5

 

- print (chave in d1) - Vai retornar True pois existe chave no dicionario D1
- print (’valor’ in d1.values()) Vai retornar True pois existe chave e um valor no dicionario D1
- del d1[’nome_da_chave’] apagar algum valor
- for k, v in d1.items - acessar chave e valor
- novo_d1 = d1.copy() copia pra um novo dicionario
- lista = [[1,2],[3,4],[5,6]]  d1 = dict(lista) tranforma lista parecida com diconario em dicionario

```python
d1 = {
  'chave':'Valor22',
  'chave2':'Valor2',
  'chave3':'Valor3'
  }

print (chave in d1) # Vai retornar True pois existe chave no dicionario D1
print (Valor2 in d1.values())
```

### SET EM PYTHON

- set.add(1) add item ao set
- set.discar(1) remove um item
- set.update(’python’) add porem separando a string
- set1 | set2 faz a uniao dos sets
- set & set2 faz a junção dos iguais
- set1 - set2 remove os iguais

# ITERADOR E GERADORES

```python
#list, tuples, str -> Sequencia -> Iteravel
nome = 'bruno'
# Iterador sao finitos
iterador = iter(nome)

for letra in iterador:
  print(letra)
print('NAO RETORNA NADA POIS E UM ITERADOR E JA CONSUMIU OS DADOS')
for letra in iterador:
  print(letra)
print('RETORNA POIS SAO ITERAVEIS ')
for letra in nome:
  print(letra)
for letra in nome:
  print(letra)
for letra in nome:
  print(letra)
```

### yield entrega um valor de cada vez

```python
import time

def fala_ola_mundo():
    ola_mundo = 'Olá'
    yield ola_mundo
    time.sleep(4)
#espera 4 sec e entregar o valor
    ola_mundo += ' Mundo'
    yield ola_mundo
 
 
fala = fala_ola_mundo()
print(next(fala))  # Olá
print(next(fala))  # Olá Mundo
```

### ZIP - ZIP_LONGEST - COUNT - GROUPBY- MAP -FILTER- REDUCE

- ZIP - CADA INDICE DE UMA LISTA COM OUTRA E FORMA UMA TUPLA, E , ZIP_LONGEST SE UMA FOR MAIOR RETORNA NONE
    
    ```python
    from intertools import zip_logest
    
     cidade =['SAO PAULO', 'MINAS GERAIS', 'SALVADOR']
     estados =['SP','MG', 'BA']
    
    cidade_estados = zip(cidade, estados) 
    #RETORNA [('SP,'SAO PAULO'), ('MINAS GERAIS','MG'),('SALVADOR', 'BA')
    ```
    

### COUNT - COUNT (START =2, STEP=3)

### SORT = ORDENAR alunos.sort(lambda item: item[’nota’])

### GROUPY = AGRUPAR alunos_agrupados = groupy(alunos, lambda item : item[’nota])

```python
from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]

def ordena(item):
  return item['nota']

alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

'''
# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
'''

# Com tee
for agrupamento, valores_agrupados in alunos_agrupados:
  v1, v2 = tee(valores_agrupados)

  print(f'Agrupamento: {agrupamento}')

  for aluno in v1:
    print(f'\t{aluno}')

  quantidade = len(list(v2))
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
```

### MAP, FILTER, REDUCE

```python
produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 30},
]
 
pessoas = [
    {'nome': 'Luiz', 'idade': 12},
    {'nome': 'Luiz', 'idade': 20},
    {'nome': 'Luiz', 'idade': 30},
]

#quero um dicionario apenas com os preços

precos = map(lambda p:p['preco'], produtos)
for preco in precos:
  print(preco) 
#RETORNA TODOS OS PREÇOS

filtros = filter(lambda p:p['preco'] > 50, produtos)

for filtro in filtros:
  print(filtro)
#FILTRA OS PRECOS
```

# FUNÇÃO DECORADORA

```python
"""
Funções decoradoras recebem uma função como parâmetro e decoram/modificam
ela retornando uma nova a ser usada no lugar.
"""
 
def decorar(funcao):
    
    # Geralmente, ao decorar uma função, deseja-se substituí-la por outra.
    # E esta abaixo irá substituir a recebida como parâmetro acima
    def funcao_decorada():
        print('############')
        funcao()
        print('############')
 
    return funcao_decorada
 
def printar():
    for i in range(3):
        print(i)
 
nova_printar = decorar(printar)
 
nova_printar()
# Saída:
# ############
# 0
# 1
# 2
# ############
# 
# Ou seja, fizemos uma decoração/modificação na função printar().
# Ao colocar o @decorador em cima de uma função X, o que o
# interpretador do Python faz é X = decorador(X).
```

# Classes

```python
class Pessoa:
  ano_atual = 2022
  def __init__(self,nome,idade, ):
    self.nome = nome
    self.idade = idade
    
  def get_ano_nascimento(self):
    print(self.ano_atual - self.idade)
    

p1= Pessoa('Bruno', 23)
p1.get_ano_nascimento()
```