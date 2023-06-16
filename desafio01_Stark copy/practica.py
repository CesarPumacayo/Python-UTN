#César Pumacayo 1°E Grupo Giovanni
# Ejercicio simulacro de parcial
import json
import csv
import re
from funciones_stark import *
rutaJSON = "desafio01_Stark copy\\data_stark.json"
lista_heroes = leer_archivo(rutaJSON)
stark_normalizar_datos(lista_heroes)


def nombrar_lista_N(lista_heroes:list, rango:int)->list:
    '''
    Esta funcion lista y nombra los superheroes que no supere maximo rango

    Parametros:
    - lista_heroes(list): Lista de diccionarios, cada diccionario representa un heroe de marvel
    - rango(int): Es el rango maximo que puede alcanzar la lista

    Retorna:

    - lista_nombre: Lista de superheroes hasta el rango 
    '''
    lista_nombre=[]
    rango = min(rango, len(lista_heroes))
    for i in range(rango):
        lista_nombre.append(lista_heroes[i]['nombre'])

    return lista_nombre


def ordenar_por_altura(lista_heroes:list, condicion:bool)->list:
    """
    Esta funcion ordena la lista de héroes, por altura de menor a mayor o viceversa (según lo ingresado) y devuelve una lista con las alturas ordenadas.

    Parametros:
    - lista_heroes: Lista de diccionarios 
    - condicion: bool (True o False)

    Retorna:

    -Devuelve una lista de alturas.
    """
    rango = len(lista_heroes)
    for indice in range(rango - 1):
        for heroes in range(rango - indice - 1):
            if  condicion == False and lista_heroes[heroes]["altura"] < lista_heroes[heroes+1]["altura"] or condicion == True and lista_heroes[heroes]["altura"] > lista_heroes[heroes+1]["altura"]:
                lista_heroes[heroes],lista_heroes[heroes+1] = lista_heroes[heroes+1],lista_heroes[heroes]
    return [heroe["altura"] for heroe in lista_heroes]

def ordenar_listar_por_fuerza(lista_heroes, condicion):
    """
    Esta funcion ordena la lista de héroes, por fuerza de menor a mayor o viceversa (según lo ingresado) y devuelve una lista con las alturas ordenadas.

    Parametros:
    - lista_heroes: Lista de diccionarios 
    - condicion: bool (True o False)

    Retorna:

    -Devuelve una lista de fuerza.
    """
    rango = len(lista_heroes)
    for indice in range(rango - 1):
        for heroes in range(rango - indice - 1):
            if  condicion == False and lista_heroes[heroes]["fuerza"] < lista_heroes[heroes+1]["fuerza"] or condicion == True and lista_heroes[heroes]["fuerza"] > lista_heroes[heroes+1]["fuerza"]:
                lista_heroes[heroes],lista_heroes[heroes+1] = lista_heroes[heroes+1],lista_heroes[heroes]
    return [heroe["fuerza"] for heroe in lista_heroes]


def calcular_promedio_key(lista_heroes:list, key:str, condicion:bool)->list:
    '''
    Esta funcion calcula el promedio y lo lista segun la key y condicion  

    Parametros: 
    - lista_heroes: lista de diccionarios
    - key: el tipo de clave key numerica
    - condicion: bool True o False

    Retorna: 

    - lista_promedio: lista segun key que puede ser mayor o menor de la condicion

    '''

    acumulador=0
    contador=0
    lista_promedio=[]
    
    for indice in lista_heroes:
        if key in indice:
            if type(indice[key]) == type(int()) or type(indice[key]) == type(float()):
                acumulador+= indice[key]
                contador+=1
    if contador > 0:
        promedio = acumulador / contador

    for indice in lista_heroes:
        if condicion == True and indice[key] > promedio or condicion == False and indice[key] < promedio:
            lista_promedio.append(indice[key])

    return lista_promedio
            

# print(calcular_promedio_key(lista_heroes, "altura"))


def buscar_heroes_inteligencia(lista_heroes, tipo_busqueda):
    '''
    Esta funcion busca "good" "high" o "average" en inteligencia y lo lista

    Parametros: 
    - Lista_heroes: lista de diccionarios
    - tipo_busqueda: el good , high o average que ingresaste
    
    '''
    lista_vac= []
    for indice in lista_heroes:
        if re.search(tipo_busqueda, indice["inteligencia"]):
            lista_vac.append(indice["nombre"])
    return lista_vac


def input_ingreso_asc_des():
    condicion= input("Ingrese como lo quiere ordenar: Ascendente (asc) o Descendente(desc)")

    while condicion != "asc" and condicion != "desc":
        print("ERROR. Reingrese la condición: Ascendente (asc) o Descendente (desc)")
        condicion = input("Ingrese cómo quiere ordenar: Ascendente (asc) o Descendente (desc)")

    if condicion == "asc":
        condicion = True
    elif condicion == "desc":
        condicion = False
    return condicion

# def guardar_csv(lista_original: list, path: str):
#     if len(lista_original) == 0:
#         print("Lista vacía.")
#         return -1

#     lista = lista_original[:]
#     lista_heroes_string = []
#     for heroe in lista:
#         dato_heroe = [str(value) for value in heroe.values()]
#         dato_heroe_string = ",".join(dato_heroe)
#         lista_heroes_string.append(dato_heroe_string)

#     datos_para_csv = "\n".join(lista_heroes_string)
#     with open(path, "w") as archivo:
#         archivo.write(datos_para_csv)
#         print("El archivo fue creado en {0}".format(path))


def guardar_csv(lista_usuarios: list, ruta: str):
    with open(ruta, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['lista'])  # Escribir encabezado en el archivo CSV

        for usuario in lista_usuarios:
            escritor.writerow([usuario])



def condicionales():
    condicion = input("Ingrese lista promedio mayor o menor: ")
    while condicion != "mayor" and condicion != "menor":
        condicion = input("ERROR, Reingrese lista promedio mayor o menor: ")
            
    if condicion == "mayor":
        condicion = True
    else:
        condicion = False

    return condicion



ultima_lista_generada = []

def menu():
    opcion = 0
    while opcion != 6:
        print("Menú de tipo parcial:\n"
                "1. Listar numeros N/ Heroes\n"
                "2. Ordenar y listar heroe por altura\n"
                "3. Ordenar y listar heroe por fuerza\n"
                "4. Calcular promedio key numérica (mayor o menor)\n"
                "5. Buscar héroes por inteligencia y listar [good, average, high]\n"
                "6. Exportar CSV segun la opcion que elijas (1-4) \n"
                "7. Salir\n"
        )
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            rango = int(input("Ingrese un rango: "))
            lista_nueva = nombrar_lista_N(lista_heroes, rango)
            ultima_lista_generada = lista_nueva[:]
            print(lista_nueva)
            
        elif opcion == 2:
            booleano = input_ingreso_asc_des()
            
            lista_nueva = ordenar_por_altura(lista_heroes, booleano)
            ultima_lista_generada = lista_nueva[:]
            print(lista_nueva)
            
        elif opcion == 3:
            booleano = input_ingreso_asc_des()
            lista_nueva= ordenar_listar_por_fuerza(lista_heroes, booleano)
            ultima_lista_generada = lista_nueva[:]
            print(lista_nueva)
            
        elif opcion == 4:
            
            lista_nueva = calcular_promedio_key(lista_heroes,key="altura", condicion=condicionales())
        elif opcion ==5:
            tipo_busqueda= input("Ingrese el tipo de busqueda segun inteligencia: good , high , average: ")
            if re.search(r'good|average|high', tipo_busqueda):
                lista_nueva = buscar_heroes_inteligencia(lista_heroes, tipo_busqueda)
                ultima_lista_generada = lista_nueva[:]
                print(lista_nueva)
        elif opcion == 6:
            numero= int(input("Ingrese la opcion de deseas [1-4]: "))
            if re.match("^[1-4]$", str(numero)):
                guardar_csv(ultima_lista_generada, "data.csv")
            else:
                print("Error, ingresaste un número no deseado")
        elif opcion == 7:
            print("Saliendo...")
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()


