#César Pumacayo 1°E grupo giovanni

#Ejercicio 11
#Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.

def contar_vocales(cadena_texto):
    vocales = "aeiou"
    cantidad_vocales = 0
    for letra in cadena_texto:
        if letra.lower() in vocales:
            cantidad_vocales += 1
    return cantidad_vocales
print(contar_vocales("Heimerdinger"))