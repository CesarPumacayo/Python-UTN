#Funciones.
#César Pumacayo 1°E grupo giovanni

#Ejercicio 1:
#Crear una función que convierta grados Celsius a grados Fahrenheit. Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

def celsius_a_fahrenheit(grados_celsius):
    '''
    Convertir y mostrar celsius a fahrenheit
    Recibe grados celsius
    Retorna grados fahrenheit

    '''
    grados_fahrenheit = (9/ 5 * grados_celsius) + 32
    return grados_fahrenheit
print(celsius_a_fahrenheit(224)) # devuelve 435.2
#César Pumacayo 1°E grupo giovanni

#Ejercicio 2
# Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.

def area_circulo(radio):
    '''
    Calcular el area del circulo
    Recibe parametros (radio)
    Retorna area del circulo
    
    '''
    pi = 3.14 
    area = pi * radio**2
    return area

print(area_circulo(5)) # 78.54
#César Pumacayo 1°E grupo giovanni

#Ejercicio 3
# Crear una función que calcule el descuento aplicado a un producto. 
# Recibe dos parámetros (precio original y precio con descuento) y 
# devuelve el porcentaje de descuento aplicado.


def porcentaje_descuento(precio_original, precio_descuento):
    '''
    Calcula el porcentaje del descuento aplicado
    Recibe precio descuento y el precio original
    Retorna el porcentaje
    '''
    descuento = precio_original - precio_descuento
    porcentaje = (descuento / precio_original) * 100
    return porcentaje


print(porcentaje_descuento(2500, 50)) # 98.0
#César Pumacayo 1°E grupo giovanni

#Ejercicio 4
# Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.

def promedio_grupo(lista_edades):
    '''
    Calcular el promedio de un grupo de personas
    Recibe lista edades
    Retorna promedio
    '''

    promedio = sum(lista_edades) / len(lista_edades)

    return promedio 
print(promedio_grupo([1, 45, 23, 12]))
#César Pumacayo 1°E grupo giovanni

#Ejercicio 5
# Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.

def es_primo(numero):
    '''
    Mostrar si es primo o no
    Recibe numero
    Retorna True o False

    '''
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


print(es_primo(2))
#César Pumacayo 1°E grupo giovanni

#Ejercicio 6
#Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.

def calcular_area_triangulo(base,altura):
    '''
    Calcular el area
    Recibe altura y base
    Retorna area
    '''

    area = (base * altura) / 2

    return area
print(calcular_area_triangulo(6,6))
#César Pumacayo 1°E grupo giovanni

#Ejercicio 7
# Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.
def calcular_maximo_divisor(numero_uno, numero_dos):
    '''
    Calcula el maximo comun divisior de dos numeros
    Recibe dos numeros
    Retorna el maximo comun divisor
    '''
    
    while numero_dos != 0:
        maximo_comun= numero_uno % numero_dos
        numero_uno = numero_dos
        numero_dos = maximo_comun
    return numero_uno
        
print(calcular_maximo_divisor(8,6))
#César Pumacayo 1°E grupo giovanni

#Ejercicio 8
# Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.

def mostrar_par_impar(numero):
    '''
    Mostrar si es impar o no
    Recibe un numero
    Retorna True si es par o False si es impar
    '''
    if numero % 2 == 0:
        return True
    else:
        return False
print(mostrar_par_impar(1))
#César Pumacayo 1°E grupo giovanni

#Ejercicio 9
#Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
# Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.

def mostrar_cantidad_elemento_lista(lista, elemento):
    contador=0
    for i in range(len(lista)):
        if lista[i] == elemento:
            contador+=1


    return contador
print(mostrar_cantidad_elemento_lista([2,4,4,6,8,1],4))
#César Pumacayo 1°E grupo giovanni

#Ejercicio 10
#Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.

def palabra_mas_larga(lista_palabras):
    mas_largo = lista_palabras[0]
    for palabra in lista_palabras:
        if len(palabra) > len(mas_largo):
            mas_largo = palabra
    return mas_largo

print(palabra_mas_larga(["vicuña", "animaciones", "Javascript" , "Python", "Heimerdinger"]))  
    
#César Pumacayo 1°E grupo giovanni

#Ejercicio 11
#Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.

def contar_vocales(cadena_texto):
    vocales = "aeiou"
    cantidad_vocales = 0
    for letra in cadena_texto:
        if letra.lower() in vocales:
            cantidad_vocales += 1
    return cantidad_vocales
print(contar_vocales("Heimerdinger"))


#César Pumacayo 1°E grupo giovanni


#Ejercicio 12
#Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas

def mostrar_elementos_iguales(lista_nombres1, lista_nombres2):
    lista_iguales=[]
     
    for nombre in lista_nombres1:
        if nombre in lista_nombres2:
            lista_iguales.append(nombre)
    return lista_iguales


print(mostrar_elementos_iguales(["telefono", "roberto", "caja", "ropero","desierto"], ["caramelo", "caja", "carpeta", "roberto","vino","telefono"]))

#César Pumacayo 1°E grupo giovanni

#Ejercicio 13
#Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.

def crear_diccionario_longitudes(lista_palabras):
    diccionario = {}
    for palabra in lista_palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

print(crear_diccionario_longitudes(["mochila", "Javascript", "Notebook", "Python"]))


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

#Ejercicio 15
#Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y 
# devuelve un diccionario con la cantidad de películas por género.

def contar_peliculas_por_genero(lista_peliculas):
    peliculas_por_genero = {}
    for pelicula in lista_peliculas:
        genero = pelicula["genero"]
        if genero in peliculas_por_genero:
            peliculas_por_genero[genero] += 1
        else:
            peliculas_por_genero[genero] = 1
    return peliculas_por_genero

peliculas = [{"titulo": "El Padrino", "genero": "Drama", "director": "Francis Ford Coppola"},    {"titulo": "El Señor de los Anillos", "genero": "Fantasía", "director": "Peter Jackson"},    {"titulo": "Jurassic Park", "genero": "Ciencia ficción", "director": "Steven Spielberg"},    {"titulo": "La La Land", "genero": "Comedia musical", "director": "Damien Chazelle"},    {"titulo": "Titanic", "genero": "Drama", "director": "James Cameron"},    {"titulo": "Star Wars", "genero": "Ciencia ficción", "director": "George Lucas"},]

peliculas_por_genero = contar_peliculas_por_genero(peliculas)


print(peliculas_por_genero)



