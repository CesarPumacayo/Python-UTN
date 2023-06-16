#César Pumacayo 1°E grupo giovanni

#EJERCICIOS DEL IF


# Ejercicio 1
#  Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número ingresado es positivo" si el número es mayor que cero, o "El número ingresado es cero o negativo" si el número es menor o igual a cero.


# numero = int(input("Ingrese el numero: "))



# if(numero > 0):
#     print("El número ingresado es positivo")
# elif(numero <= 0):
#     print("El número ingresado es cero o negativo")




# Ejercicio 2
# Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, o "Eres menor de edad" si la edad es menor a 18.


# edad= int(input("Ingrese la edad: "))

# if(edad >= 18):
#     print("Eres mayor o igual a 18")
# elif(edad < 18):
#     print("Eres menor edad")


# Ejercicio 3

# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número ingresado es par" si el número es divisible por 2, o "El número ingresado es impar" si el número no es divisible por 2.


# numero = int(input("Ingrese un número entero: "))


# resto = numero % 2

# if(resto == 0):
#     print("El numero ingresado es par")
# else:
#     print("El numero ingresado es impar")



# Ejercicio 4

# Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo, "El segundo número es mayor" si el segundo número es mayor que el primero, o "Los dos números son iguales" si los dos números son iguales.

# numeroUno= int(input("Ingrese el primer numero: "))
# numeroDos= int(input("Ingrese el segundo numero: "))

# if(numeroUno > numeroDos):
#     print("El primer número es mayor")
# elif(numeroUno == numeroDos):
#     print("Los dos números son iguales")
# else:
#     print("El segundo número es mayor")


# Ejercicio 5

# Escribir un programa que le pida al usuario que ingrese su nombre, y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro", o "Hola desconocido" si el nombre ingresado no es uno de esos tres.

# nombre = input("Ingrese el nombre: ")

# if(nombre == "Juan"):
#     print("Hola " + nombre)
# elif(nombre == "María"):
#     print("Hola " + nombre)
# elif(nombre == "Pedro"):
#     print("Hola " + nombre)
# else:
#     print("Hola Desconocido")

# Ejercicio 6

# Escribir un programa que le pida al usuario que ingrese su nombre y su edad, y luego imprima "Puedes votar" si la edad es mayor o igual a 18 y menor o igual a 65, o "No puedes votar" si la edad es menor a 18 o mayor a 65.

# nombre = input("Ingrese el nombre: ")
# edad= int(input("Ingrese la edad: "))


# if(edad >= 18 and edad <= 65):
#     print("Puedes votar")
# else:
#     print("No puedes votar")

# Ejercicio 7

# Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número es primo" si el número es primo, 
# o "El número no es primo" si el número no es primo.

# numero = int(input("Ingrese el numero positivo: "))

# primo= True

# for n in range(2,numero):
#     if numero % n == 0: 
#         print("No es primo", n , "es divisor")
#         primo= False
#         break
# if primo:
#     print("Es primo")


# # Ejercicio 8

# Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número es un cuadrado perfecto" 
# si el número es un cuadrado perfecto, o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.

# numero = int(input("Ingrese con un numero positivo:"))

# if(numero== 4):
#     print("¡WOW!, es un cuadrado perfecto")
# else:
#     print("El número no es un cuadrado perfecto")




# Ejercicio 9

# Escribir un programa que le pida al usuario que ingrese una letra, y luego imprima "Es una vocal" 
# si la letra es una vocal (a, e, i, o, u), o "Es una consonante" si la letra es una consonante.


# letra= input("Ingrese la letra: ")

# if(letra=="a"or
#    letra=="e"or
#    letra=="i"or
#    letra=="o"or
#    letra=="u"):
#     print("Es una consonante")
# else:
#     print("Es una vocal")
    

# Ejercicio 10

# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es positivo y par" 
# si el número es positivo y divisible por 2, o "El número no cumple ninguna condición" si el número no cumple ninguna de las dos condiciones anteriores.

# numero = int(input("Ingresa un número entero: "))

# if numero > 0 and numero % 2 == 0:
#     print("El número es positivo y par")
# elif numero > 0 and numero % 2 != 0:
#     print("El número es positivo e impar")
# elif numero < 0 and numero % 2 == 0:
#     print("El número es negativo y par")
# elif numero < 0 and numero % 2 != 0:
#     print("El número es negativo e impar")
# else:
#     print("El número es cero")

#  Manera mas simplificada 

# numero = int(input("Ingresa un número entero: "))

# if numero % 2 == 0:
#     paridad = "par"
# else:
#     paridad = "impar"

# if numero > 0:
#     positividad = "positivo"
# elif numero < 0:
#     positividad = "negativo"
# else:
#     positividad = "cero"

# print("El número es", positividad, "y", paridad)


# Ejercicio 11

# Escribir un programa que le pida al usuario que ingrese su edad, 
# y luego imprima "Eres un niño" si la edad es menor a 12, "Eres un adolescente" si la edad está entre 12 y 17 inclusive, "Eres un adulto" si la edad está entre 18 y 64


# numero = int(input("Ingrese su edad: "))

# if(numero < 12):
#     print("Eres un niño")
# elif(numero >= 12 and numero <=17):
#     print("Eres un adolescente")    
# else:
#     if(numero >=18 and numero <=64):
#         print("Eres un adulto")


# Ejercicio 12
# Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima "El primer número es positivo" si el primer número es mayor que cero, "El segundo número es positivo" si el segundo número es mayor que cero, o "Ambos números son negativos" si los dos números son negativos.


# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# mensaje = ""

# if(num1 > 0):
#     mensaje += "El primer número es positivo. "
# if(num2 > 0):
#     mensaje += "El segundo número es positivo. "
# if(num1 <= 0 and num2 <= 0):
#     mensaje += "Ambos números son negativos. "

# print(mensaje)


# Ejercicio 13

# Escribir un programa que le pida al usuario que ingrese 
# un número entero, y luego imprima "El número es divisible por 3 y por 5" si el número es divisible por 3 y por 5, o "El número no es divisible por 3 y por 5" si el número no es divisible por 3 y por 5.

# numero = int(input("Ingresa un número entero: "))

# if numero % 3 == 0 and numero % 5 == 0:
#     print("El número es divisible por 3 y por 5")
# else:
#     print("El número no es divisible por 3 y por 5")


# Ejercicio 14

# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es múltiplo de 4 y de 6" si el número es múltiplo de 4 y de 6, o "El número no es múltiplo de 4 y de 6" si el número no es múltiplo de 4 y de 6.


# numero = int(input("Ingrese numero:"))

# if numero % 4 == 0 and numero % 6== 0:
#     print("El numero es multiplo de  4 y 6")
# else:
#     print("No es multiplo de 4 y 6")

#Ejercicio 15

# Escribir un programa que le pida al usuario que ingrese un número entero positivo, 
# y luego imprima "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.

# numero = int(input("Ingrese un número entero positivo: "))

# if numero < 2:
#     print("El número no es primo.")
# else:
#     es_primo = True
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             es_primo = False
#             break
#     if es_primo:
#         print("El número es primo.")
#     else:
#         print("El número no es primo.")

#Ejercicio 16

# Escribir un programa que le pida al usuario que ingrese su nombre y su edad, y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive, 
# "Eres adulto" si la edad está entre 18 y 64 inclusive, o "Eres adulto mayor" si la edad es mayor o igual a 65.

# nombre= input("Ingrese el nombre:")
# edad= int(input("Ingrese la edad del usuario: "))

# if edad >=13 and edad <17:
#     print("Eres adolescente")
# elif edad >= 18 and edad <=64:
#     print("Eres adulto")
# elif edad >= 65:
#     print("Eres adulto mayor")

#Ejercicio 17


# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima 
# "El número es negativo" si el número es menor que cero, "El número es cero" si el número es igual a cero, o "El número es positivo" si el número es mayor que cero.

# numero= int(input("Ingrese un numero entero: "))

# if numero < 0:
#     print("El número es negativo")
# elif numero == 0:
#     print("El número es igual a 0")
# else: 
#     print("El número es positivo")


#Ejercicio 18

# Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es par y es múltiplo de 3"
#  si el número es par y es múltiplo de 3, o "El número no cumple ninguna de las dos condiciones" si el número no cumple ninguna de las dos condiciones.


# numero = int(input("Ingrese un número entero: "))

# if numero %2 == 0 and numero % 3 ==0:
#     print("Es número par y es multiplo de 3")
# else:
#     print("El número no cumple ninguna de las dos condiciones")

#Ejercicio 19

# Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, "Eres adolescente" si la edad está entre 13 y 17 inclusive, o "Eres menor de edad" si la edad es menor que 13.

# edad = int(input("Ingrese la edad: "))

# if edad >= 18:
#     print("Eres mayor de edad")
# elif edad >=13 and edad <=17:
#     print("Eres adolescente")
# elif edad < 13:
#     print("Eres de menor edad")

#Ejercicio 20


# Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima "Los dos números son iguales" si los dos números son iguales, 
# "El primer número es mayor" si el primer número es mayor que el segundo, o "El segundo número es mayor" si el segundo número es mayor que el primero.

# numero_uno= int(input("Ingrese el primer numero: "))
# numero_dos= int(input("Ingrese el segundo numero: "))

# if numero_uno == numero_dos:
#     print("Los dos números son iguales")
# elif numero_uno > numero_dos:
#     print("El primer número es mayor")
# else: 
#     print("El segundo número es mayor")
