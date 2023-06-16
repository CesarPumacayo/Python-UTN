#LISTA PARALELAS : DISTINTAS LISTAS DE ID , NOMBRE , EDAD , MEMBRESIA

# lista_identificacion=[1,2,3,4]
# lista_nombre=["Cesar","Juan","Diego","Carlos"]
# lista_edad= [20,19,32,41]
# lista_membresia= ["anual","mensual","mensual", "anual"]

# # while True:
#     # identificacion= int(input("Ingrese el numero de identificacion: "))
#     # nombre = input("Ingrese el nombre: ")
#     # edad= int(input("Ingrese la edad: "))
#     # tipoMembresia = input("Ingrese el tipo de membresia: ")
#     # while tipoMembresia != "mensual" and tipoMembresia != "anual":
#     #     print("Error, no ingresaste el tipo correcto.")
#     #     tipoMembresia = input("Ingrese el tipo de membresia NUEVAMENTE: ")

#     # respuesta = input("Desea continuar? si o no")
#     # if respuesta == "no":
#     #     break
# texto_busqueda= input("Que buscas? ")

# indice_busqueda= None
# for indice in range(len(lista_identificacion)):
#     if lista_nombre[indice] == texto_busqueda:
#         indice_busqueda= indice
#         break
# # indice= 1  #range

# # if indice < len(lista_identificacion):

# if indice_busqueda != None and indice_busqueda < len(lista_identificacion):
#     print("ID: {0} Nombre: {1} Edad: {2} Membresia: {3}".format(lista_identificacion[indice_busqueda],
#                                                                 lista_nombre[indice_busqueda],
#                                                                 lista_edad[indice_busqueda], 
#                                                                 lista_membresia[indice_busqueda],
#                                                                 ))






miembro_identificacion=[1,2,3,4]
miembro_nombre=["Cesar","Juan","Diego","Carlos"]
miembro_edad= [20,19,32,41]
miembro_membresia= ["anual","mensual","mensual", "anual"]


lista_de_miembros= [{"id": 100,"nombre":"JUAN", "edad": 22,"membresia": "ANUAL" },
                    {"id": 200,"nombre":"VERONICA", "edad": 35,"membresia": "MENSUAL"},
                    ]


#Diccionario vacio y agrega con el .append()

auxiliar_miembro = {}
auxiliar_miembro["id"]= 300
auxiliar_miembro["nombre"]= "PEDRO"
auxiliar_miembro["edad"]= 20
auxiliar_miembro["membresia"]= "MENSUAL"

lista_de_miembros.append(auxiliar_miembro)

indice_busqueda = 1
#MUESTRA UNO SOLO
print("ID: {0} Nombre: {1} Edad: {2} Membresia: {3}".format(lista_de_miembros[indice_busqueda]["id"],
                                                            lista_de_miembros[indice_busqueda]["nombre"],
                                                            lista_de_miembros[indice_busqueda]["membresia"], 
                                                            lista_de_miembros[indice_busqueda]["edad"],
                                                            ))

#RECORRE TODOS
for miembro in lista_de_miembros:
    print("ID: {0} Nombre: {1} Edad: {2} Membresia: {3}".format(miembro["id"],
                                                            miembro["nombre"],
                                                            miembro["membresia"], 
                                                            miembro["edad"],
                                                            ))





