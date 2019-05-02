#Minha biblioteca , matematica_temp.py
def celskel(C):# Celsius para Kelvin
    K = (C + 273.15)
    return ('RESULTADO...\n{K:.2f}K'.format(K=K))

def celsfah(C):  #Celsius para Fahrenheit
    F = (C * 1.8 + 32)
    return ('RESULTADO....\n{F:.2f}°F'.format(F=F))

def celsre(C): # Celsius para Réamur
    R = (C * 4 / 5)
    return ('RESULTADO...\n{R:.2f}°Ré'.format(R=R))

def kelcels(K):  # Kelvin para Celsius
    C = (K - 273.15)
    return ('RESULTADO....\n{C:.2f}°C'.format(C=C))

def kelfah(K):  # Kelvin para Fahrenheit
    F = (K * 1.8 - 459.7)
    return ('RESULTADO...\n{F:.2f}°F'.format(F=F))

def kelre(K):  #Kelvin para Réamur
    R = (K - 273.15 * 0.8)
    return ('RESULTADO...\n{R:.2f}°Ré'.format(R=R))

def fahcels(F):  # Fahrenheit para Celsius
    C = (F - 32 / 1.8)
    return ('RESULTADO....\n{C:.2f}°C'.format(C=C))

def fahkel(F):  # Fahrenheit para Kelvin
    K = ((F - 32) / 1.8 + 273)
    return('RESULTADO....\n{K:.2f}K'.format(K=K))

def fahre(F): # Fahrenheit PARA Réamur
    R = (F - 32) * 4/9
    return ('Resultado ....\n{R:.2f}Ré'.format(R=R))

def recels (R): # Réamur para célsius
    C = (R * 5/4)
    return ('Resultado ....\n{C:.2f}°C'.format(C=C))

def rekel (R): # Réamur para kelvin
    K =  ((R *5/4) + 273.15)
    return ('Resultado.....\n{K:.2f}K'.format(K=K))

def refah (R): # Réamur para fahrenheit
   F = (R * 9/4 + 32)
   return ('Resultado.....\n{F:.2f}°F'.format(F=F))