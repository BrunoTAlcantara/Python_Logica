perguntas = {
  'Pergunta 1': {
    'pergunta': 'Quanto e 2+2',
    'respostas': {
      'a':'4',
      'b':'3',
      'c': '2'
    },
    'resposta_certa':'b',
  }
}

for pk,pv in perguntas.items():
  print(pk,pv['pergunta'])