lista_identificacion=[1,2,3,4]
lista_nombre=["Cesar","Juan","Diego","Carlos"]
lista_edad= [20,19,32,41]
lista_membresia= ["anual","mensual","mensual", "anual"]

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        
        identificacion= int(input("Ingrese el numero de identificacion: "))
        nombre = input("Ingrese el nombre: ")
        edad= int(input("Ingrese la edad: "))
        tipoMembresia = input("Ingrese el tipo de membresia: ")
        while tipoMembresia != "mensual" and tipoMembresia != "anual":
            print("Error, no ingresaste el tipo correcto.")
            tipoMembresia = input("Ingrese el tipo de membresia NUEVAMENTE: ")
        
        lista_identificacion.append(identificacion)
        lista_nombre.append(nombre)
        lista_edad.append(edad)
        lista_membresia.append(tipoMembresia)

                    
        pass
        # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
        for i in range(len(lista_identificacion)):
 
            print("{0}\t{1}\t{2}\t{3}".format(lista_identificacion[i], lista_nombre[i], lista_edad[i], lista_membresia[i]))
        
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        modificacion = int(input("Ingrese el id para modificar: "))
        if modificacion in lista_identificacion:
            indice = lista_identificacion.index(modificacion)
            nueva_membresia = input("Ingrese el nuevo tipo de membresía: ")
            while nueva_membresia != "mensual" and nueva_membresia != "anual":
                print("ERROR, REINGRESE NUEVAMENTE")
                nueva_membresia = input("Ingrese el nuevo tipo de membresía CORRECTAMENTE: ")
   

            lista_membresia[indice] = nueva_membresia
            print("{0}\t{1}\t{2}\t{3}".format(lista_identificacion[indice], lista_nombre[indice], lista_edad[indice], lista_membresia[indice]))
        else: 
            print("NO SE ENCONTRÓ")
            break

    # Opción 4: Buscar información de un miembro

    elif opcion == "4":
        modificacion_Usuario= int(input("Ingrese el numero de identificacion : "))

        if modificacion_Usuario in lista_identificacion:
            indice= lista_identificacion.index(modificacion_Usuario)
        print("{0}\t{1}\t{2}\t{3}".format(lista_identificacion[indice], lista_nombre[indice], lista_edad[indice], lista_membresia[indice]))
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        acumulador = sum(lista_edad)

        promedio = acumulador / len(lista_edad)

        print("El promedio es : {0}".format(promedio))
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    # Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y mínima en la lista de edades y mostrar el nombre y número de identificación 
    # correspondientes en las listas de nombres y números de identificación.
    elif opcion == "6":

        mas_joven = lista_edad[0]
        mas_mayor = lista_edad[0]
        nombre_joven = ""
        nombre_mayor = ""
        identificacion_joven = ""
        identificacion_mayor = ""

        for i in range(len(lista_edad)):
            if lista_edad[i] > mas_mayor:
                nombre_mayor = lista_nombre[i]
                identificacion_mayor = lista_identificacion[i]
                mas_mayor = lista_edad[i]
            elif lista_edad[i] < mas_joven:
                nombre_joven = lista_nombre[i]
                identificacion_joven = lista_identificacion[i]
                mas_joven = lista_edad[i]

        print("El miembro más joven es {0}, con ID {1} y edad {2}".format(nombre_joven, identificacion_joven, mas_joven))
        print("El miembro más viejo es {0}, con ID {1} y edad {2}".format(nombre_mayor, identificacion_mayor, mas_mayor))

        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")
