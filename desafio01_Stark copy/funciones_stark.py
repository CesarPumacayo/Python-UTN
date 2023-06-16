#César Pumacayo 1°E grupo Giovanni
import re
import json

# print(ordenar_por_altura(lista_heroes))

'''
Desafio #1: stark (sin menu)
'''

def print_genero(heroes, genero):
    if genero == "F":
        tipo = "femenino"
    else:
        tipo = "masculino"
    print("\n--------------------------------------\n")
    print("Los superheroes de genero {0} son:\n".format(tipo))
    for heroes in lista_heroes:
        if heroes["genero"]==genero:
            print("\nNombre: {0}".format(heroes["nombre"]))

def calcular_mas_menos_por_clave_genero(lista_heroes, genero, maximo=True):
    valor_min_max = None
    if maximo == True:
        tipo = "maxima"
    else:
        tipo= "minima"
    for personaje in lista_heroes:

        if personaje["genero"] == genero:

            valor_actual = float(personaje["altura"])
            
            if valor_min_max is None:
                valor_min_max = (valor_actual, personaje)
            elif maximo and valor_actual > valor_min_max[0]:
                valor_min_max = (valor_actual, personaje)
            elif not maximo and valor_actual < valor_min_max[0]:
                valor_min_max = (valor_actual, personaje)

    if valor_min_max is None:
        return f"No se encontraron personajes del género {genero} en la lista."
    else:
        resultado = f"La {tipo} altura del superhéroe de género {genero} es {valor_min_max[1]['nombre']} y su altura es {valor_min_max[1]['altura']} cm."
        return resultado

def mostrar_altura_promedio_por_genero(genero):
    acumulador=0
    contador=0
    for indice in lista_heroes:
        if indice["genero"]== genero:
            acumulador_femenido= float(indice["altura"])
            acumulador+= acumulador_femenido
            contador+=1

    promedio = acumulador / contador
    if genero == "M":
        genero = "masculino"
    else:
        genero = "femenino"

    resultado = "El promedio de la altura del genero {0} es: {1}".format(genero , promedio)
    return resultado

def contar_tipo_superheroes(lista_heroes , tipo_clave):
    diccionario_tipo= {}
    for tipo in lista_heroes:
        contar = tipo[tipo_clave] 
        if contar in diccionario_tipo:
            
            diccionario_tipo[contar] += 1
        else:
            diccionario_tipo[contar] = 1
    if tipo_clave == "inteligencia":
        if diccionario_tipo[""]:
            diccionario_tipo[""] = "no tiene"


    return diccionario_tipo

def agrupar_tipo_superheroes(lista_heroes , tipo_clave):
    diccionario_tipo= {}
    for tipo in lista_heroes:
        agrupar= tipo[tipo_clave]
        dato_heroe= tipo["nombre"]

        if agrupar in diccionario_tipo:
            auxiliar_lista = diccionario_tipo[agrupar]
            auxiliar_lista.append(dato_heroe)
        else:
            auxiliar_lista= []
            auxiliar_lista.append(dato_heroe)
            diccionario_tipo[agrupar] = auxiliar_lista

    return diccionario_tipo

def print_tipos_contador(tipo,clave):
    print("--------------------------------------------\n")
    print("Los  cantidad de superheroes con el tipo de {0} de los superheroes son:".format(clave))
    print(tipo)
    
def print_tipos_agrupados(tipo):
    for heroes in tipo:
        print("---------------")
        print(heroes)
        print(len(tipo[heroes]))
        print(tipo[heroes])

'''
Desafio #2 : Stark (inicia aqui)
'''
def stark_normalizar_datos(lista_heroes:list):
    '''
    Recibe una lista de héroes y normaliza los datos numéricos
    '''
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return

    # Lista de keys numéricas
    keys_numericas = ["altura", "peso", "fuerza"]
    datos_modificados = False

    for heroe in lista_heroes:
        for key in keys_numericas:
            # Verificar que la key exista y que su valor no sea numérico
            if key in heroe and not isinstance(heroe[key], (int, float)):
                # Validar que el valor de la key sea numérico antes de convertir
                if heroe[key].isdigit():
                    heroe[key] = int(heroe[key])
                    datos_modificados = True
                elif heroe[key].replace(".", "", 1).isdigit():
                    heroe[key] = float(heroe[key])
                    datos_modificados = True

    if datos_modificados:
        print("Datos normalizados")

def obtener_nombre(diccionario_nombre:dict)->str:
    nombre= diccionario_nombre["nombre"]
    texto = "nombre: " + nombre 
    return texto

def imprimir_dato(texto:str):
    print(texto)

def stark_imprimir_nombres_heroes(lista_heroes:list):
    if not lista_heroes:
        return -1
    
    for heroe in lista_heroes:
        nombre = obtener_nombre(heroe)
        print(nombre)

def obtener_nombre_y_dato(diccionario:dict,key:str)->str:
    nombre = diccionario["nombre"]
    valor_key = diccionario[key]
    nombre = "Nombre: "+ nombre + " | " + key+": " + str(valor_key)
 
    return nombre

def stark_imprimir_nombres_alturas(lista_heroes:list)->None:
    if not lista_heroes:
        return -1
    for i in lista_heroes:
        nombre_altura = obtener_nombre_y_dato(i, "altura")
        imprimir_dato(nombre_altura)
        
def calcular_max(lista_heroes:list, key:str)->str:
    '''
    Calcular maximo de la lista segun el key
    Recibe lista_heroes y key(str)
    Retorna el heroe del dato mas alto
    '''
    valor= lista_heroes[0]

    for i in lista_heroes:
        if float(i[key]) > float(valor[key]):
            valor = i
            texto={'nombre': valor["nombre"], key : valor[key]}
   
    return texto

def calcular_min(lista_heroes:list, key:str)->str:
    '''
    Calcular minimo de la lista segun el key
    Recibe lista_heroes y key(str)
    Retorna el heroe del dato menos alto
    '''
    valor = lista_heroes[-1]

    for i in lista_heroes:
        if float(i[key]) < float(valor[key]):
            valor= i
            texto = {'nombre': valor["nombre"], key : valor[key]}
    return texto

def calcular_max_min_dato(lista_heroes:list, string:str, string_clave:str)->dict:
    '''
    Calcular maximo y minimo en una sola funcion
    Recibe lista_heroes , string (maximo o minimo) y string_clave("altura", "edad", "peso")
    No retorna
    '''
    if string=="maximo":
        dato_maximo= calcular_max(lista_heroes, string_clave)
        return dato_maximo 
    elif string=="minimo":
        dato_minimo=calcular_min(lista_heroes,string_clave)
        return dato_minimo

def stark_calcular_imprimir_heroe(lista_heroes:list, max_min:str, string_clave:str)->None:
    '''
    Calcula el maximo y minimo segun la key que le ingreses ("altura" , "peso" , "fuerza")
    Recibe lista_heroes , max_min (toma valor maximo o minino) y un string que representa la key
    No Retorna
    '''
    if not lista_heroes:
        return -1
    else:
        max_min_dato = calcular_max_min_dato(lista_heroes, max_min, string_clave)

        resultado = obtener_nombre_y_dato(max_min_dato, string_clave)

        if max_min== "maximo":
            palabra_max_min = "Mayor"
        elif max_min == "minimo":
            palabra_max_min= "Menor"
        texto = ("{0} {1} : {2}".format(palabra_max_min, string_clave, resultado))
        imprimir_dato(texto)
    
def sumar_dato_heroe(lista_heroes: list, dato_key: str)->int:
    '''
    Suma todos datos segun la key del dato
    Recibe lista_heroes y dato_key
    Retorna un int
    '''
    suma = 0
    
    for heroe in lista_heroes:
        if type(heroe) == dict and bool(heroe):
            suma += float(heroe.get(dato_key, 0))
    
    return suma

def dividir(dividendo:float, divisor:float)->float:
    '''
    Realiza la division de 2 numeros
    Recibe dividendo y divisor
    Retorna un float 
    '''
    if divisor == 0:
        return 0
    resultado = float(dividendo / divisor)
    return resultado

def calcular_promedio(lista_heroes:list, string:str)->float:
    '''
    Calcula el promedio segun la key(string) que quieras promediar
    Recibe lista_heroes y string
    Retorna float
    '''
    stark_normalizar_datos(lista_heroes)
    datos= sumar_dato_heroe(lista_heroes, string)
    cantidad= len(lista_heroes)
    promedio = dividir(datos, cantidad)

    return promedio

def stark_calcular_imprimir_promedio_altura(lista_heroes:list)->float:
    '''
    Calcula el promedio de altura
    Recibe lista_heroes
    Retorna el float (promedio_altura)
    '''
    if not lista_heroes:
        return -1
    else:
        promedio_altura= calcular_promedio(lista_heroes, "altura")
    return promedio_altura

def imprimir_menu()->None:
    '''
    Imprime el menu del desafio stark 2
    No recibe nada
    No retorna
    '''
    imprimir_dato(  "1 - Mostrar la lista de superheroes por nombre\n"
                    "2 - Mostrar la lista de superheroes por nombre y altura\n"
                    "3 - Mostrar el maximo o minimo segun key de dato que pases a la funcion ('peso','altura','fuerza')\n"
                    "4 - Imprimir la altura promedio\n"
                    "5 - Salir\n"
                 )

def validar_entero(texto_de_numero:str)->bool:
    '''
    Verifica que sea sea un string conformado únicamente por dígitos    
    Recibe texto_de_numero
    Retorna bool(True o False)
    '''
    if texto_de_numero.isdigit():
        return True
    else:
        return False

def stark_menu_principal()->int:
    '''
    Muestra el menu de opciones y valida el numero que ingreso el usuario
    No recibe nada
    Retorna un int
    '''
    imprimir_menu()
    entrada = input("Ingrese el número de la opción deseada: ")
   
    if validar_entero(entrada):
        opcion = int(entrada)
        if opcion in range(1,6):
            return opcion
    else:
        return -1

def stark_marvel_app(lista_heroes:list)->None:
    '''
    Muestra ejecución principal de nuestro programa. 
    Recibe lista_heroes
    No retorna
    '''
    while True:
        respuesta = stark_menu_principal()    
        if respuesta == 1:
            stark_imprimir_nombres_heroes(lista_heroes)
        elif respuesta == 2:
            stark_imprimir_nombres_alturas(lista_heroes)
        elif respuesta == 3:
            imprimir_dato(calcular_max_min_dato(lista_heroes, string="minimo", string_clave="fuerza"))
        elif respuesta == 4:
            imprimir_dato(stark_calcular_imprimir_promedio_altura(lista_heroes))
        elif respuesta == 5:
            break
        else:
            print("Opción inválida, intente de nuevo")
        input("\nPulse enter para continuar\n")


'''
Desafio #5 (modificacion del desafio #1): Stark (inicia aqui)
'''
def validar_character(texto:str)->bool:
    '''
    Verifica que sea un caracter conformado por letras
    Recibe texto
    Retorna bool(True o False)
    '''
    if texto.isalpha():
        return True
    else:
        return False

def imprimir_menu_desafio_5()->None:
    '''
    Imprime el desafio 5 de la parte 1 stark
    No recibe nada
    No retorna
    '''
    imprimir_dato(
                    "A - Mostrar el nombre de todo los superheroes de genero M\n"
                    "B - Mostrar el nombre de todo los superheroes de genero F\n" 
                    "C - Mostrar el superheroe con mas altura de genero Masculino\n"
                    "D - Mostrar el superheroe con mas altura de genero Femenino\n"
                    "E - Mostrar el superheroe con menos altura de genero Masculino\n"
                    "F - Mostrar el superheroe con menos altura de genero Femenino\n"
                    "G - Mostrar el promedio de la altura del genero Masculino\n"
                    "H - Mostrar el promedio de la altura del genero Femenino\n"
                    "I - Mostrar cuántos superheroes tienen cada tipo de color de ojos\n"
                    "J - Mostrar cuántos superhéroes tienen cada tipo de color de pelo\n"
                    "K - Mostrar cuántos superhéroes tienen cada tipo de inteligencia\n"
                    "L - Mostrar todos los superhéroes agrupados por color de ojos\n"
                    "M - Mostrar todos los superhéroes agrupados por color de pelo\n"
                    "N - Mostrar todos los superhéroes agrupados por tipo de inteligencia\n"
                    "O- Salir\n"
    )

def stark_menu_principal_desafio_5()->str:
    '''
    Muestra el menu de opciones y valida el caracter que ingreso el usuario con un rango
    No recibe nada
    Retorna un int
    '''
    imprimir_menu_desafio_5()
    entrada = input("Ingrese una letra de la opción deseada: ")
    if validar_character(entrada):
        opcion = entrada
        if re.search("[A-O]", opcion):
            return opcion
        else:
            return -1

def stark_marvel_app_5(lista_heroes:list)->None:
    '''
    Muestra ejecución principal de nuestro programa 
    Recibe lista_heroes
    No retorna
    '''
    while True:
        respuesta = stark_menu_principal_desafio_5()
        if respuesta == "A":
            imprimir_dato(stark_guardar_heroe_genero(lista_heroes, genero="M"))
        elif respuesta == "B":
            imprimir_dato(stark_guardar_heroe_genero(lista_heroes, genero="F"))
        elif respuesta == "C":
            imprimir_dato(stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, max_min="maximo", string_clave="altura", genero="M"))
        elif respuesta == "D":
            imprimir_dato(stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, max_min="maximo", string_clave="altura", genero="F"))
        elif respuesta == "E":
            imprimir_dato(stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, max_min="minimo", string_clave="altura", genero="M"))
        elif respuesta == "F": 
            imprimir_dato(stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, max_min="minimo", string_clave="altura", genero="F"))
        elif respuesta == "G":
            imprimir_dato(stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, string="altura",genero="M"))
        elif respuesta == "H":
            imprimir_dato(stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, string="altura",genero="F"))
        elif respuesta == "I":
            imprimir_dato(stark_calcular_cantidad_por_tipo(lista_heroes, tipo_dato="color_ojos"))
        elif respuesta == "J":
            imprimir_dato(stark_calcular_cantidad_por_tipo(lista_heroes, tipo_dato="color_pelo"))
        elif respuesta == "K":
            imprimir_dato(stark_calcular_cantidad_por_tipo(lista_heroes, tipo_dato="inteligencia"))
        elif respuesta == "L":
            imprimir_dato(stark_listar_heroes_por_dato(lista_heroes , tipo_dato="color_ojos"))
        elif respuesta == "M":
            imprimir_dato(stark_listar_heroes_por_dato(lista_heroes , tipo_dato="color_pelo"))
        elif respuesta == "N":
            imprimir_dato(stark_listar_heroes_por_dato(lista_heroes , tipo_dato="inteligencia"))
        elif respuesta == "O":
            break
        else:
            print("Opción inválida, ingrese una letra con mayuscula")
        input("\nPulse enter para continuar\n")

def leer_archivo(ruta:str)->list:
    with open(ruta , "r") as archivo:
        diccionario_heroes= json.load(archivo)
    return diccionario_heroes["heroes"]



def guardar_archivo(nombre_archivo: str, contenido: str)->bool:
    try:
        with open(nombre_archivo, 'w+') as archivo:
            archivo.write(contenido)
        print(f'Se creó el archivo: {nombre_archivo}')
        return True
    except:
        print(f'Error al crear el archivo: {nombre_archivo}')
        return False
    
def capitalizar_palabras(texto:str):
    texto = texto.split()
    palabras = []
    for palabra in texto:
        palabra_capitalizada = palabra.capitalize()
        palabras.append(palabra_capitalizada)
    texto_capitalizado = " ".join(palabras)
    return texto_capitalizado

def obtener_nombre_capitalizado(diccionario_heroe:dict)->str:

    nombre_heroe = diccionario_heroe["nombre"]
    resultado = capitalizar_palabras(nombre_heroe)
    
    texto = f"Nombre: {resultado}"
    return texto

def obtener_nombre_y_dato(diccionario_heroe:dict, tipo_key:str)->str:
    nombre= obtener_nombre_capitalizado(diccionario_heroe)

    valor_key = diccionario_heroe[tipo_key]
    tipo_key = tipo_key.capitalize()
    nombre =  nombre + " | " + tipo_key +": " + valor_key
 
    return nombre

'''
------------------ Segunda Parte --------------------
'''
def es_genero(diccionario_heroe:dict, texto_evaluar:str)->bool:
    if diccionario_heroe["genero"] == texto_evaluar:
        return True
    else:
        return False

def stark_guardar_heroe_genero(lista_heroes:list, genero:str)->bool:
    if not lista_heroes:
     return False
    else:
        lista_genero = []
        separador_archivo = ","
        nombre_archivo = f"desafio01_Stark copy\\heroes_{genero}.csv"
        for heroe in lista_heroes:
            if es_genero(heroe, genero):
                lista_genero.append(obtener_nombre_capitalizado(heroe))
        archivo = separador_archivo.join(lista_genero)
        archivo = archivo.replace(",", "\n")
        guardar_archivo(nombre_archivo, archivo)
        return True

'''
------------------- Tercera Parte ----------------------- 
'''
def calcular_min_genero(lista_heroes:list, key: str, genero:str)->dict: 
    '''
    Calcular minimo de la lista segun el key y genero
    Recibe lista_heroes y key(str) , genero (M , F o NB)
    Retorna el heroe con el dato minimo
    '''
    valor = lista_heroes[-1]

    for i in lista_heroes:
        if es_genero(i ,genero):
            if float(i[key]) < float(valor[key]):
                valor= i
                texto = {'nombre': valor["nombre"], key : valor[key]}
    return texto

def calcular_max_genero(lista_heroes: list , key: str, genero:str)->dict:
    '''
    Calcular el maximo de la lista segun el key y genero (M, F O NB)
    Recibe lista_heroes y key(str) , genero (M , F o NB)
    Retorna diccionario con el dato maximo
    '''

    valor = lista_heroes[0]

    for i in lista_heroes:
        if es_genero(i ,genero):
            if float(i[key]) > float(valor[key]):
                valor= i
                texto = {'nombre': valor["nombre"], key : valor[key]}
    return texto

def calcular_max_min_dato_genero(lista_heroes:list, string:str, string_clave:str , genero:str)->dict:
    '''
    Calcular maximo y minimo en una sola funcion segun su genero
    Recibe lista_heroes , string (maximo o minimo) , string_clave("altura", "edad", "peso") y genero (M, F, NB)
    No retorna
    '''
    if string=="maximo":
        dato_maximo= calcular_max_genero(lista_heroes, string_clave, genero)
        return dato_maximo 
    elif string=="minimo":
        dato_minimo=calcular_min_genero(lista_heroes,string_clave, genero)
        return dato_minimo
    
def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes:list, max_min:str, string_clave:str, genero:str)->bool:
    '''
    Calcula el maximo y minimo segun la key que le ingreses ("altura" , "peso" , "fuerza")
    Recibe lista_heroes , max_min (toma valor maximo o minino) y un string que representa la key
    No Retorna
    '''
    lista_genero = []
    if not lista_heroes:
        return False
    else:
        max_min_dato = calcular_max_min_dato_genero(lista_heroes, max_min, string_clave, genero)

        resultado = obtener_nombre_y_dato(max_min_dato, string_clave)

        if max_min== "maximo":
            palabra_max_min = "Mayor"
        elif max_min == "minimo":
            palabra_max_min= "Menor"

        tipos= string_clave.capitalize()
            
        texto = ("{0} {1} : {2}".format(palabra_max_min, tipos, resultado))
        resultado = imprimir_dato(texto)

        lista_genero.append(max_min_dato)


        nombre_archivo = f"desafio01_Stark copy\\heroes_{max_min}_{string_clave}_{genero}.csv"


    
        nombres_heroes = []
        for heroe in lista_genero:
            nombres_heroes.append(obtener_nombre_capitalizado(heroe))

        nombres_heroes = ("{0}".format(texto))

        resultado = guardar_archivo(nombre_archivo, nombres_heroes)
        return True
    
'''
------------------------- Cuarta Parte------------------------------
'''

def sumar_dato_heroe_genero(lista_heroes: list, dato_key: str, genero: str) -> int:
    '''
    Suma todos los datos segun el genero
    Recibe lista , str dato , key y genero
    Retorna int
    '''
    suma = 0
    
    for heroe in lista_heroes:
        if es_genero(heroe, genero):
            if type(heroe) == dict and bool(heroe):
                suma += float(heroe.get(dato_key, 0))
    if suma == 0:
        return -1
    else:
        return suma

def cantidad_heroes_genero(lista_heroes:list, genero:str)->str:
    '''
    Cuenta la cantidad de superheroes de cada genero
    Recibe lista_heroes y genero
    Retorna texto
    '''
    contador_genero = 0
    for heroe in lista_heroes:
        genero_heroe = heroe["genero"]
        if genero_heroe == genero:
            contador_genero += 1

    return contador_genero

def calcular_promedio_genero(lista_heroes:list, string:str , genero:str):

    acumulador= sumar_dato_heroe_genero(lista_heroes , string , genero)

    contador = cantidad_heroes_genero(lista_heroes, genero)

    resultado = dividir(acumulador, contador)

    return resultado

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list, string:str ,genero:str)->bool:
    '''
    Calcula el promedio segun la key(string) que quieras promediar
    Recibe lista_heroes , string (fuerza, altura , etc) y genero ( M o F , NB)
    Retorna float
    '''
    
    if not lista_heroes: 
        print("Error: Lista de héroes vacía.")
        booleano = False
    else:
        promedio_altura= calcular_promedio_genero(lista_heroes, string , genero)
        string = string.capitalize()
        texto = "{0} promedio genero {1}: {2}".format(string , genero ,promedio_altura)
        print(texto)

        nombre_archivo = f"desafio01_Stark copy\\heroes_promedio_altura_{genero}.csv"
        guardar_archivo(nombre_archivo, texto)
        booleano = True
    return booleano

'''
---------------- Quinta Parte -----------------------
'''
def calcular_cantidad_tipo(lista_heroes:list , clave:str)->dict:
    '''
    Calcular la cantidad de tipo
    Recibe lista_heroes y clave 
    Retorna diccionario
    '''
    diccionario_tipo= {}

    if not lista_heroes:
        return {"Error": "La lista se encuentra vacía"}
    else:
        for tipo_dato in lista_heroes:
            tipos = tipo_dato[clave]
            tipos_capitalizados = capitalizar_palabras(tipos)
            if tipos_capitalizados in diccionario_tipo:
                diccionario_tipo[tipos_capitalizados] += 1
            else:
                diccionario_tipo[tipos_capitalizados] = 1

        return diccionario_tipo

def guardar_cantidad_heroes_tipo(diccionario_tipos:dict, tipo_dato: str)-> bool:
    """
    Itera cada key del diccionario y variabiliza dicha key con su valor para luego formatearlos en un mensaje el cual deberá guardar en archivo.
    Recibe un diccionario con las distintas variedades del tipo de dato como clave y sus respectivas cantidades como valor, y el tipo de dato a usar en el mensaje final formateado.
    Reutiliza la función 'guardar_archivo' para guardar el mensaje en un archivo con el nombre correcto.
    Retorna True si salió todo bien, False caso contrario.
    """

    if not diccionario_tipos:
        return False
    else:
        lista_dato = []
        separador_archivo = "\n"
        nombre_archivo = f"desafio01_Stark copy\\heroes_cantidad_{tipo_dato}.csv"
        for clave, valor in diccionario_tipos.items():
            mensaje_final = "Caracteristicas: {0} {1} - Cantidad de heroes: {2}".format(tipo_dato , clave , valor)
            lista_dato.append(mensaje_final)
            imprimir_dato(mensaje_final)
        
        archivo_txt= separador_archivo.join(lista_dato)
        guardar_archivo(nombre_archivo, archivo_txt)
        return True

def stark_calcular_cantidad_por_tipo(lista_heroes:list , tipo_dato:str)->bool:
    '''
    Muestra la cantidad de tipos , lista_heroes y segun el tipo de dato 
    Recibe lista_heroes y tipo_dato
    Retorna Bool
    '''
    if not lista_heroes:
        return False
    else:
        lista = calcular_cantidad_tipo(lista_heroes, tipo_dato)
        guardar_cantidad_heroes_tipo(lista, tipo_dato)
        return True
    
'''
Desafio #6: Stark (inicia aqui)
'''

def obtener_lista_de_tipos(lista_heroes: list, tipo_dato: str) -> set:
    """
    Retorna un set con las variedades del tipo de dato pasado por parámetro (sus valores) 
    encontradas en la lista de héroes. Si no se encuentra un valor para el tipo de dato, se 
    asigna 'N/A' antes de agregarlo a la lista.
    """
    valores = set()
    for heroe in lista_heroes:
        valor = heroe.get(tipo_dato)
        if valor is None or valor == '':
            valor = 'N/A'
        else:
            valor = capitalizar_palabras(valor)
        valores.add(valor)
    return valores

# print(obtener_lista_de_tipos(lista_heroes , tipo_dato="inteligencia"))

def normalizar_dato(dato_valor:str , dato_por_defecto:str="N/A"):
    '''
    Si el valor de una key ('color_ojos' : 'verde') es igual a "" el otro parametro reemplaza su valor
    Recibe dato_valor y dato_por_defecto
    Retorna dato_valor 
    '''
    if dato_valor == "":
        dato_valor = dato_por_defecto
    return dato_valor

def normalizar_heroe(diccionario_heroe:dict , dato_key:str)->dict:
    '''
    Capitalizar y normalizar el key y Nombre  Ej: dict:{("heroe")}  y key: (key) = xxx
    Recibe diccionario_heroe y dato_key
    Retorna un dicccionario de los heroes normalizados 
    '''
    diccionario_heroe[dato_key]= capitalizar_palabras(diccionario_heroe[dato_key])
    diccionario_heroe[dato_key]= normalizar_dato(diccionario_heroe[dato_key])
    diccionario_heroe["nombre"]= capitalizar_palabras(diccionario_heroe["nombre"])

    return diccionario_heroe

def obtener_heroes_por_tipo(lista_heroes: list, set_tipos: set, tipo_dato: str) -> dict:
    """
    Obtener los tipos con los heroes agrupados
    Recibe Lista_heroes , set y un tipo de dato
    Retorna un diccionario con cada variedad como clave y una lista de nombres de héroes como valor.
    """
    diccionario_tipo = {}
    for tipo in set_tipos:
        diccionario_tipo[tipo] = []
        for heroe in lista_heroes:
            valor = heroe.get(tipo_dato)
            if valor is None or valor == '':
                valor = 'N/A'
            else:
                valor = capitalizar_palabras(valor)
            if tipo == valor:
                nombre = capitalizar_palabras(heroe["nombre"])
                diccionario_tipo[tipo].append(nombre)
    return diccionario_tipo

def guardar_heroes_por_tipo(diccionario_tipo:dict , tipo_dato:str)->bool:
    '''
    Guarda todos los heroes en sus tipos de datos
    Recibe diccionario y tipo de dato
    Retorna bool
    '''
    if not diccionario_tipo:
        return False
    else:
        lista_dato = []
        separador_archivo = "\n"
        nombre_archivo= "desafio01_Stark copy\\heroes_segun_{0}.csv".format(tipo_dato)
        for clave, valor in diccionario_tipo.items():
            mensaje = " | ".join(valor)
            mensaje_final = "{0} {1}: {2}".format(tipo_dato , clave , mensaje)
            lista_dato.append(mensaje_final)
            imprimir_dato(mensaje_final)

        archivo_txt= separador_archivo.join(lista_dato)
        guardar_archivo(nombre_archivo, archivo_txt)
        return True

def stark_listar_heroes_por_dato(lista_heroe:list , tipo_dato:str)->bool:




    '''
    Muestra los distintos tipos de datos y junto con los nombres de los heroes
    Recibe lista y str
    Retorna booleano
    '''

    if not lista_heroe:
        return False
    else:
        lista_set = obtener_lista_de_tipos(lista_heroe, tipo_dato)
        lista_heroe = obtener_heroes_por_tipo(lista_heroe, lista_set ,tipo_dato)
        guardar_heroes_por_tipo(lista_heroe, tipo_dato)
        return True


'''
------------------------ Parte desafio #6 --------------------------------------
'''
def ordenar_por_altura(lista_heroes):
    """
    Ordena la lista de héroes por altura de menor a mayor y devuelve una lista con las alturas ordenadas.
    Recibe una lista de diccionarios con la información de cada héroe.
    Devuelve una lista de alturas.
    """
    rango = len(lista_heroes)
    for indice in range(rango - 1):
        for heroes in range(rango - indice - 1):
            if lista_heroes[heroes]["altura"] > lista_heroes[heroes+1]["altura"]:
                lista_heroes[heroes], lista_heroes[heroes+1] = lista_heroes[heroes+1], lista_heroes[heroes]
    
    return [heroe["altura"] for heroe in lista_heroes]


def ordenar_por_peso(lista_heroes):
    """
    Ordena la lista de héroes por altura de mayor a menor y devuelve una lista con las alturas ordenadas.
    Recibe una lista de diccionarios con la información de cada héroe.
    Devuelve una lista de alturas.
    """
    rango = len(lista_heroes)
    for indice in range(rango - 1):
        for heroes in range(rango - indice - 1):
            if lista_heroes[heroes]["peso"] < lista_heroes[heroes+1]["peso"]:
                lista_heroes[heroes], lista_heroes[heroes+1] = lista_heroes[heroes+1], lista_heroes[heroes]
    
    return [heroe["peso"] for heroe in lista_heroes]

# print(ordenar_por_peso(lista_heroes))


def ordenar_por_nombre(lista_heroes):
    rango = len(lista_heroes)
    for indice in range(rango - 1):
        for heroes in range(rango - indice - 1):
            if lista_heroes[heroes]["nombre"] > lista_heroes[heroes+1]["nombre"]:
                lista_heroes[heroes], lista_heroes[heroes+1] = lista_heroes[heroes+1], lista_heroes[heroes]
    
    return [heroe["nombre"] for heroe in lista_heroes]

# print(ordenar_por_nombre(lista_heroes))

def ordenar_por_largo_nombre(lista_heroes):
    rango = len(lista_heroes)
    for indice in range(rango - 1):
        for heroes in range(rango - indice - 1):
            if len(lista_heroes[heroes]["nombre"]) < len(lista_heroes[heroes+1]["nombre"]):
                lista_heroes[heroes], lista_heroes[heroes+1] = lista_heroes[heroes+1], lista_heroes[heroes]
    
    return [heroe["nombre"] for heroe in lista_heroes]

# print(ordenar_por_largo_nombre(lista_heroes))

def ordenar_por_key(lista_heroes:list, tipo_dato:str, booleano:bool):


    rango = len(lista_heroes)
    for indice in range(rango - 1):
        for heroes in range(rango - indice - 1):
            if  booleano == False and lista_heroes[heroes][tipo_dato] < lista_heroes[heroes+1][tipo_dato] or booleano == True and lista_heroes[heroes][tipo_dato] > lista_heroes[heroes+1][tipo_dato]:
                lista_heroes[heroes],lista_heroes[heroes+1] = lista_heroes[heroes+1],lista_heroes[heroes]
    
    return [heroe[tipo_dato] for heroe in lista_heroes]

# print(ordenar_por_key(lista_heroes, "altura", booleano=True))
def menu():
    opcion = 0
    while opcion != 6:
        print("Menú de ordenamiento:\n"
                "1. Ordenar por altura\n"
                "2. Ordenar por peso\n"
                "3. Ordenar por nombre\n"
                "4. Ordenar por largo de nombre\n"
                "5. Ordenar por bool max o min y tipo clave\n"
                "6. Salir\n"
        )
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            # Llamar a la función de ordenamiento por altura
            imprimir_dato(ordenar_por_altura(lista_heroes))
            
        elif opcion == 2:
            # Llamar a la función de ordenamiento por peso
            imprimir_dato(ordenar_por_peso(lista_heroes))
            
        elif opcion == 3:
            # Llamar a la función de ordenamiento por nombre
            imprimir_dato(ordenar_por_nombre(lista_heroes))
            
        elif opcion == 4:
            # Llamar a la función de ordenamiento por largo de nombre
            imprimir_dato(ordenar_por_largo_nombre(lista_heroes))
        elif opcion ==5:
            imprimir_dato(ordenar_por_key(lista_heroes, "fuerza", booleano=True))
            
        elif opcion == 6:
            print("Saliendo...")
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

rutaJSON = "desafio01_Stark copy\\data_stark.json"
lista_heroes = leer_archivo(rutaJSON)
stark_normalizar_datos(lista_heroes)


