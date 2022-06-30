produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 60},
    {'nome': 'p3', 'preco': 30},
]

def desconto(p):
  p['preco'] = round(p['preco'] * 1.5,2) 
  return p


precos = map(desconto,produtos)



filtros = filter(lambda p:p['preco'] > 50, produtos)


for filtro in filtros:
  print(filtro)

