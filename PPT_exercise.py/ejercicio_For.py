#César Pumacayo 1°e grupo Giovanni
# Ejercicios del FOR

# ejercicio 1
# Dada una lista de números, imprimir el número más grande de la lista.


# numeros = [5,23,99,2,78]

# numeroAlto= numeros[0]

# for i in numeros:
#     if i > numeroAlto:
#         numeroAlto = i


# print(numeroAlto)





#Ejercicio 2
# Dada una lista de palabras, imprimir la palabra más larga de la lista.


# lista=["Hola","Jorge","Palabra","Bienvenido","Pi"]
# listaMax= ""

# for i in lista:
#     if len(i) > len(listaMax):
#         listaMax = i

# print(listaMax)





#Ejercicio 3
# Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.

# n = int(input("Introduce un número entero: "))

# for i in range(2, n+1, 2):
#     print(i)





#Ejercicio 4
# Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.

# n = int(input("Ingrese el numero entero: "))
# acumulador= 0

# for i in range(1,n+1,2):
#     acumulador += i
    
# print(acumulador)





#Ejercicio 5
# Dada una lista de números, imprimir el número más pequeño de la lista.

# lista= [12,5,2,68,4,1,99]
# lista_menor= lista[0]

# for i in lista:
#     if i < lista_menor:
#         lista_menor = i

# print(lista_menor)






#Ejercicio 6
# Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

# lista_palabra= ["hola", "german", "bienvenido", "oso", "elefante"]
# vocales = "aeiou"
# acumulador=0

# for palabra in lista_palabra:
#     for letra in palabra:
#         if letra.lower() in vocales: 
#             acumulador+=1

# print(acumulador)






#Ejercicio 7
#Dado un número entero n, imprimir la secuencia de números impares menores o iguales a n.

# n= int(input("Ingrese un numero entero: "))

# for i in range(1,n+1,2):
#     print(i)






#Ejercicio 8
#Dado un número entero n, imprimir la suma de los números pares menores o iguales a n.

# n= int(input("ingrese el numero entero: "))
# acumuladorPar=0

# for i in range(2, n+1,2):
#     acumuladorPar+= i

# print(acumuladorPar)





    
#Ejercicio 9
# Dada una lista de números, imprimir la cantidad de números negativos en la lista.

# lista= [2,87,-53,42,69,-53,-21]
# acumuladorNegativo= 0

# for i in lista:
#     if i < 0:
#         acumuladorNegativo+= i
# print(acumuladorNegativo)





#Ejercicio 10
# Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.

# lista = ["ana", "oso", "casa", "perro", "raton", "reconocer"]

# for palabra in lista:
#     if palabra[0] == palabra[-1]:
#         print(palabra)

        



#Ejercicio 11
# Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n.

# n = int(input("ingresa un numero entero: "))

# for i in range(2, n+1):  # empieza en 2 y termina en el numero que le ingrese
#     primo=True
#     for j in range(2,i):
#         if i % j == 0 and i % 1 == 0:  # i se divide por j y de resto tiene que dar "0" y tambien el i(mismo numero que ingresaste) dividido con el numero que ingresaste te de resto "0"
#             primo=False
#     if primo:
#         print("Es primo: {}".format(i))
            




#Ejercicio 12
# Dada una lista de números, imprimir la cantidad de números pares en la lista.


# lista= [156,21,4,6,231,11]

# for i in lista:
#     if i % 2 == 0:
#         print(i)


#Ejercicio 13
# Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

# lista = ["Jorge","Barcacoa","Merluza","Mostaza","Avioneta"]

# for i in lista:
#     if len(i) % 2 != 0:
#         print(i)





#Ejercicio 14
#Dado un número entero n, imprimir la secuencia de números perfectos menores o iguales a n.

# n = int(input("Ingrese un número entero positivo: "))
# print("Los números perfectos menores o iguales a", n, "son:")

# for i in range(1, n+1):
#     acumulador_suma = 0
#     for j in range(1, i):
#         if i % j == 0:
#             acumulador_suma += j
#     if acumulador_suma == i:
#         print(i)





#Ejercicio 15
# Dada una lista de números, imprimir la cantidad de números impares en la lista.

# lista= [2,6,31,32,21,9]

# contador= 0

# for i in lista:
#     if i % 2 != 0:
#         contador+=1
# print("La cantidad de palabras impares son {}".format(contador))





#Ejercicio 16
# Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

# lista= ["hola", "Bienvenido", "Mundo" , "objetivo", "Destreza"]

# letra= input("Ingrese una letra especifica: ")

# for i in lista:
#     for palabra in i: 
#         if palabra.lower() in letra:
#             print(i)





#Ejercicio 17
#Dado un número entero n, imprimir la secuencia de números de Harshad menores o iguales a n.  DUDASSSFWEFWEFWEFEW

# numero = int(input("Ingresa un número: "))
# suma = 0

# for digito in str(numero):
#     suma += int(digito)
#     dividir = numero / suma
    
#     for j in digito:

# n = int(input("Ingresa un número: "))

# for i in range(1, n+1):
#     suma_digitos = 0
#     for digito in str(i):
#         suma_digitos += int(digito)
#     if i % suma_digitos == 0 and i <= n:
#         print(i)




#Ejercicio 18
# Dada una lista de números, imprimir la suma de los números en la lista que son mayores que el promedio de la lista.

# lista = [2, 54, 23, 1, 7]
# acumulador = 0

# for i in lista:
#     acumulador += i

# cantidad_numeros = len(lista)
# promedio_numeros = acumulador / cantidad_numeros

# suma_mayores = 0
# for i in lista:  #suma el 54 y 23 ya que supera el promedio
#     if i > promedio_numeros:
#         suma_mayores += i

# print("La suma de los números mayores que el promedio es:", suma_mayores)





#Ejercicio 19
#Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula.

# lista = ["Mundo","Tres","naranja","molusco","Caja"]

# for i in lista:
#     for letra in i:
#         if letra.isupper():
#             print(i)
        

#Ejercicio 20
# Dado un número entero n, imprimir la secuencia de números triangulares menores o iguales a n.

n = int(input("Ingrese un número entero: "))

triangular = 0

for i in range(1, n+1):
    triangular += i  # Agregar el número actual a la suma
    if triangular > n:
        break
    print(triangular)







        
 

