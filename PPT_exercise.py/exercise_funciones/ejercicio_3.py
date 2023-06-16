#César Pumacayo 1°E grupo giovanni

#Ejercicio 3
# Crear una función que calcule el descuento aplicado a un producto. 
# Recibe dos parámetros (precio original y precio con descuento) y 
# devuelve el porcentaje de descuento aplicado.


def porcentaje_descuento(precio_original, precio_descuento):
    '''
    Calcula el porcentaje del descuento aplicado
    Recibe precio descuento y el precio original
    Retorna el porcentaje
    '''
    descuento = precio_original - precio_descuento
    porcentaje = (descuento / precio_original) * 100
    return porcentaje


print(porcentaje_descuento(2500, 50)) # 98.0
