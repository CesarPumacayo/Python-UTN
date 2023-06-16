# lista_personajes =[
#  {
#    "nombre": "Howard the Duck",
#    "identidad": "Howard (Last name unrevealed)",
#    "empresa": "Marvel Comics",
#    "altura": "79.349999999999994",
#    "peso": "18.449999999999999",
#    "genero": "M",
#    "color_ojos": "Brown",
#    "color_pelo": "Yellow",
#    "fuerza": "2",
#    "inteligencia": "average"
#  },
#  {
#    "nombre": "Rocket Raccoon",
#    "identidad": "Rocket Raccoon",
#    "empresa": "Marvel Comics",
#    "altura": "122.77",
#    "peso": "25.73",
#    "genero": "M",
#    "color_ojos": "Brown",
#    "color_pelo": "Brown",
#    "fuerza": "5",
#    "inteligencia": "average"
#  }
# ]



# # #lee tu codigo segun lo que estas mandando
# # def listar_por_caracteristicas(lista:list[dict], caracteristica:str)->None:
# #     for element in lista:
# #         print(element[caracteristica])


# # listar_por_caracteristicas(lista_personajes, "nombre")

# # for personajes in lista_personajes:
# #     print(personajes["nombre"], personajes["altura"])

# # primer_personaje = lista_personajes[0]
# # altura= float(primer_personaje)



# #--------------------------------------Strings------------------------------------------------



# lista_buscar_reemplazar = {
#     ("Hola", "Hello"),
#     ("Uno", "One"),
#     ("Si", "Yes")
# }
# # texto = "Hola el numero a ser reemplazado es el Uno Si y solo Si es....."
# texto = "Hola Mundo"
# print("----Ejemplos----")
# print(texto.split())
# print(texto.split("reemplazado"))
# print(texto.split("....."))
# print("----------------")



# for buscar, remplazar in lista_buscar_reemplazar:
#   texto= texto.replace(buscar, remplazar)

# print(texto)

# lista=["Hola", "Mundo", "Pepe", "Uno"]

# # texto = "es"
# texto = " "


# print(" ".join(lista))  #El join usa la lista y el " " separa los datos con espacion y los junta en un dato. 

# print(texto.join(lista)) #Tambien puede usarse una variable en vez de  " ". 

# print("-------".join(lista)) # usa la lista ylos separa con --------


# hola= "Hola mundo"

# hola = hola.split()

# dict= hola[0]

# helo = dict[0]

# print(helo)


import re 
texto ="QUEVEDO || BZRP Music Sessions #52"
fecha = "2022-07-06 00:00:00"
print(re.split("[\|]{2}|[#]{1}", texto))#elimina las barras mas simple

# print(re.split("[0-9]{4}\-[0-9]{2}\-[0-9]{2}", fecha)) te muestra todo los numeros e ignora las barras / split (elimina)

print(re.split("[\- :]{1}", fecha))

# print(re.split(r'\- | |:', fecha))

# print(re.split("[\\\]+", fecha)) #Lo mismo
print(re.split(r"[\\]+", fecha)) #Lo mismo



print(re.findall(r"[a-zA-Z ]{1,}" , texto)) #findall agrega r(expresion regular)



print(re.findall(r"[a-zA-Z ]{2,}[|]{2}([a-zA-Z ]{2,})#([0-9]+)" , texto)) #findall agrega r(expresion regular) "+" tambien puede ser {1,} 
print(re.findall(r"[a-zA-Z ]{2,}[|]{2} BZRP Music Sessions #[0-9]+" , texto)) #Tambien podes agregar el texto 

# ( lo que me interes nomas)    (este tambien me interesa)
#

print("Lo que paso el profe")
texto = "QUEVEDO || BZRP Music Sessions #52 JUAN || BZRP Music Sessions #2 Q  || BZRP Music Sessions #22"
fecha = "2022-07-06 00\\00:00"
print(re.split(r'[\\]+', fecha))     

print(re.findall(r"([a-zA-Z ]{2,})[|;]{2} BZRP Music Sessions #([0-9]+)",texto))