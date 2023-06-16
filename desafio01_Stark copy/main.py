#César Pumacayo 1°E grupo Giovanni
from funciones_stark import *
import json
import csv


lista_heroes =[
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
 {
   "nombre": "Rocket Raccoon",
   "identidad": "Rocket Raccoon",
   "empresa": "Marvel Comics",
   "altura": "122.77",
   "peso": "25.73",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Brown",
   "fuerza": "5",
   "inteligencia": "average"
 }
]

rutaJSON = "desafio01_Stark copy\\data_stark.json"
lista_heroes = leer_archivo(rutaJSON)


while True:
    respuesta = int(input(                        
                        "1 - Ingresar Parte 2 (modificacion del desafio #0) del Desafio Stark\n"
                        "2 - Ingresar Parte 5 (modificacion del desafio #1) del Desadio Stark\n"
                        "3 - Ingresar Parte 6 del Desafio Stark\n"
                        "------------------------Parte 1--------------------------\n"
                        "8 - Mostrar el nombre de todo los superheroes de genero M\n"
                        "9 - Mostrar el nombre de todo los superheroes de genero F\n" 
                        "10 - Mostrar el superheroe con mas altura de genero Masculino\n"
                        "11 - Mostrar el superheroe con mas altura de genero Femenino\n"
                        "12 - Mostrar el superheroe con menos altura de genero Masculino\n"
                        "13 - Mostrar el superheroe con menos altura de genero Femenino\n"
                        "14 - Mostrar el promedio de la altura del genero Masculino\n"
                        "15 - Mostrar el promedio de la altura del genero Femenino\n"
                        "16 - Mostrar cuántos superheroes tienen cada tipo de color de ojos\n"
                        "17 - Mostrar cuántos superhéroes tienen cada tipo de color de pelo\n"
                        "18 - Mostrar cuántos superhéroes tienen cada tipo de inteligencia\n"
                        "19 - Mostrar todos los superhéroes agrupados por color de ojos\n"
                        "20 - Mostrar todos los superhéroes agrupados por color de pelo\n"
                        "21 - Mostrar todos los superhéroes agrupados por tipo de inteligencia\n"
                        "------------------------Parte 2--------------------------\n"
                        "22- SALIR.\n"))
    match(respuesta):
        case 1:
            stark_marvel_app(lista_heroes)
        case 2:
            stark_marvel_app_5(lista_heroes) # Parte 5
        case 3:
            menu()
        case 8:
            print_genero(lista_heroes, genero="M")
        case 9:
            print_genero(lista_heroes, genero="F")
        case 10:
            imprimir_dato(calcular_mas_menos_por_clave_genero(lista_heroes, genero="M"))
        case 11:
            imprimir_dato(calcular_mas_menos_por_clave_genero(lista_heroes, genero="F"))
        case 12:
            imprimir_dato(calcular_mas_menos_por_clave_genero(lista_heroes, genero= "M", maximo=False))
        case 13:
            imprimir_dato(calcular_mas_menos_por_clave_genero(lista_heroes, genero="F", maximo=False))     
        case 14:
            imprimir_dato(mostrar_altura_promedio_por_genero(genero="M"))
        case 15:
            imprimir_dato(mostrar_altura_promedio_por_genero(genero="F"))
        case 16:
            ojos = contar_tipo_superheroes(lista_heroes , tipo_clave="color_ojos")
            print_tipos_contador(ojos,clave="ojo")
        case 17:
            pelos = contar_tipo_superheroes(lista_heroes , tipo_clave="color_pelo")
            print_tipos_contador(pelos,clave="pelo")
        case 18:
            inteligencia= contar_tipo_superheroes(lista_heroes, tipo_clave= "inteligencia")
            print_tipos_contador(inteligencia, clave="inteligencia")
        case 19:
            dict_resultado_ojos = agrupar_tipo_superheroes(lista_heroes, tipo_clave="color_ojos")
            print_tipos_agrupados(dict_resultado_ojos)
        case 20:
            dict_resultado_pelos = agrupar_tipo_superheroes(lista_heroes, tipo_clave="color_pelo")
            print_tipos_agrupados(dict_resultado_pelos)
        case 21:
            dict_resultado_inteligencia = agrupar_tipo_superheroes(lista_heroes, tipo_clave="inteligencia")
            print_tipos_agrupados(dict_resultado_inteligencia)
        case 22:
            break
        case _:
            imprimir_dato("\nError, reingrese la opcion correcta\n")


    input("\nPulse enter para continuar\n")




