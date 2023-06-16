# César Pumacayo 1°E grupo giovanni

diccionario_de_miembros= [{"id": 100,"nombre":"JUAN", "edad": 22,"membresia": "ANUAL" },
                          {"id": 200,"nombre":"VERONICA", "edad": 35,"membresia": "MENSUAL"}
                        ]

auxiliar_miembro = {}


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
        auxiliar_miembro["id"]= int(input("Ingrese el numero de identificacion: "))
        auxiliar_miembro["nombre"] = input("Ingrese el nombre: ")
        auxiliar_miembro["edad"]= int(input("Ingrese la edad: "))
        auxiliar_miembro["tipoMembresia"] = input("Ingrese el tipo de membresia: ")
        while auxiliar_miembro["tipoMembresia"] != "mensual" and auxiliar_miembro["tipoMembresia"] != "anual":
            print("Error, no ingresaste el tipo correcto.")
            auxiliar_miembro["tipoMembresia"] = input("Ingrese el tipo de membresia NUEVAMENTE: ")

        diccionario_de_miembros.append(auxiliar_miembro)
        pass


       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":

        print("Nro ID.\tNombre\tEdad\tTipo membresia")
        for miembro in diccionario_de_miembros:
            print("{0}\t{1}\t{2}\t{3}".format(miembro["id"], miembro["nombre"], miembro["edad"], miembro["membresia"]))         
       
        # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        modificacion = int(input("Ingrese el id para modificar: "))

        for miembro in diccionario_de_miembros:
            if miembro["id"] == modificacion:
                nueva_membresia = input("Ingrese el nuevo tipo de membresía: ")
                while nueva_membresia.lower() not in ("mensual", "anual"):
                    print("ERROR, REINGRESE NUEVAMENTE")
                    nueva_membresia = input("Ingrese el nuevo tipo de membresía CORRECTAMENTE: ")

                miembro["membresia"] = nueva_membresia

                print("{0}\t{1}\t{2}\t{3}".format(miembro["id"], miembro["nombre"], miembro["edad"], miembro["membresia"]))

                break
        else:
            print("NO SE ENCONTRÓ")



        pass
        # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        busqueda = int(input("Ingrese el id del miembro: "))
        encontrado = False
        for miembro in diccionario_de_miembros:
            if miembro["id"] == busqueda:
                encontrado = True
                print("Nombre:", miembro["nombre"])
                print("Edad:", miembro["edad"])
                print("Membresía:", miembro["membresia"])

        if not encontrado:
            print("El miembro no se encuentra en la lista.")
        
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        acumulador = 0
        for miembro in diccionario_de_miembros:
            acumulador += miembro["edad"]
        promedio = acumulador / len(diccionario_de_miembros)
        print(f"El promedio de edad de los miembros es: {promedio}")
        pass

    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        joven = diccionario_de_miembros[0]
        viejo = diccionario_de_miembros[0]

        for miembro in diccionario_de_miembros:
            if miembro["edad"] < joven["edad"]:
                joven = miembro
            if miembro["edad"] > viejo["edad"]:
                viejo = miembro

        print(f"El miembro más joven es: {joven['nombre']} ({joven['edad']} años), con id {joven['id']}")
        print(f"El miembro más viejo es: {viejo['nombre']} ({viejo['edad']} años), con id {viejo['id']}")


        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")


