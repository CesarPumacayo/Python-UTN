# LISTAS

lista_valores= [1,33,12,-12]

print(lista_valores[1]) # 33
lista_valores[1] = 22
print(lista_valores[1]) # 22


lista_valores.append(99)
print(lista_valores[4]) #99

for valor in lista_valores:
    print(valor)

for indice in range(len(lista_valores)):
    print(lista_valores[indice])

cantidad_elementos_lista = len(lista_valores)
for indice in range(cantidad_elementos_lista):
    print(lista_valores[indice])



#DICT

dict_alumno= {"legajo":"205664", "nombre": "Juan", "apellido": "Perez"}

print("El legajo es {0} , el nombre es {1} y el apellido es {2}.".format(
                    dict_alumno["legajo"], 
                    dict_alumno["nombre"], 
                    dict_alumno["apellido"]))

dict_alumno["cuit"] = "22-12333444-9"



print("Su cuit es {0}, El legajo es {1} , el nombre es {2} y el apellido es {3}.".format(
                    dict_alumno["cuit"],
                    dict_alumno["legajo"], 
                    dict_alumno["nombre"], 
                    dict_alumno["apellido"]))


#Pedir las claves y los imprimo
claves = dict_alumno.keys()
print(claves)

#Acceder a los valores de los diccionarios

#Opcion 1 : La clave del diccionario
for clave in dict_alumno.keys():
    print(dict_alumno[clave])
    # print("La clave: {0} tiene el valor: {1}".format(clave,valor)) SE LE PODRIA AGREGAR CON MAS INFO


#Opcion 2 : La clave y valor juntos
for clave, valor in dict_alumno.items(): 
    print("La clave: {0} tiene el valor: {1}".format(clave,valor))









