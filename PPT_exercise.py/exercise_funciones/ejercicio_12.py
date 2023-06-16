#César Pumacayo 1°E grupo giovanni


#Ejercicio 12
#Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas

def mostrar_elementos_iguales(lista_nombres1, lista_nombres2):
    lista_iguales=[]
     
    for nombre in lista_nombres1:
        if nombre in lista_nombres2:
            lista_iguales.append(nombre)
    return lista_iguales


print(mostrar_elementos_iguales(["telefono", "roberto", "caja", "ropero","desierto"], ["caramelo", "caja", "carpeta", "roberto","vino","telefono"]))