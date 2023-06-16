#César Pumacayo 1°E grupo giovanni

#Ejercicio 13
#Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.

def crear_diccionario_longitudes(lista_palabras):
    diccionario = {}
    for palabra in lista_palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

print(crear_diccionario_longitudes(["mochila", "Javascript", "Notebook", "Python"]))

