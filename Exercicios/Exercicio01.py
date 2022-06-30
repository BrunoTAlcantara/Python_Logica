
# Exerxicio completo = https://exercism.org/tracks/python/exercises/meltdown-mitigation






def reactor_efficience(voltage,current,theoretical_max_power):
    generatePower = voltage*current
    resul = (generatePower/theoretical_max_power)*100
    
    if resul >= 80:
        return print('Green')
    elif resul<80 and resul>= 60:
        return print('Orange')
    elif resul<60 and resul>= 30:
        return print('Red')
    else:
        return print('Black')

def is_critical_balance(temp, neutr):
    if temp < 800 and neutr >500:
        return print ('True')
    else:
        return print ('False')
def fail_safe(temperature,neutrons_produced_per_second,threshold):
     porce = temperature*neutrons_produced_per_second
     if porce <threshold *0.9:
        return print('LOW')
     elif porce <threshold *0.1:
        return print('NORMAL')
     else:
        return print('DANGER')

    





is_critical_balance(750, 600)
reactor_efficience(200,50,15000)
fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)

