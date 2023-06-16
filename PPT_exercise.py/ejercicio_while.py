#César Pumacayo 1°E Grupo Giovanni
# Ejercicios de While


# Ejercicio 1
# Dado un número entero n, imprimir todos los números desde n hasta 1 en orden descendente.


# n = int(input("Ingrese un numero entero para descenderlo: "))
# while n >= 1:
#     print(n)
#     n-=1


#Ejercicio 2
#Dado un número entero n, imprimir todos los números desde 1 hasta n en orden ascendente.
# n = int(input("Ingrese un número entero: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1




#Ejercicio 3
#Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.

# cadena = input("Ingrese la cadena: ")
# contador = 0
# while contador < len(cadena):
#     print(cadena[contador])
#     contador+=1




#Ejercicio 4
#Dada una lista de números, imprimir la suma de todos los elementos de la lista.

# lista=[1,2,5,7,10]
# contador=0
# acumulador=0
# while contador < len(lista):
#     acumulador+= lista[contador]
#     print(acumulador)
#     contador+=1
# print("La suma en total de la lista es: {0}".format(acumulador))




#Ejercicio 5
#Dado un número entero n, imprimir si el número es primo o no.

# numero = int(input("Ingrese un número entero: "))

# if numero < 2:
#     print("El número no es primo")
# else:
#     es_primo = True
#     i = 2
#     while i <= numero ** 0.5:
#         if numero % i == 0:
#             es_primo = False
#             break
#         i += 1

#     if es_primo:
#         print("El número es primo")
#     else:
#         print("El número no es primo")



#Ejercicio 6:
# Dado un número entero n, imprimir la suma de todos los números pares menores o iguales a n.
# n = int(input("Ingrese numero entero: "))
# contador=0
# acumulador=0

# while contador <= n:
#     if contador % 2==0:
#         acumulador+=contador

#     contador+=1

# print(acumulador)


#Ejercicio 7
#Dada una lista de números, imprimir todos los números que son mayores que el promedio de la lista.

# lista=[2,5,8,25,23]
# contador=0
# acumulador= 0
# print(lista)

# while contador < len(lista):
#     acumulador += lista[contador]
#     contador += 1

# promedio = acumulador / len(lista)

# print("El promedio de la lista es:", promedio)

# contador = 0
# while contador < len(lista):
#     if lista[contador] > promedio:
#         print(lista[contador])
#     contador += 1

#Ejercicio 8
#Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.

# cadena = input("Ingrese una palabra: ")
# contador = 0
# vocales = "aeiou"
# acumulador = 0

# while contador < len(cadena):
#     letra = cadena[contador]
#     if letra in vocales:
#         acumulador += 1
#     contador += 1

# print("Cantidad de vocales en la cadena:", acumulador)

# Ejercicio 9
#Dado un número entero n, imprimir todos los números impares menores o iguales a n.

# numero = int(input("Ingrese un numero entero: "))

# contador =0 
# acumulador=0
# while contador <= numero:
#     if contador % 2 != 0:
#         acumulador+= contador

#     contador+=1
# print(acumulador)


#Ejercicio 10
#Dada una lista de números, imprimir la cantidad de números pares en la lista.

# lista = [2, 46, 21, 12, 9]
# contador = 0
# indice = 0
# while indice < len(lista):
#     if lista[indice] % 2 == 0:
#         contador += 1
#     indice += 1
# print(f"La cantidad de números pares en la lista es: {contador}")





#Ejercicio 11
#Dada una lista de palabras, imprimir todas las palabras que tengan una longitud mayor a 5 caracteres.

# lista_palabras= ["Oso","pardo","Elefante","jirafa"]
# contador=0
# while contador < len(lista_palabras):
#     letra = lista_palabras[contador]
#     if len(letra) > 5:
#         print(letra)

#     contador+=1


#Ejercicio 12
#Dado un número entero n, imprimir la suma de todos los números impares menores o iguales a n.

# numero = int(input("Ingrese un numero entero: "))
# contador= 0
# acumulador=0
# while contador < numero:
#     if contador %2!= 0:
#         acumulador+= contador


    
#     contador+=1
# print(acumulador)



#Ejercicio 13
#Dada una lista de números, imprimir la cantidad de números negativos en la lista.

# lista= [-1,34,2,7,-8]
# indice=0
# contador = 0
# while indice < len(lista):
#     if lista[indice] < 0:
#         contador+=1
#     indice+=1

# print("La cantidad de numeros negativos de la lista es de ",contador)






#Ejercicio 14
#Dada una cadena de texto, imprimir la cantidad de veces que aparece una letra específica en la cadena.

# cadena = input("Ingrese una palabra: ")
# letra= input("Ingrese una letra especifica: ")
# contador=0
# indice=0
# while indice < len(cadena):
#     buscar = cadena[indice]
#     if buscar == letra:
#         contador += 1
#     indice += 1

# print(f"La letra '{letra}' aparece {contador} veces en la cadena.")




#Ejercicio 15
#Dado un número entero n, imprimir todos los números primos menores o iguales a n.


# numero = int(input("Ingrese un numero entero: "))

# if numero < 2:
#     print("No hay números primos menores o iguales a {0}".format(numero))
# else:
#     contador = 2
#     while contador <= numero:
#         es_primo = True
#         divisor = 2
#         while divisor < contador:
#             if contador % divisor == 0:
#                 es_primo = False
#                 break
#             divisor += 1
#         if es_primo:
#             print(contador)
#         contador += 1



#Ejercicio 16
#Dada una lista de números, imprimir todos los números que son múltiplos de 3.


# lista=[1,4,2,5,3,6,18]
# contador=0
# while contador < len(lista):
#     if lista[contador] % 3==0:
#         print(lista[contador])
#     contador+=1



#Ejercicio 17
#Dada una cadena de texto, imprimir la cadena al revés.

# palabra = input("Ingrese una palabra: ")
# invertida = ""
# i = len(palabra) - 1

# # recorre la cadena de texto en reversa y la va añadiendo a una nueva variable
# while i >= 0:
#     invertida += palabra[i]
#     i -= 1

# # imprime la cadena invertida
# print(invertida)



#Ejercicio 18
# Dado un número entero n, imprimir la suma de todos los números que son múltiplos de 5 menores o iguales a n.

# numero = int(input("Ingrese un numero entero: "))
# contador = 0
# acumulador =0
# while contador < numero:
#     contador+=1

#     if contador % 5 == 0:
#         acumulador += contador

# print(acumulador)



#Ejercicio 19
#Dada una lista de números, imprimir todos los números que son mayores que el número anterior en la lista.

# lista_numeros = [5,2,8,33,23]
# contador = 1
# while contador < len(lista_numeros):
#     if lista_numeros[contador] > lista_numeros[contador - 1]:
#         print(lista_numeros[contador])
#     contador += 1


# Ejercicio 20
#Dado un número entero n, imprimir todos los números perfectos menores o iguales a n. Los números perfectos son aquellos números enteros positivos 
# que son iguales a la suma de sus divisores propios (excluyendo al propio número). En otras palabras, 
# si sumamos todos los divisores propios de un número (excluyendo el número en sí mismo) y el resultado es igual al número, 
# entonces ese número se considera un número perfecto.

#Por ejemplo, el primer número perfecto es 6, ya que sus divisores propios son 1, 2 y 3, y 1 + 2 + 3 = 6. 
# Otros ejemplos de números perfectos son 28, 496 y 8128. Actualmente se conocen más de 50 números perfectos, y se cree que existen infinitos 
# números perfectos, aunque no se ha podido demostrar matemáticamente esta afirmación.

n = 100
numero = 1

while numero <= n:
    suma_divisores_propios = 0
    divisor = 1
    while divisor < numero:
        if numero % divisor == 0:
            suma_divisores_propios += divisor
        divisor += 1
    if suma_divisores_propios == numero:
        print(numero)
    numero += 1

















