class Pessoa:
  ano_atual = 2022
  def __init__(self,nome,idade, ):
    self.nome = nome
    self.idade = idade
    
  def get_ano_nascimento(self):
    print(self.ano_atual - self.idade)
    



p1= Pessoa('Bruno', 23)
p1.get_ano_nascimento()