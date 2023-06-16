#Ejercicio 1

# Crea una lista con los números del 1 al 10 e imprime solo los números impares.

# lista = [1,2,3,4,5,6,7,8,9,10]

# for i in lista:
#     if i %2 != 0:
#         print(i, end=" ")


#Ejercicio 2

# Crea una lista con 5 números enteros. Luego solicita un nuevo número y reemplaza el tercer elemento de la lista por el número ingresado. Finalmente imprime todos los números

# lista= [4,2,6,8,10]

# print(lista)

# nuevo= int(input("Ingrese el valor para la clave:"))

# lista.pop(3)
# lista.insert(3,nuevo)

# print(lista)

#Ejercicio 3

# Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo. Luego, muestra la suma de todos los números ingresados.

# lista= []
# acumulador=0
# while True:
#     numero = int(input("Ingrese numeros enteros: "))
#     if numero > 0:
#         acumulador+=numero
        
#     if numero < 0:
#         break
#     lista.append(numero)

# print(lista)
# print("La suma de todos los numero son: {0}".format(acumulador))

#Ejercicio 4

# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, muestra la primera letra de la palabra. Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

# lista= []
# substring= ""

# while True:
#     letra= input("Ingrese palabra: ")

#     lista.append(letra)

#     for letra in lista:
#         print(letra[0])
#     substring = letra[0]== "z"

#     if substring: # tambien if letra[0] == "z":
#         break

  





#Ejercicio 5

# Crea una lista con los nombres de 5 ciudades y luego imprime el último elemento de la lista.

# lista =[]
# contador = 0
# while contador < 5:
#     nombres= input("Ingrese el nombre de la ciudad: ")
#     lista.append(nombres)
#     contador+=1


# print(lista[4])

#Ejercicio 6

# Crea una lista con 3 números enteros y luego agrega un nuevo número al final de la lista.

# lista= []
# contador= 0
# while contador < 3:
#     numero = int(input("Ingrese el numero: "))
#     lista.append(numero)
#     contador+=1
# nuevo= int(input("Ingrese un nuevo numero: "))
# lista.append(nuevo)
# print(lista)

#Ejercicio 7

# Crea una lista con los nombres de tus 3 deportes favoritos y luego agrega otro deporte al final de la lista.

# lista = []
# contador=0

# while contador < 3:
#     nombre= input("Ingrese el nombre del deporte favorito: ")
#     lista.append(nombre)
#     contador+=1

# nuevo= input("Agrege un nuevo deporte favorito: ")
# lista.append(nuevo)
# print(lista)


#Ejercicio 8

# Crea una lista con los nombres de tus 5 libros favoritos y luego imprime solo los primeros 3 libros de la lista.

# lista= []
# contador = 0

# while contador < 5:
#     libro= input("Ingrese tu libro favorito: ")
#     lista.append(libro)
#     contador+=1

# print(lista[0:3])


#Ejercicio 9

# Crea una lista de números enteros y pide al usuario que ingrese otro número entero. Luego, 
# busca el número ingresado en la lista y muestra la posición en la que se encuentra.
# Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró

# lista = [2,5,3,7,8,9]
# print(lista)


# numero = int(input("Ingrese un número entero: "))
# lista.append(numero)

# print("Lista:", lista)

# busqueda = int(input("Ingrese el número que desea buscar: "))

# if busqueda in lista:
#     posicion = lista.index(busqueda)
#     print("El número", busqueda, "se encuentra en la posición", posicion)
# else:
#     print("El número", busqueda, "no se encuentra en la lista")






#Ejercicio 10
# Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

# lista = []
# lista_largo = []

# while True:
#     palabra = input("Ingrese una palabra a la lista: ")
#     lista.append(palabra)

#     respuesta = input("Desea continuar? si o no ")

#     if respuesta == "no":
#         break

# for palabra in lista:
#     if len(palabra) > 5:
#         print(palabra)
#         lista_largo.append(palabra)

# print("Lista original: ", lista)
# if lista_largo:
#     print("Lista de palabras largas: ", lista_largo)
# else:
#     print("No hay palabras largas en la lista.")





#Ejercicio 11
# Crea una lista de palabras y pide al usuario que ingrese una palabra. 
# Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.


# lista = ["oso","gato","python","bienvenido","Javascript"]
# lista_largo= []
# print(lista)

# nuevo= input("Ingrese una nueva palabra a la lista: ")


# print(lista)

# for palabra in lista:
#     if len(palabra) == len(nuevo):
#         print(palabra)
#         lista_largo.append(palabra)

# if lista_largo: 
#     print("Lista de palabras largas mayores a la palabra que ingresaste: ", lista_largo)
# else:
#     print("No hubo palabra mayores a lo que ingresaste: ")



    


#Ejercicio 12
#Crea una lista con los nombres de tus 3 películas favoritas y luego imprime los elementos en orden inverso (sin utilizar el método reverse())

# lista_peliculas= ["Megamente", "Iron man", "Neutron"]

# print("Lista original: ",lista_peliculas)

# lista_peliculas.reverse()
# print("Lista en 'reverse':",lista_peliculas)


#Ejercicio 13
#Crea una lista de números y encuentra el promedio de todos los números en la lista.

# lista= [1,9,8,3,6]

# acumulador= sum(lista)

# contador = len(lista)

# promedio= acumulador / contador

# print("El promedio es: {0}".format(promedio))


#Ejercicio 14
#Crea dos listas de 10 números enteros cada una y realiza una multiplicación de los elementos con el mismo índice en ambas listas.

# lista_uno=[2,8,3,5,7,1,9,7,57,7]
# lista_dos=[8,15,7,12,9,12,3,6,9,10]
# resultado=[]

# for i in range(len(lista_uno)):
#     producto = lista_uno[i] * lista_dos[i]
#     resultado.append(producto)


# print(resultado)



#Ejercicio 15
#Crea una lista de números enteros y luego encuentra la suma de los números en índices impares.


# lista_uno = [2, 8, 3, 5, 7, 1, 9, 7, 57]
# suma_impares = 0

# for i in range(len(lista_uno)):
    
#     if i % 2 != 0:
#         suma_impares += lista_uno[i]

# print("La suma de los números en índices impares es:", suma_impares)



#Ejercicio 16
#Crea dos listas con la misma cantidad de elementos y luego crea una tercera lista que contenga los elementos de ambas listas intercalados. 
# Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"], la tercera lista debería ser [1, "a", 2, "b", 3, "c"].

# lista_uno=[1,2,3]
# lista_dos=["a","b","c"]
# lista_mezclada=[]


# for i in range(len(lista_uno)):
#     mezcla = lista_uno[i] 
#     lista_mezclada.append(mezcla)
#     mezcla = lista_dos[i]
#     lista_mezclada.append(mezcla)

# print(lista_mezclada)
    




#Ejercicio 17
# Crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.

# lista_uno=[3,1,32,12,9]
# lista_dos=[23,9,1,8,3]

# result = []

# for num in lista_uno:  # el num se vuelve lista_uno
#     if num in lista_dos:
#         result.append(num)

# print(result)





#Ejercicio 18
#Solicitar al usuario números enteros hasta que ingrese el 0. Almacenar los números en una lista y luego imprimir el mayor (sin utilizar la función max())

# lista = []

# while True:
#     num = input("Ingrese un numero a la lista // ingresa '0' para terminar: ")
#     if num == "0":
#         break
#     lista.append(int(num))

# mayor = lista[0]

# for numero in lista:
#     if numero > mayor:
#         mayor = numero

# print("El mayor numero de la lista es:", mayor)






#Ejercicio 19
#Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, agrega la palabra a la lista si no se encuentra ya en la lista. 
#Repite este proceso hasta que la lista tenga al menos 5 palabras.


# lista = []

# while len(lista) < 5:
#     palabra = input("Ingrese una palabra a la lista: ")
#     if palabra not in lista:
#         lista.append(palabra)
#     else:
#         print("La palabra ya está en la lista.")
# print("La lista de palabras ingresadas es:", lista)




#Ejercicio 20
#A partir de la lista: [1,80,5,0,15,-5,1,79] determinar, el mayor, el menor, el promedio y la suma total de todos los elementos


# lista= [1,80,5,0,15,-5,1,79]
# mayor = lista[0]
# menor= lista[0]
# acumulador= 0


# for i in lista:
#     acumulador+= i
#     if i > mayor:
#         mayor = i
#     elif i < menor:
#         menor= i

# promedio = acumulador / len(lista)

# print(mayor)
# print(menor)
# print(acumulador)
# print(promedio)





#Ejercicio 21
#Crear un programa que solicite al usuario ingresar precio unitario y cantidad de 5 productos. 
# Almacenar cada valor en dos listas distintas. Luego imprimir el precio total de cada artículo.

# lista_precio_unitario= []
# lista_producto=[]
# lista_cantidad= []


# while len(lista_producto) < 5:
#     precio = float(input("Ingrese el precio unitario: "))
#     cantidad = int(input("Ingrese la cantidad: "))
#     producto = input("Ingrese el producto: ")

#     lista_precio_unitario.append(precio)
#     lista_cantidad.append(cantidad)
#     lista_producto.append(producto)

# lista_precio_total= []

# for i in range(len(lista_producto)):
#     multiplicar=(lista_cantidad[i] * lista_precio_unitario[i])
#     lista_precio_total.append(multiplicar)

# print(lista_precio_total)








#Ejercicio 22
#Crear un programa que solicite al usuario ingresar: nombre del producto, cantidad y precio unitario. Guardar los datos en 3 listas distintas. 
#Solicitar productos hasta que el nombre del producto sea ‘xxx’. Luego imprimir la lista de artículos con el siguiente formato:


#nombre_articulo	cantidad	$ precio_unitario 	$ total
#	Ejemplo:
#	alfajor capitan del espacio		6	$ 150		$ 900




lista_precio_unitario= []
lista_producto=[]
lista_cantidad= []

while True:
    producto= input("Ingrese un producto // finalizas el programa al escribir: 'xxx': ")
    if producto == "xxx":
        break
    
    cantidad= int(input("Ingrese la cantidad de producto: "))
    precio_unitario = int(input("Ingrese el precio unitario: "))

    lista_precio_unitario.append(precio_unitario)
    lista_cantidad.append(cantidad)
    lista_producto.append(producto)

lista_total= []

print("Nombre_articulo\tcantidad\t$ precio_unitario\t$ total")
for i in range(len(lista_producto)):
    total = lista_cantidad[i] * lista_precio_unitario[i]
    print("{0}\t\t{1}\t\t${2}\t\t\t${3}".format(lista_producto[i], lista_cantidad[i], lista_precio_unitario[i], total))





        # case 22:
        #     stark_normalizar_datos(lista_personajes)
            
        # case 23: 
        #     print(obtener_nombre(lista_personajes[23]))
        # case 24:
        #     imprimir_dato(lista_personajes[0]["color_ojos"])

        # case 25:
        #     stark_imprimir_nombres_heroes(lista_personajes)
        # case 26:
        #     print(obtener_nombre_y_dato(lista_personajes[2],"fuerza"))
        # case 27:
        #     stark_imprimir_nombres_alturas(lista_personajes)
        # case 28:
        #     print(calcular_max(lista_personajes, "fuerza"))
        # case 29:
        #     print(calcular_min(lista_personajes, "peso"))
        # case 30:
        #     print(calcular_max_min_dato(lista_personajes, string="minimo", string_clave="fuerza"))
        # case 31:
        #     stark_calcular_imprimir_heroe(lista_personajes,"minimo","altura")
        # case 32:
        #     stark_calcular_imprimir_promedio_altura(lista_personajes)
        # case 33:
        #     stark_marvel_app(lista_personajes)
        # case _:
        #     break
