#César Pumacayo 1°E grupo giovanni

#Ejercicio 2
# Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.

def area_circulo(radio):
    '''
    Calcular el area del circulo
    Recibe parametros (radio)
    Retorna area del circulo
    
    '''
    pi = 3.14 
    area = pi * radio**2
    return area

print(area_circulo(5)) # 78.54
