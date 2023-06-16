#Ejercicios del Dict( Diccionario)
#Ejercicio 1
#Crea un diccionario que represente los días de la semana, donde las claves son los nombres de los días y
#  los valores son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor correspondiente al día "miércoles".

# diccionario = {"lunes": 1 , "martes": 2 , "miercoles": 3 , "Jueves": 4 , "Viernes":5 , "Sabado" : 6, "Domingo": 7}

# print(diccionario["miercoles"])






#Ejercicio 2
#Crea un diccionario que represente los meses del año, donde las claves son los nombres de los meses y
# los valores son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el número correspondiente al mes "julio".


# diccionario = {"enero":1 ,"febrero": 2,"marzo": 3,"abril": 4,"mayo": 5,"junio": 6,"julio": 7,"agosto": 8,"septiembre": 9,"octubre": 10,"noviembre": 11, "diciembre": 12}

# print(diccionario["julio"])





#Ejercicio 3
#Crea un diccionario que contenga la información de una película, como título, director y año de estreno. Luego, imprime el título de la película.

# diccionario = {"titulo": "Interestelar", "director": "Christopher Nolan", "año_estreno": 2014}

# print(diccionario["titulo"])




#Ejercicio 4
#Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, código postal, 
# partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.

# diccionario= {"calle": "lobos", "altura": 23,"localidad": "Villa celina", "codigo_postal": 1423, "partido": "La matanza" , "provincia": "Buenos aires"}
# print(diccionario["calle"],diccionario["altura"])




#Ejercicio 5
#Crea un diccionario que represente los continentes, donde las claves son los nombres de los continentes y 
#los valores son los números correspondientes (por ejemplo, {"América": 1, "Europa": 2, ...}). Imprime el valor correspondiente al continente "África".

# diccionario = {"Africa": 1, "America": 2 , "Asia": 3, "Antartida": 4, "Europa": 5, "Oceanía": 6}
# print(diccionario["Africa"])




#Ejercicio 6
#Crea un diccionario que represente las estaciones del año, donde las claves son los nombres de las estaciones y
# los valores son los números correspondientes (por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el valor correspondiente a la estación "invierno".

# diccionario={"primavera": 1, "verano": 2, "otoño": 3, "invierno": 4}
# print(diccionario["invierno"])




#Ejercicio 7
#Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.

# diccionario = {"titulo": "Burning heart", "artista": "Survivor", "duracion": "3:51"}
# print(diccionario["duracion"])




#Ejercicio 8
#Crea un diccionario que represente las edades de varias personas, donde las claves son los nombres de las personas y
# los valores son sus edades. Imprime la edad de la persona más joven.

# diccionario= {"Carlos": 21, "Pablo": 19 , "Joaquin": 34}

# edadMasJoven = min(diccionario.values())

# print("La edad de la persona más joven es:", edadMasJoven)





#Ejercicio 9
#Crea un diccionario que contenga las capitales de los países de América del Sur. 
# Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

# capitales = {
#     "Argentina": "Buenos Aires",
#     "Bolivia": "La Paz / Sucre",
#     "Brasil": "Brasilia",
#     "Chile": "Santiago",
#     "Colombia": "Bogotá",
#     "Ecuador": "Quito",
#     "Guyana": "Georgetown",
#     "Paraguay": "Asunción",
#     "Perú": "Lima",
#     "Suriname": "Paramaribo",
#     "Uruguay": "Montevideo",
#     "Venezuela": "Caracas"
# }

# nombre= input("Ingrese un pais de america del sur: ")

# for i in capitales:
#     if i == nombre.capitalize():
#         print(capitales[i])





#Ejercicio 10
#Crea un diccionario que represente las notas de un examen de varios estudiantes,
# donde las claves son los nombres de los estudiantes y los valores son sus notas. Imprime el promedio de las notas.

# acumulador=0

# diccionario = {
#     "Juan": 7,
#     "Maria": 6,
#     "Santiago": 8,
#     "Roberto":1
# }

# for i in diccionario:
#     acumulador+=diccionario[i]

# promedio = acumulador / len(diccionario) 


# print("El promedio de las notas es {}".format(promedio))






#Ejercicio 11
#Crea un diccionario que represente una lista de tareas por hacer. Cada clave del diccionario debe ser el nombre de una tarea y
# cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado

# diccionario = {
#     "Trapear": "pendiente",
#     "Lavar platos": "completada",
#     "Estudiar": "en proceso",
#     "Comprar carne": "completada",
#     "Ver clases grabadas": "pendiente"
# }

# for clave, valor in diccionario.items(): 
#     print("{0} : {1}".format(clave,valor))






#Ejercicio 12
#Crea un diccionario que represente una lista de las compras. Cada clave del diccionario debe ser el nombre de un producto y cada valor debe ser su cantidad.
# Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad


# dict_compras= {
#     "leche": 3,
#     "caja":2,
#     "carne":4,
#     "arroz":1,
#     "lechuga":2,
#     "coca cola":1
# }

# nombre= input("Ingrese el producto que desea: ")

# if nombre in dict_compras:
#     print(f"La cantidad de {nombre} que necesita es: {dict_compras[nombre]}")
# else:
#     print(f"Lo siento, {nombre} no está en la lista de compras")




#Ejercicio 13
#Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa. 
# Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres


# diccionario_juegos = {"Ajedrez": 5, 
#                        "Risk": 8, 
#                        "Catan": 6, 
#                        "Monopoly": 4, 
#                        "Scrabble": 7}


# nombre= int(input("Ingrese nivel de dificultad: "))

# for juego, dificultad in diccionario_juegos.items():
#     if dificultad == nombre:
#         print(juego)   






#Ejercicio 14
#Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego. 
# Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.

# diccionario= {"Juan": 5,
#               "Carlos":8,
#               "Joaco": 10,
#               "Miguel": 5,
#               "Enzo":6
#               }

# nombre =input("Ingrese el nombre del jugador: ")
# nuevo_puntaje=int(input("Ingrese un nuevo puntaje: "))

# if nombre in diccionario:
#     diccionario[nombre] = nuevo_puntaje

# for clave, valor in diccionario.items():
#     print("{0} : {1}".format(clave, valor))





#Ejercicio 15
#Crea un diccionario que contenga el nombre y el sueldo de varios empleados.
#  Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.


# diccionario= {"Juan": 5000,
#               "Carlos":800,
#               "Joaco": 1000,
#               "Miguel": 50,
#               "Enzo":60000
#               }

# nombre =input("Ingrese el nombre del jugador: ")
# aumento= int(input("Ingrese el aumento que usted quiere: "))
# if nombre in diccionario:
#     diccionario[nombre] += aumento 
#     print("El nuevo sueldo de {0} es: {1}".format(nombre, diccionario[nombre]))
# else:
#     print("El empleado no está en la lista.")

# for clave, valor in diccionario.items():
#     print("{0}: {1}".format(clave,valor))


 
    

#Ejercicio 16
#Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y los valores son "True" si están completadas y 
# "False" si no lo están. 
# Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes


# diccionario = {
#     "Trapear": True,
#     "Lavar": False,
#     "Estudiar": True,
#     "Comprar": False,
#     "Correr": True
# }

# nombre_tarea= input("Ingrese el nombre de una tarea especifica: ")
# nombre_tarea= nombre_tarea.capitalize()
       
# while True:
#     modificado = input("Ingrese True para marcarlo como ocupado o False para marcarlo como libre: ")
#     if modificado.capitalize() == "True" or modificado.capitalize() == "False":
#         break
#     else:
#         print("Entrada inválida. Ingrese True o False.")

# if nombre_tarea in diccionario:
#     if diccionario[nombre_tarea] == True:
#         print("La tarea ya está marcada como completada.")
#     else:
#         diccionario[nombre_tarea] = True
        
#         print("La tarea {0} ha sido marcada como completada.".format(nombre_tarea))


# print("\nTareas pendientes:")
# for clave, valor in diccionario.items():
#     if valor == False:
#         print("{0}: {1}".format(clave, valor))

# print("\nTareas completadas:")
# for clave, valor in diccionario.items():
#     if valor == True:
#         print("{0}: {1}".format(clave, valor))
        





#Ejercicio 17
#Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y 
# los valores son los horarios correspondientes. Modifica el horario de la película "Avengers: Endgame" a las 19:30.

# diccionario_peliculas= {"Iron man": "19:30",
#                         "Hell boy": "21:30",
#                         "Resident evil":"16:30",
#                         "Avengers: Endgame":"12:00",
#                         "Overwatch": "15:00" 
#                         }

# print("\t\t\tDiccionario Original: ")
# for clave, valor in diccionario_peliculas.items():
#     print("{0}:{1}".format(clave,valor))

# print("\t\t\tDiccionario modificado: ")
# for clave, valor in diccionario_peliculas.items():

#     diccionario_peliculas["Avengers: Endgame"]= "19:30"
#     print("{0}:{1}".format(clave,valor))






#Ejercicio 18
#Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y 
# los valores son las puntuaciones correspondientes. Solicita al usuario el nombre de un juego y luego su puntuación, 
# si el juego no existe agregarlo y si existe actualizar su puntuación 


# diccionario_juegoConsola= {"Resident Evil":10,
#                            "Call of duty": 6,
#                            "Overwatch":8,
#                            "Minecraft":9,
#                            "Fifa":10
#                            }


# nombre= input("Ingrese el nombre del juego: ")
# puntuacion= int(input("Ingrese nueva puntuacion: "))

# if nombre in diccionario_juegoConsola:
#     diccionario_juegoConsola[nombre]= puntuacion
# else:
#     diccionario_juegoConsola[nombre]= puntuacion

# for clave, valor in diccionario_juegoConsola.items():
#     print("{0}:{1}".format(clave,valor))



#Ejercicio 19
#Crea un diccionario que represente las temperaturas de una ciudad durante una semana, 
# donde las claves son los días de la semana y los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana.

# diccionario_temperatura = {"lunes": 34,
#                            "Martes": 28,
#                            "Miercoles": 34,
#                            "Jueves": 42,
#                            "Viernes": 25,
#                            "Sabado": 19,
#                            "Domingo": 20
#                            }

# acumulador = 0
# for i in diccionario_temperatura:
    
#     acumulador+= diccionario_temperatura[i]


# promedio = acumulador / len(diccionario_temperatura)

# print("El promedio de la temperatura de la semana es {0}".format(promedio))






#Ejercicio 20
#Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos 
# y los valores son "True" si están ocupados y "False" si no lo están.
#  Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres

# dict_asientos_avion = {
#     1: False,
#     2: False,
#     3: True,
#     4: True,
#     5: False,
#     6: False,
#     7: True,
#     8: True,
#     9: False,
#     10: False
# }

# numero = int(input("Ingrese el numero de asiento que desea modificar:"))

# # validar entrada del usuario para condicion
# while True:
#     condicion = input("Ingrese True para marcarlo como ocupado o False para marcarlo como libre: ")
#     if condicion.capitalize() == "True" or condicion.capitalize() == "False":
#         break
#     else:
#         print("Entrada inválida. Ingrese True o False.")

# condicion = condicion.capitalize()

# if numero in dict_asientos_avion:
#     if condicion == "True":
#         dict_asientos_avion[numero]=True
#     else:
#         dict_asientos_avion[numero]=False
#     print("El asiento {0} ha sido marcado como {1}.".format(numero, condicion))

# print("\nAsientos libres:")
# for clave, valor in dict_asientos_avion.items():
#     if valor == False:
#         print("{0}: {1}".format(clave, valor))





#Ejercicio 21
#Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y 
# los valores son los gastos correspondientes. Calcula el total de gastos de la persona.

# acumulador=0
# dict_gastos = {
#     'comida': 5000,
#     'transporte': 2000,
#     'entretenimiento': 3000,
#     'salud': 1500,
#     'ropa': 2500
# }

# for i in dict_gastos:
#     acumulador+= dict_gastos[i]

# print(acumulador)








#Ejercicio 22
#Crea un diccionario que represente los gastos de una persona en diferentes categorías,
#  donde las claves son los nombres de las categorías y los valores son los gastos correspondientes. 
# Calcula el total de gastos de la persona en el mes.



# acumulador=0
# dict_gastos = {
#     'comida': 5000,
#     'transporte': 2000,
#     'entretenimiento': 3000,
#     'salud': 1500,
#     'ropa': 2500
# }

# for i in dict_gastos:
#     acumulador+= dict_gastos[i]

# print(acumulador)







#Ejercicio 23
#Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas y
#  los valores son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: 
# agregarlo al diccionario en caso de que no exista. En caso de que exista modificar el número de teléfono del contacto.


dict_contactos = {
    'Juan': '555-1234',
    'Maria': '555-5678',
    'Pedro': '555-9012',
    'Laura': '555-3456',
    'Luis': '555-7890'
}

for clave, valor in dict_contactos.items():
    print("{0}:{1}".format(clave,valor))


nombre = input("Ingrese un nombre del diccionario ").capitalize()

if nombre in dict_contactos:
    
    modificar= input("Este nombre esta en el diccionario.Ahora modifique el número de teléfono del contacto (recuerda el '-'): ")
    dict_contactos[nombre] = modificar
else:

    modificar= input("Lo que ingresaste no esta en el diccionario. Igual lo agregamos. Ingrese el número de teléfono del contacto (recuerda el '-'): ")
    dict_contactos[nombre]= modificar

for clave, valor in dict_contactos.items():
    print("{0}:{1}".format(clave,valor))

