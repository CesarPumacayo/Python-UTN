
#Ejercicio 14
# Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, 
# el valor máximo y el promedio de los números en la lista.

def mostrar_valor_max_min_promedio(lista_numeros):
    diccionario={}
    numero_min=0
    numero_max=0
    acumulador=0
    for i in range(len(lista_numeros)):
        acumulador+= lista_numeros[i]
        if lista_numeros[i] < lista_numeros[numero_min]:
            numero_min = i
            
        if lista_numeros[i] > lista_numeros[numero_max]:
            numero_max = i
    promedio = acumulador / len(lista_numeros)

    diccionario["numero minimo"]= lista_numeros[numero_min]
    diccionario["numero maximo"] = lista_numeros[numero_max]
    diccionario["promedio"] = promedio

    return diccionario

print(mostrar_valor_max_min_promedio([2,6,22,41,1,9]))