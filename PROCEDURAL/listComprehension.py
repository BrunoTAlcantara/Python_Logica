import time


def fala_ola_mundo():
    ola_mundo = 'Olá'
    yield ola_mundo
    time.sleep(4)
    ola_mundo += ' Mundo'
    yield ola_mundo
 
 
fala = fala_ola_mundo()
print(next(fala))  # Olá
print(next(fala))  # Olá Mundo