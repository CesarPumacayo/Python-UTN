#César Pumacayo 1°E grupo giovanni

#Ejercicio 4
# Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.

def promedio_grupo(lista_edades):
    '''
    Calcular el promedio de un grupo de personas
    Recibe lista edades
    Retorna promedio
    '''

    promedio = sum(lista_edades) / len(lista_edades)

    return promedio 
print(promedio_grupo([1, 45, 23, 12]))



