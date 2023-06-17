edad = input("Ingrese una edad")

print(edad)
print(type(edad))

edad = int(edad)
print(type(edad))

edad = edad + 2 

print(edad)

# edad = str(edad) es mas util 

# print("La edad sumada es ", edad)

print("La edad sumada es {0} ".format(edad))

print("La edad sumada es " + str(edad)) 
