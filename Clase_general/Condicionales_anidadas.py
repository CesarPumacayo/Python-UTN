print("=========")
print("Conversor")
print("=========\n")

print("Menú de opciones: \n")
print("Presiona 1 para convertir de número a palabra.")
print("Presiona 2 para convertir de palabra a número.\n")

opcion=int(input("¿Cuál es tu opcion deseada?: "))

if opcion == 1:
    print("\n Conversor de número a palabra.\n")

    numero= int(input("¿Cuál es el numero que deseas convertir a palabra?: "))
    if numero==1:
        print("El número es 'Uno'")
    elif numero==2:
        print("El número es 'Dos'")
    elif numero==3:
        print("El número es 'Tres'")
    elif numero==4:
        print("El número es 'Cuatro'")
    elif numero==5:
        print("El número es 'Cinco'")
    else:
        print("El número seleccionado no esta registrado")
        
elif opcion == 2:
    print("\n Conversor de palabra a numero.\n")

    palabra= input("¿Cuál es el palabra que deseas convertir a número?: ")
    palabra = palabra.lower()
    if palabra=="uno":
        print("La palabra es 1")
    elif palabra=="dos":
        print("La palabra es 2")
    elif palabra=="tres":
        print("La palabra es 3")
    elif palabra=="cuatro":
        print("La palabra es 4")
    elif palabra=="cinco":
        print("La palabra es 5")
    else:
        print("El número seleccionado no esta registrado")
else:
    print("Opcion no disponible")
    
print("Fin.")

    
    
    

