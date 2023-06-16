# Ejercicio tipo parcial
import json
import csv
import re
from funciones_stark import *
rutaJSON = "desafio01_Stark copy\\data_stark.json"
lista_heroes = leer_archivo(rutaJSON)
stark_normalizar_datos(lista_heroes)


def guardar_archivo(nombre_archivo: str, contenido: str)->bool:
    try:
        with open(nombre_archivo, 'w+') as archivo:
            archivo.write(contenido)
        print(f'Se creó el archivo: {nombre_archivo}')
        return True
    except:
        print(f'Error al crear el archivo: {nombre_archivo}')
        return False


# Función para listar los primeros N héroes
def listar_primeros_n_heroes(lista_heroes, n):
    n = min(n, len(lista_heroes))
    for i in range(n):
        print(f"{i+1}. {lista_heroes[i]['nombre']}")

# Función para ordenar y listar héroes por una clave específica
def ordenar_y_listar_heroes(lista_heroes, clave, orden):
    ordenado = sorted(lista_heroes, key=lambda hero: hero[clave], reverse=(orden == 'desc'))
    for hero in ordenado:
        print(f"{hero['nombre']}: {hero[clave]}")

# Función para calcular el promedio de una clave numérica y filtrar los héroes según una condición
def calcular_promedio_y_filtrar(lista_heroes, clave, condicion):
    valores = [hero[clave] for hero in lista_heroes]
    promedio = sum(valores) / len(valores)

    if condicion == 'menor':
        filtrados = [hero for hero in lista_heroes if hero[clave] < promedio]
    elif condicion == 'mayor':
        filtrados = [hero for hero in lista_heroes if hero[clave] > promedio]
    else:
        filtrados = []

    for hero in filtrados:
        print(f"{hero['nombre']}: {hero[clave]}")

# Función para buscar héroes por inteligencia
def buscar_heroes_por_inteligencia(lista_heroes, inteligencia):
    regex = re.compile(inteligencia, re.IGNORECASE)
    resultados = [hero for hero in lista_heroes if regex.search(hero['inteligencia'])]
    for hero in resultados:
        print(f"{hero['nombre']}: {hero['inteligencia']}")

# Función para exportar la lista de héroes ordenada a un archivo CSV
def exportar_a_csv(lista_heroes, clave):
    ordenado = sorted(lista_heroes, key=lambda hero: hero[clave])
    nombre_archivo = f"superheroes_ordenados_por_{clave}.csv"

    with open(nombre_archivo, 'w', newline='') as csvfile:
        fieldnames = lista_heroes[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ordenado)

    print(f"La lista de héroes ordenada por {clave} ha sido exportada a {nombre_archivo}.")

# Función para mostrar el menú y realizar las operaciones seleccionadas
def mostrar_menu():
    while True:
        print("----- Menú -----")
        print("1. Listar los primeros N héroes")
        print("2. Ordenar y listar héroes por altura")
        print("3. Ordenar y listar héroes por fuerza")
        print("4. Calcular promedio de una clave numérica y filtrar")
        print("5. Buscar héroes por inteligencia")
        print("6. Exportar a CSV la lista de héroes ordenada")
        print("0. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == '0':
            break

        elif opcion == '1':
            n = input("Ingrese la cantidad de héroes a listar: ")
            if re.fullmatch(r'\d+', n):
                n = int(n)
                listar_primeros_n_heroes(lista_heroes, n)
            else:
                print("¡Ingrese un número válido!")

        elif opcion == '2':
            orden = input("Ingrese el orden ('asc' o 'desc'): ")
            if re.fullmatch(r'asc|desc', orden):
                ordenar_y_listar_heroes(lista_heroes, 'altura', orden)
            else:
                print("¡Ingrese un orden válido!")

        elif opcion == '3':
            orden = input("Ingrese el orden ('asc' o 'desc'): ")
            if re.fullmatch(r'asc|desc', orden):
                ordenar_y_listar_heroes(lista_heroes, 'fuerza', orden)
            else:
                print("¡Ingrese un orden válido!")

        elif opcion == '4':
            clave = input("Ingrese la clave numérica: ")
            if clave in lista_heroes[0]:
                condicion = input("Ingrese la condición ('menor' o 'mayor'): ")
                if re.fullmatch(r'menor|mayor', condicion):
                    calcular_promedio_y_filtrar(lista_heroes, clave, condicion)
                else:
                    print("¡Ingrese una condición válida!")
            else:
                print("¡La clave ingresada no es válida!")

        elif opcion == '5':
            inteligencia = input("Ingrese el nivel de inteligencia ('good', 'average', 'high'): ")
            if re.fullmatch(r'good|average|high', inteligencia):
                buscar_heroes_por_inteligencia(lista_heroes, inteligencia)
            else:
                print("¡Ingrese un nivel de inteligencia válido!")

        elif opcion == '6':
            clave = input("Ingrese la clave para ordenar y exportar a CSV: ")
            if clave in lista_heroes[0]:
                exportar_a_csv(lista_heroes, clave)
            else:
                print("¡La clave ingresada no es válida!")

        else:
            print("¡Opción no válida!")

# Ejecutar el menú
mostrar_menu()
