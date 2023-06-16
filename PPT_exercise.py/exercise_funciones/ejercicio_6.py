#César Pumacayo 1°E grupo giovanni

#Ejercicio 6
#Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.

def calcular_area_triangulo(base,altura):
    '''
    Calcular el area
    Recibe altura y base
    Retorna area
    '''

    area = (base * altura) / 2

    return area
print(calcular_area_triangulo(6,6))