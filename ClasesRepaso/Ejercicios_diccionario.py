mi_lista=[1,2,"marina",["a","b","c"],True]
mi_lista[3]


notas_1=[7,8,9]
notas_2= [10,8,9]
alumnos= ["pepe","juan","emma"]



#Tres listas por su indice
for i in range(3):
    print(f"Alumno:{alumnos[i]} Primera Nota: {notas_1[i]}, Segunda Nota {notas_2[i]}")


mi_dic= {"nonbre": "marina" , "apellido": ["cardozo","pagura"]}
print(mi_dic["apellido"])

mi_dic["edad"]= 21

print(mi_dic)

mi_dic["edad"] = 15 #agrega la clave
print(mi_dic)

del mi_dic["edad"]  #elimina esta clave

print(mi_dic)