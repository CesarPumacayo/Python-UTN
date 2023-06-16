# #César Pumacayo 1°E grupo Giovanni

# #Ejercicio 1
# # Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.

# def convertir_mayusculas(texto):
#     '''
#     Convertir string a mayuscula
#     Recibe string
#     Retorna upper()
#     '''
#     return texto.upper()

# # texto = "Hola mundo"
# # texto_en_mayusculas = convertir_mayusculas(texto)
# # print(texto_en_mayusculas)



# #Ejercicio 2
# #Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.

# def convertir_minuscula(texto):
#     '''
#     Convertir texto a minuscula
#     Recibe texto
#     Retorna texto.lower()
#     '''
#     return texto.lower()

# # texto = "Hola MUNDO"
# # texto_en_minuscula = convertir_minuscula(texto)
# # print(texto_en_minuscula)





# #Ejercicio 3
# #Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.

# def concatenar_strings(texto1, texto2):
#     '''
#     Concatenar strings y separarlos con un espacio
#     Recibe 2 strings
#     Retorna la concatenacion y separacion 
#     '''

#     return texto1 + " " +texto2

# # primer_texto = "Hola"
# # segundo_texto = "Jose"

# # separados_espacio= concatenar_strings(primer_texto,segundo_texto)
# # print(separados_espacio)





# #Ejercicio 4
# #Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.

# def mostrar_string(texto):
#     '''
#     Muestra la longitud de los caracteres
#     Recibe un string
#     Retorna un len(texto)
#     '''      
#     return len(texto)

# texto= "Hola Javascript"
# mensaje = mostrar_string(texto)
# print(mensaje)



# #Ejecicio 5
# #Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.

# def mostrar_count(string, caracter):
#     return string.count(caracter)

# letra= "i"
# palabra= "Bienvenido"

# resultado = mostrar_count(palabra, letra)
# print(resultado)





# #Ejercicio 6
# #Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.

# def devolver_lista_caracter(string, caracter):
#     palabras = string.split()
#     palabras_con_caracter= []
#     for i in palabras:
#         if caracter in i:
#             palabras_con_caracter.append(i)
#     return palabras_con_caracter


# texto = "Hola mundo caja Python"
# caracter= "o"
# resultado = devolver_lista_caracter(texto, caracter)
# print(resultado)



#Ejercicio 7
#Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados

# def mostrar_espacio_eliminados(string):
#     return string.replace(" ", "")

# texto= "Hola como se llama?"

# resultado = mostrar_espacio_eliminados(texto)
# print(resultado)

#Ejercicio 8
# #Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula


# def capitalize_nombre_apellido(nombre, apellido):
#     nombre= nombre.strip()
#     apellido= apellido.strip()

#     nombre= nombre.capitalize()
#     apellido= apellido.capitalize()

#     diccionario= {nombre,apellido}

#     return diccionario

# # resultado= capitalize_nombre_apellido(nombre=" césar ", apellido=" pumacayo ")

# # print(resultado)

# #Ejercicio 9
# #Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".

# def lista_nombres(lista):
#     for nombre in range(len(lista)):
#         salto= lista[nombre].replace("," , "\n")
#         print(salto) 


# # lista = ["Juan", "María", "Pedro"]  
# # lista_nombres(lista)



# #Ejercicio 10
# #Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".

# def nombre_apellido_email(nombre, apellido):
#     email= "inicial_nombre.apellido@utn-fra.com.ar"
#     email = email.replace("nombre", nombre)
#     email = email.replace("apellido", apellido)
#     print(email)
    


# # nombre_apellido_email("César", "Pumacayo")



# #Ejercicio 11
# #Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..

# def mostrar_lista(lista:list)->str:
#     '''
#     DOCUMENTAR
#     Concatena en un solo string con coma y "y"
#     Recibe lista
#     Retorna reemplazo
#     '''
    
#     reemplazo = ", ".join(lista[:-1]) + " y " + lista[-1]

#     return reemplazo
# # lista= ["manzanas", "naranjas", "bananas"]

# # resultado = mostrar_lista(lista)
# # print(resultado)





# #Ejercicio 12
# #Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 

# def mostrar_numero_tarjeta_credito():
#     numero_tarjeta= input("Ingrese el numero de tarjeta")
#     if numero_tarjeta.isalnum():
#         digitos= "*" * (len(numero_tarjeta)-4) + numero_tarjeta[-4:]
        
#         return digitos
    
# # resultado  = mostrar_numero_tarjeta_credito()
# # print(resultado)

# #Ejercicio 13
# #Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".

# def eliminar_email(correo_electronico:str):
#     correo_electronico= correo_electronico.replace("@gmail.com", "")
#     return correo_electronico

# # correo="usuario@gmail.com"

# # resultado = eliminar_email(correo)
# # print(resultado)
    

# #Ejercicio 14
# #Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

# def obtener_nombre_dominio(url):
#     # Eliminar el prefijo "https://" o "http://"
#     if url.startswith("https://"):
#         url_sin_prefijo = url[8:]
    
    
#     # Obtener el nombre de dominio (parte antes de la primera barra diagonal)
#     indice_barra = url_sin_prefijo.find("/")
#     # indice_barra = url_sin_prefijo.find(".com")

#     if indice_barra != -1:
#         dominio = url_sin_prefijo[:indice_barra]
#     else:
#         dominio = url_sin_prefijo
    
#     # Eliminar el subdominio (parte antes del primer punto)
#     indice_punto = dominio.find(".")
#     if indice_punto != -1:
#         nombre_dominio = dominio[indice_punto+1:]
#     else:
#         nombre_dominio = dominio
    
#     return nombre_dominio

# # url=input("Ingrese el url: ")
# # resultado = obtener_nombre_dominio(url)
# # print(resultado)




# #Ejercicio 15
# #Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”


# def solo_caracteres_alfabeticos(texto):
#     palabras = texto.split()
#     solo_letras = []
#     for palabra in palabras:
#         solo_letras.append(''.join(c for c in palabra if c.isalpha()))
#     return ' '.join(solo_letras)

# # texto= "H0l4, m4nd0!"
# # resultado = solo_caracteres_alfabeticos(texto)
# # print(resultado)
    


# #Ejercicio 16
# #Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

# def mostrar_acronimo(texto):
#     texto = texto.split()
#     acronimo= []
#     for palabra in texto:
#         acronimo.append(palabra[0])
#     return "".join(acronimo)
    

# # texto= input("Ingrese una cadena de texto")
# # resultado= mostrar_acronimo(texto)
# # resultado = resultado.upper()
# # print(resultado)


# #Ejercicio 17
# #Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".


# def mostrar_binario_8_bits(numero):
#     return numero.zfill(8)


# # numero = input("Ingrese un numero: ")
# # resultado = mostrar_binario_8_bits(numero)
# # print(resultado)



# #Ejercicio 18
# #Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"


# def caracter_primer_minuscula_todO_mayuscula(texto):
#     return texto.swapcase()

# texto= input("Ingrese una palabra: ")
# resultado = caracter_primer_minuscula_todO_mayuscula(texto)
# print(resultado)


# #Ejercicio 19
# #Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.


# def mostrar_cantidad_digitos(texto):
#     contador = 0

#     texto = texto.replace(" ", "")

#     for palabra in texto:
#         if palabra >= '0' and palabra <= '9':
#             contador += 1
#     return contador

# texto= input("Ingrese una palabra: ")
# resultado= mostrar_cantidad_digitos(texto)
# print(resultado)









# #Ejercicio 20
# #Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: 
# # ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".



# def mostrar_correo(lista_correo):
#     separador = ";"
#     separador = separador.join(lista_correo)
#     return separador


# # lista_correo = ["juan@gmail.com", "maria@hotmail.com"]
# lista_correo= []
# lista_correo.append(input("Ingrese email: "))
# lista_correo.append(input("Ingrese email2: "))


# resultado =mostrar_correo(lista_correo)
# print(resultado)






#Ejercicio 21
#Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.


# def limpia_texto(texto:str):
#     texto = texto.replace(",", "")
#     texto = texto.replace(":", "")
#     texto = texto.replace(";", "")
#     texto = texto.replace(".", "")
#     return texto

# print(limpia_texto("diccionario donde cada, clave es una palabra; y cada: valor es. un entero que"))

# def contar_palabras(string):
#     '''
#     Contar palabras repetidas en el string
#     Recibir string
#     Retorna resultado
#     '''
#     # Crear un diccionario vacío
#     resultado = {}
    
#     # Convertir el string en una lista de palabras
#     palabras = string.split()
    
    
#     # Recorrer la lista de palabras y actualizar el diccionario
#     for palabra in palabras:
#         if palabra in resultado:
#             resultado[palabra] += 1
#         else:
#             resultado[palabra] = 1
    
#     # Devolver el diccionario con los resultados
#     return resultado

# texto = input("Ingrese un texto: ")
# resultado=contar_palabras(texto)
# print(resultado)




#----------------------------------------------------
#Ejercicio 12

# def  validar_tarjeta(texto):
#     lista= texto.split(" ")
#     flag_tarjeta_ok = True
#     var_texto = "ERROR"

#     for e in lista:
#         if(e.isdigit() == False):
#             flag_tarjeta_ok=False
#             break
#     if(flag_tarjeta_ok and len(lista) == 4):
#         var_texto = "**** {0} {1} *****".format(lista[1],lista[2])

#     return var_texto

# print(validar_tarjeta("1111 8888 9999 0000"))
# print(validar_tarjeta("1A21 8888 9999 0000"))


#------------------------------------------------

#Ej 11

# def concatenar(palabras:list)->str:

#     texto= ""
#     if(len(palabras)>1):
#         for palabra in palabras[0:-1]:
#             texto = "{0}{1}, ".format(texto,palabra)
        
#         texto = texto[0:-2]
#         texto = "{0} y {1}".format(texto,palabras[-1])
#     elif(len(palabras) == 1):
#         texto = palabras[0]
#     else:
#         texto = "-------"
#     return texto
# print(concatenar(["manzanas","manzanas","manzanas","naranjas","bananas"]))
# print(concatenar(["manzanas","bananas"]))
# print(concatenar([]))








































































