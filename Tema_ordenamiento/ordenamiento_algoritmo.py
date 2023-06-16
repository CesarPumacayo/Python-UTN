#Algoritmo de ordenamiento

lista = [1,22,3,1,45,8]
# print(lista)

# rango_a = len(lista) # rango_a len(lista) pero entra while y rango_a resta 1 EL A TIENE QUE LLEGAR LA POSICION 5
# flag_swap = True

# while(flag_swap):
#     flag_swap = False
#     rango_a = rango_a - 1 # ES PARA QUE NO COMPARE MAYOR CON MAYOR AL FINAL DE LA LISTA AHORRAMOS PROCESAMIENTO Y TIEMPO

#     for indice_A in range(rango_a):
#         if lista[indice_A] > lista[indice_A+1]:
#             # aux = lista[indice_A] #ES UN VALOR NO UNA LISTA
#             # lista[indice_A] = lista[indice_A+1]
#             # lista[indice_A+1] = aux
#             lista[indice_A],lista[indice_A+1] = lista[indice_A+1] , lista[indice_A]
#             flag_swap = True#VA HACER SWAP HASTA QUE LA LISTA ESTE ORDENADA

# print(lista)

import random 
import time

def ivan_sort_A(lista_original:list):
    lista = lista_original[:]
    rango_a = len(lista)
    flag_swap = True

    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if  lista[indice_A] < lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True
    return lista

# print(ivan_sort_A(lista))

def ivan_sort_B(lista_original:list,flag_orden:bool):
    lista = lista_original[:]
    rango_a = len(lista) - 1
    flag_swap = True

    while(flag_swap):
        flag_swap = False

        for indice_A in range(rango_a): #Todo junto
            if  flag_orden == False and lista[indice_A] < lista[indice_A+1] \
             or flag_orden == True and lista[indice_A] > lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True

def quick_sort(lista_original:list, flag_orden:bool)->list:
    # 8 11 0 1 3 2 10
    #pivot 8
    #list iz 0 1 3 2
    #list de 11 10
    lista_de = [] #lista derecha
    lista_iz = [] #lista izquierda
    if len(lista_original)<=1:
        return lista_original
    else:
        pivot= lista_original[0]#puede ser al azar o no
        for elemento in lista_original[1:]: #ignoro el 0
            if elemento > pivot:
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    # list_ iz| 0 1 3 2
    lista_iz = quick_sort(lista_iz, True)
    #list_iz| 0 1 2 3
    lista_iz.append(pivot)# lista_iz| 0 1 2 3 8
    #list_de| 11 10
    lista_de = quick_sort(lista_de, True) 
    #list_de| 10 11
    lista_iz.extend(lista_de) # 0 1 2 3 8 10 11 

    return lista_iz


lista = list(range(10000)) 
random.shuffle(lista) # MEZCLA LISTA ALEATORIA

# Copia profundo genero un espacio de memoria de manera conjunta
lista_A = lista[:]
lista_B = lista[:]
lista_C = lista[:]


inicio = time.time()
ivan_sort_A(lista_A)

fin = time.time()

print("IVAN_A {0}".format((fin-inicio)))


# inicio = time.time()
# ivan_sort_B(lista_B,True)
# fin = time.time()
inicio = time.time()
lista_ordenada = quick_sort(lista_C,True)
fin = time.time()

print("QSORT {0}".format((fin-inicio)))



inicio = time.time()
ivan_sort_A(lista_A)
fin = time.time()

print("IVAN_A_YA ORDENADO {0}".format((fin-inicio)))


#Ejemplo recursividad
# def factorial_recursive(n: int) -> int:
#     if n < 2:
#         return 1
#     return n * factorial_recursive(n - 1)



