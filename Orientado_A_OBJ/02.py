class Produto:
  def __init__(self,nome,preco):
    self.nome= nome
    self.preco= preco
  def desconto(self,percentual):
    self.preco= self.preco - (self.preco*(percentual/100))

p1=Produto('Coca',2)
p1.desconto(10)
print(p1.preco)
p2=Produto('Frango',20)
p3=Produto('Leite',4)