
#https://exercism.org/tracks/python/exercises/card-games

def get_round(round_number):

    lista=[round_number]
    for round in range(0,2):
        round_number = round_number+1
        lista.append(round_number)
    return print(lista)



def concatenate_rounds(rounds_1, rounds_2):
   concatLista = [*rounds_1,*rounds_2]
   return print(concatLista)



get_round(27)
concatenate_rounds([27, 28, 29], [35, 36])  