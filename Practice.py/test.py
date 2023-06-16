
# Ejercicio1: par e impar


# numero_texto = input("Ingrese un numero: ")

# #validar
# numero_int = int(numero_texto)
# resto = numero_int % 2
# if(resto == 0):
#     print("El numero ingresado es par")
# else:
#     print("El numero ingresado es impar")


# # Ejercicio2: imprimir desde 1 al que n° que ingresaste con condicion while

# numero_texto = input("Ingrese un numero: ")

# #validar
# numero_int = int(numero_texto)

# contador= 1
# while(contador <= numero_int):  #"<=" te cuenta lo que ingresaste 
#     print(contador)
#     contador = contador + 1 # contador += 1



# Ejercicio3: range
lista_numeros = [0,1,2,3] #es equivalente a : lista_numeros= list(range(4))


for numero in lista_numeros:
    print(numero)


lista_de_nombres = ["Lio","Ema","Vero"]

for nombre in lista_de_nombres:
    print(nombre)


# lista_de_nombres = ["Lio","Ema","Vero"]
# cantidad_elementos = len(lista_de_nombres)

# for indice in range(cantidad_elementos):
#     print(lista_de_nombres[indice])

lista_numeros = [1,2,4,5,77,-1]

for numero in lista_numeros:
    if(numero == 5):
        continue  # 1 2 4 77 -1 || break: 1 ,2 ,4
    print(numero, end=" ")


lista_de_nombres = ["LIO","EMA","VERO","LIO","EMA","VERO"]

for indice in range(10):
    if(lista_de_nombres[indice]== "VERO"):
        break
    print(lista_de_nombres[indice])

lista_numeros_texto = []


# AGREGAR UNA LISTA
# for indice in range(10):
#     numero_texto = input("Numero:")
#     if(numero_texto == "EXIT"):
#         break
#     lista_numeros_texto.append(numero_texto)



# texto = input("Ingrese orden: ")

# match texto:
#     case "SALTAR":
#         print("SALTAR La orden es...." + texto)
#     case "CORRER":
#         print("CORRER La orden es...{0}".format(texto))
#     case other:
#         print("La orden es....{0}".format(texto))



