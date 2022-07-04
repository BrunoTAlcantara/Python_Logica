#When resistors are connected together in series,
 #the same current passes through each resistor ]
 #in the chain and the total resistance, RT, 
# of the circuit must be equal to the sum of all the individual resistors added together. That is:

def series_resistance(lst):
    soma = sum(lst)
    final = str(soma) +' ohms'
    return print(final)

series_resistance([1,5,6,3])