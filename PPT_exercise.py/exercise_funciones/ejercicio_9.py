#César Pumacayo 1°E grupo giovanni

#Ejercicio 9
#Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
# Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.

def mostrar_cantidad_elemento_lista(lista, elemento):
    contador=0
    for i in range(len(lista)):
        if lista[i] == elemento:
            contador+=1


    return contador
print(mostrar_cantidad_elemento_lista([2,4,4,6,8,1],4))