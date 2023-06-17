print("***************************************************************************")
print("* Programa para determinar ¿Cúal es el número mas grande de tres números? *")
print("***************************************************************************")

numero_uno= int(input("\n Introduce el primer número: "))
numero_dos= int(input("\n Introduce el segundo número:"))
numero_tres= int(input("\n Introduce el tercer número:"))

if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El número ", numero_uno , " es el mas grande de los 3...")
elif numero_dos > numero_uno and numero_dos > numero_tres:
    print("El número ", numero_dos , " es el mas grande de los 3...")
elif numero_tres >  numero_uno and numero_tres >  numero_dos:
    print("El número ", numero_tres , " es el mas grande de los 3...")
print("Fin.")
    
