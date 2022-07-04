

def stutter(word):
  inicial = word[0] + word[1]
  final = inicial + '...' + inicial +'...'+ word + '?'
  return print(final)
  
stutter("adventures")