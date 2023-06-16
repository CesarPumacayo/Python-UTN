#César Pumacayo Grupo Giovanni 1°E
import re

#Ejercicio 1
# Crear una función llamada es_mayuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario

# def es_mayuscula(texto):
#     if re.match(r'^[A-Z]*$', texto):
#         return True
#     else:
#         return False

# print(es_mayuscula("HOLsA"))


# def es_mayuscula(texto:str) -> bool:
#     """
#     \nQué hace:
#     - Busca si el texto ingresado está escrito completamente en mayúsculas.
#     \nParámetros:
#     - texto (str): el texto a analizar.
#     \nDevuelve:
#     - bool: True si está completamente en mayúsculas, False si no lo está.
#     """
#     if re.search('[a-zá-úñ]',texto) == None:
#         variable_es_mayuscula = True
#     else:
#         variable_es_mayuscula = False
    
#     return variable_es_mayuscula

# print(es_mayuscula('HOLA!! É Ñ'))






#Ejercicio 2
#Crear una función llamada es_minuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario

# def es_minuscula(texto):
#     if re.match(r'^[a-z]*$', texto):
#         return True
#     else:
#         return False
    
# print(es_minuscula("hola"))






#Ejercicio 3
#Crear una función llamada es_entero que reciba un string y devuelva True en caso de que se trate de un número entero y False en caso contrario.

# def es_entero(texto):
#     if re.match("^[0-9]*$",texto):
#         return True
#     else:
#         return False
    
# print(es_entero("434"))




#Ejercicio 4
#Crear una función llamada es_solo_texto que reciba un string y devuelva True en caso de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario

# def es_solo_texto(texto):
#     if re.match("^[a-zA-Z ]*$", texto):
#         return True
#     else:
#         return False

    
# print(es_solo_texto("Hola mundo"))





#Ejercicio 5
#Crear una función llamada es_decimal que reciba dos strings: el primero representa la expresión a evaluar y el segundo el separador decimal (puede ser punto . o coma ,). Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.


# def es_decimal(texto_evaluar, texto_separador):
#     patron = r'^-?\d+(?:[{separador}]\d{{1,2}})?$'.format(separador=texto_separador)
#     if re.match(patron, texto_evaluar):
#         return True
#     else:
#         return False
    


# print(es_decimal("23.22", ",."))






#Ejercicio 6
# Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de solo letras y números y False en el caso contrario (es decir que contenga caracteres especiales) 

# def alfa_numerico(texto):
#     if re.match(r"^[a-zA-Z0-9 ]*$",texto):
#         return True
#     else:
#         return False


# print(alfa_numerico("123abc"))








#Ejercicio 7
#Crear una función llamada es_binario que devuelva True en caso de un número binario válido (solo ceros y unos) o False en el caso contrario


# def es_binario(texto):
#     if re.match("^[0-1 ]*$",texto):
#         return True
#     else:
#         return False
    
# print(es_binario("1110010001"))








#Ejercicio 8
#Crear una función que reciba una lista de palabras y devuelva otra lista con las palabras  que comienzan con la letra ‘U’

# def palabras_con_U(lista_palabras):
#     lista_resultado = []
#     for palabra in lista_palabras:
#         if re.match("^[Uu]", palabra):
#             lista_resultado.append(palabra)
#     return lista_resultado

# palabras = ["hola", "Uva", "Uno", "uhu", "ultra"]
# resultado = palabras_con_U(palabras)
# print(resultado)





#Ejercicio 9
# Crear una función que reciba un texto y devuelva una lista con las palabras que contienen entre 3 y 6 caracteres de largo

# def recibir_caracteres_rango(texto:str):
#     lista = texto.split()
#     lista_vacio = []
#     for palabra in lista:
#         if re.match(r"^[a-zA-Z ]{3,6}$",palabra):
#             lista_vacio.append(palabra)
#     return lista_vacio

# palabras = "Hola es un string que lleva primera letra con mayuscula"
# resultado = recibir_caracteres_rango(palabras)
# print(resultado)



#Ejercicio 10
#Crear una función que reciba un texto y devuelva una lista de todas las palabras que terminan con ‘ción’. Ejemplo de texto: https://onlinegdb.com/swyremkF6

# def devolver_lista_ción(texto):
#     lista= texto.split()
#     lista_vacio = []
#     for palabra in lista:
#         if re.match(r"^[a-zA-Z]+?ción", palabra):
#             lista_vacio.append(palabra)
#     return lista_vacio



# texto = "La tecnología de la información ha revolucionado la comunicación en todas sus formas. La digitalización y la automatización de procesos han permitido la optimización de los recursos y la mejora en la eficiencia de los sistemas. La cibernética, la robótica y la inteligencia artificial son algunas de las áreas de la informática que se han desarrollado en las últimas décadas y han transformado la forma en que vivimos y trabajamos. La interconexión de dispositivos y la transmisión de datos en tiempo real han permitido la creación de nuevas industrias y modelos de negocio que antes eran impensables. La educación, la salud, el transporte y la logística son algunos de los sectores que han sido beneficiados por la innovación tecnológica. En conclusión, la tecnología ha generado una revolución en nuestra sociedad que ha llevado a la transformación y evolución de la misma."
# resultado = devolver_lista_ción(texto)
# print(resultado)





#Ejercicio 11
#Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que comienzan con una vocal

# def devolver_lista_vocales(texto):
#     texto= texto.split()
#     lista_vacio = []
#     for palabra in texto:
#         if re.match("^[aeiouAEIOU]",palabra):
#             lista_vacio.append(palabra)
#     return lista_vacio 



# texto = "La tecnología de la información ha revolucionado la comunicación en todas sus formas"
# resultado = devolver_lista_vocales(texto)
# print(resultado)






#Ejercicio 12
#Crear una función llamada obtener_oraciones que reciba como parámetro un string y que devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’). 
# Ejemplo de texto: https://onlinegdb.com/UMdr3hI3G


# def obtener_oraciones(texto):
#     lista_vacio = []
#     oraciones = re.findall(r"[A-Z][^\.!?]*[\.!?]", texto)
#     for oracion in oraciones:
#         # Eliminar espacios antes y después de los signos de puntuación
#         oracion = oracion.strip()
#         lista_vacio.append(oracion)
#     return lista_vacio




# texto = "¿Bello es mejor que feo? Explícito es mejor que implícito. Simple es mejor que complejo. Complejo es mejor que complicado. Plano es mejor que anidado. Espaciado es mejor que denso. La legibilidad es importante. Los casos especiales no son lo suficientemente especiales como para romper las reglas. Sin embargo la practicidad le gana a la pureza. Los errores nunca deberían pasar silenciosamente. A menos que se silencien explícitamente. Frente a la ambigüedad, evitar la tentación de adivinar. Debería haber una, y preferiblemente solo una, manera obvia de hacerlo. A pesar de que eso no sea obvio al principio a menos que seas Holandés. Ahora es mejor que nunca. A pesar de que nunca es muchas veces mejor que *ahora* mismo. Si la implementación es difícil de explicar, es una mala idea. Si la implementación es fácil de explicar, puede que sea una buena idea. Los espacios de nombres son una gran idea, ¡tengamos más de esos!"
# resultado =obtener_oraciones(texto)
# print(resultado)


#Ejercicio 13
#Crear una función que reciba un texto como parámetro y que corrija los errores de ortografía que no cumplan con la regla ortográfica que indica que antes de V se escribe N y que antes de B se escribe M.
 
# Por ejemplo,
#  si el texto es: "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente envarcar en esta nueva aventura." 

# La función debería devolver:
# “Mi convicción me hace sentir que es el momento de invertir tiempo para finalmente embarcar en esta nueva aventura."



# def corregir_ortografia(texto): dudas

#     texto_corregido = re.sub(r"nv", r"mb", texto)
#     texto_corregido = re.sub(r"mv", r"nv", texto_corregido)
    

    
    

#     return texto_corregido


# texto=  "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente envarcar en esta nueva aventura envase." 
# resultado= corregir_ortografia(texto)
# print(resultado)







#Ejercicio 14 (complicado)
#Crear la función es_fecha que reciba dos string, el primero representa la expresión a evaluar y el segundo el separador de la fecha (puede ser la barra / o el guión -) y que devuelva True en caso de tratarse de una fecha válida y False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o ‘dd-mm-aaaa’

# def es_fecha(texto_evaluar, texto_separador):
#     patron_fecha = r"\d{2}" + re.escape(texto_separador) + r"\d{2}" + re.escape(texto_separador) + r"\d{4}"
#     if re.match(patron_fecha, texto_evaluar):
#         return True
#     else:
#         return False

# texto = "04/05/2023"
# separador = "/"
# resultado = es_fecha(texto, separador)
# print(resultado)  # True

            
#Ejercicio 15
# Crear la función es_hora que reciba un string y que devuelva True en caso de tratarse de una hora válida y False en el caso contrario. El formato admitido es ‘hh:mm:ss’

# def es_hora(texto):
#     if re.match("^[0-9]{2}:[0-9]{2}:[0-9]{2}",texto):
#         return True
#     else:
#         return False

# texto = "12:54:15"
# resultado = es_hora(texto)
# print(resultado)



#Ejercicio 16
#Crear la función validar_codigo_postal que reciba un string como parámetro y devuelva True en caso de tratarse de código postal válido o False en caso contrario. 

# def validar_codigo_postal(texto):
#     if re.match("^[A-Z][0-9]{4}[A-Z]{3}$",texto):
#         return True
#     else:
#         return False
    



# texto = "A1342FDA"
# resultado =validar_codigo_postal(texto)
# print(resultado)



#Ejercicio 17
#Crear la función validar_patente que reciba un string como parámetro y devuelva True en caso de tratarse de un número de patente válido o False en caso contrario.  Debe poder admitir estos dos tipos:


# def validar_patente(texto):
#     if re.match(r"^[A-Z]{2}\ [0-9]{3}\ [A-Z]{2}$",texto):
#         return True
#     elif re.match(r"^[A-Z]{3}\ [0-9]{3}$",texto):
#         return True
#     else:
#         return False
    


# texto = "AB 123 CD"
# texto2= "ABC 123"

# resultado = validar_patente(texto)
# print(resultado)



#Ejercicio 18
#Crear una función que se llame obtener_direcciones_email que reciba un texto y devuelva una lista con todas las direcciones de email válidas que encuentren en el mismo. Acá dejamos un texto de ejemplo: https://onlinegdb.com/Ln0jhatKeI


# def obtener_direcciones_email(texto):
#     lista_vacio = []
#     texto = texto.split()
#     for palabra in texto:
#         if re.search("@", palabra):
#             lista_vacio.append(palabra)
#     return lista_vacio


# datos = " <Alberto, Cervantes> acervantes@gmx.com <Ana, Jimenez> ajimenez@hotmail.com <Antonio, Castillo> acastillo@gmail.com <Armando, Vega> avega@yahoo.com <Arturo, Arredondo> aarredondo@gmail.com <Beatriz, Vargas> bvargas@outlook.com <Berenice, Rios> bribos@yahoo.com <Brenda, Gonzalez> bgonzalez@terra.com <Brian, Hernandez> bhernandez@outlook.com <Camila, Reyes> creyes@terra.com <Carlos, Gallegos> cgallegos@gmail.com <Carolina, Alvarado> calvarado@outlook.com <Cesar, Rosales> crosales@terra.com <Christian, Moreno> cmoreno@gmail.com <Clara, Serrano> cserrano@yahoo.com <Cristian, Huerta> chuerta@terra.com <Cristina, Ochoa> cochoa@yahoo.com <Dalia, Rivas> drivas@outlook.com <Daniel, Perez> dperez@yahoo.com <Daniela, Ruiz> druiz@outlook.com <David, Velasco> dvelasco@gmail.com <Diana, Andrade> dandrade@yahoo.com <Diego, Ortiz> dortiz@terra.com <Eduardo, Vazquez> evazquez@gmail.com <Elisa, Castillo> ecastillo@outlook.com <Elizabeth, Cruz> ecruz@yahoo.com <Emmanuel, Pacheco> epacheco@terra.com <Enrique, Fuentes> efuentes@gmail.com <Erika, Cabrera> ecabrera@yahoo.com <Erick, Zavala> ezavala@outlook.com <Esmeralda, Valdes> evaldes@gmx.com <Esteban, Montes> emontes@gmail.com <Evelyn, Vera> evera@yahoo.com <Fabian, Rangel> frangel@terra.com <Fatima, De La Cruz> fdela@gmx.com <Felipe, Salas> fsalas@outlook.com <Fernanda, Guerrero> fguerrero@gmail.com <Fernando, Olvera> folvera@yahoo.com <Francisco, Hernandez> fhernandez@terra.com <Gabriela, Acosta> gacosta@gmail.com <Gael, Maldonado> gmaldonado@outlook.com <Gerardo, Flores> gflores@yahoo.com <Giselle, Alvarado> galvarado@terra.com <Gloria, Tapia> gtapia@gmx.com <Gonzalo, Zamora> gzamora@yahoo.com <Graciela, Ochoa> gochoa@outlook.com <Guadalupe, Aguilar> gaguilar@gmail.com <Guillermo, Garza> ggarza@yahoo.com <Gustavo, Mora> gmora@terra.com <Heidi, Hernandez> hhernandez@gmx.com <Hector, Barrios> hbarrios@outlook.com <Hugo, Villarreal> hvillarreal@yahoo.com <Ignacio, Soto> isoto@gmail.com <Ingrid, Vidal> ividal@yahoo.com <Irma, Garza> igarza@terra.com <Isaac, Palacios> ipalacios@gmail.com <Ivan, Rojas> irojas@yahoo.com <Jacqueline, Fuentes> jfuentes@outlook.com <Jaime, Huerta> jhuerta@yahoo"

# resultado = obtener_direcciones_email(datos)
# print(resultado)





#Ejercicio 19 (mhhh)
#Crear una función llamada validar_password que reciba un string y verifique si se trata de una contraseña cumple con los requisitos mínimos de seguridad:
# Al menos 8 caracteres
# Al menos una letra mayúscula y una letra minúscula
# Un número 
# Un carácter especial
	
# En caso de no cumplir con alguno de los requisitos, imprimir un mensaje informando cual no se cumplio


# def validar_password(password):
#     print(len(password))
#     if len(password) > 8:
#         return "La contraseña debe tener al menos 8 caracteres."
#     if not re.search(r"[a-z]", password):
#         return "La contraseña debe contener al menos una letra minúscula."
#     if not re.search(r"[A-Z]", password):
#         return "La contraseña debe contener al menos una letra mayúscula."
#     if not re.search(r"[0-9]{1}", password):
#         return "La contraseña debe contener exactamente un número."
#     if not re.search(r"[\d]{1}", password):
#         return "La contraseña debe contener al menos un carácter especial."

    
#     return "La contraseña cumple con los requisitos mínimos de seguridad."


# password = "Contra1$"
# resultado = validar_password(password)
# print(resultado)



#Ejercicio 20
#Crear una función llamada validar_ip que reciba un string como parámetro y verifique si se trata de una dirección IP v4 válida, en caso de serlo retornar True de lo contrario retornar False. 
#Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde xxx es un número entero entre 0 y 255.

def validar_ip(texto):
    if re.match("^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", texto):
        return True
    else:
        return False

texto = "234.123.255.188"
resultado = validar_ip(texto)
print(resultado)






























