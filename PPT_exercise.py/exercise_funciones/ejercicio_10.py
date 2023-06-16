#César Pumacayo 1°E grupo giovanni

#Ejercicio 10
#Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.

def palabra_mas_larga(lista_palabras):
    mas_largo = lista_palabras[0]
    for palabra in lista_palabras:
        if len(palabra) > len(mas_largo):
            mas_largo = palabra
    return mas_largo

print(palabra_mas_larga(["vicuña", "animaciones", "Javascript" , "Python", "Heimerdinger"]))