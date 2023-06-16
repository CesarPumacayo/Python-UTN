#Funciones.
#César Pumacayo 1°E grupo giovanni
#Ejemplo:


# def calcular_promedio(lista):
#     """
#     Calcula el promedio de una lista de números.


#     Parámetros:
#     lista (list): Una lista de números.


#     Devuelve:
#     float: El promedio de la lista.
#     """
#     suma = sum(lista)
#     promedio = suma / len(lista)
#     return promedio


#Ejercicio 1:
#Crear una función que convierta grados Celsius a grados Fahrenheit. Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

def celsius_a_fahrenheit(grados_celsius):
    '''
    Convertir y mostrar celsius a fahrenheit
    Recibe grados celsius
    Retorna grados fahrenheit

    '''
    grados_fahrenheit = (9/ 5 * grados_celsius) + 32
    return grados_fahrenheit
print(celsius_a_fahrenheit(224)) # devuelve 435.2
