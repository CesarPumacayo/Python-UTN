
# 3) Copa pistón!!!
# Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
# Se pedirá el ingreso de:
# nombre
#  edad (mayor a 18)
# nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
#  cantidad de carreras ganadas (no pueden ser números negativos)
#  número del vehículo (no puede ser un número negativo)
# se necesita saber:
# *Nacionalidad del piloto más joven.
# *Cantidad de vehículos con número par.
# *Nombre del piloto con menos victorias y el número de auto impar.
# *Cantidad de pilotos mayores de 25 años con número de vehículo impar.
# *Nombre del piloto más joven con más victorias.
# *Nacionalidad del piloto más veterano con menos victorias.
# *Promedio de edad de los pilotos que tiene un vehículo con número par.


# contador = 0
# maximo= 0
# bandera =0
# masJoven = 0
# nacionalidadMasJoven= ""
# contadorPares =0

# menosVictorias = 0
# nombrePerdedor= ""
# banderaPerdida= 0
# contadorPilotosMas25años= 0
# banderaVictorias= 0
# masVictorias= 0
# masJoven2=0

# nombreJoven= ""


# Masviejo = 0
# masPerdidasViejo= 0
# banderaViejoPerdido= 0

# promedioEdad= 0
# acumuladorEdad= 0
# nacionalidadVeterano= ""
# vehiculoImpar=""


# while contador < 3:
#     nombre = input("Ingrese su nombre: ")
#     edad = int(input("Ingrese su edad"))
#     while edad < 18:
#         print("Error, reingrese una edad mayor a 18")
#     nacionalidadPiloto= input("Ingrese su nacionalidad")
#     while nacionalidadPiloto != "argentino" and nacionalidadPiloto != "ingles" and nacionalidadPiloto != "frances" and nacionalidadPiloto != "brasilero" and nacionalidadPiloto != "estadounidense":
#         print("Error, Reingrese la nacionalidad")
#     cantidadGanadas= int(input("Ingrese la cantidad de carreras ganadas"))
#     while cantidadGanadas < 0:
#         print("Error,reingrese un numero que sea positivo")
#     numeroVehiculo= int(input("Ingrese el numero del vehiculo que no sea negativo"))
#     while numeroVehiculo < 0:
#         print("Error, reingrese el numero del vehiculo que sea POSITIVO")


#     if edad < masJoven or bandera == 0:
#         masJoven = edad
#         nacionalidadMasJoven = nacionalidadPiloto
#         bandera = 1

#     elif numeroVehiculo % 2 == 0:
#         contadorPares+=1
#         acumuladorEdad+= edad

#     elif cantidadGanadas < menosVictorias or banderaPerdida == 0:
#         menosVictorias = cantidadGanadas
#         nombrePerdedor = nombre
#         banderaPerdida = 1

#         if numeroVehiculo % 2 != 0:
#             vehiculoImpar= numeroVehiculo
#         else:
#             print("No se encontro impar del vehiculo")

#     elif numeroVehiculo % 2 != 0 and edad > 25:
#         contadorPilotosMas25años+=1
#     elif edad < masJoven2 and cantidadGanadas > masVictorias or banderaVictorias == 0:
#         masJoven2 = edad
#         nombreJoven= nombre
#         masVictorias = cantidadGanadas
#         banderaVictorias =1
#     elif edad > Masviejo and cantidadGanadas < masPerdidasViejo or banderaViejoPerdido == 0:
#         Masviejo = edad
#         masPerdidasViejo = cantidadGanadas
#         nacionalidadVeterano = nacionalidadPiloto
#         banderaViejoPerdido= 1
    

#     contador+=1

# promedioEdad = acumuladorEdad // contador


# print("La nacionalidad del piloto mas joven es {0} y su edad es {1}".format(nacionalidadMasJoven,masJoven))
# print("La cantidad de vehiculos pares son {}".format(contadorPares))
# print("Nombre del piloto con menos victorias es {0} y el número de auto impar es {1}".format(nombrePerdedor, vehiculoImpar))
# print("Cantidad de pilotos mayores de 25 años son {0} y con número de vehículo impar {1}".format(contadorPilotosMas25años, vehiculoImpar))
# print("Nombre del piloto más joven se llama {0} con más victorias.".format(nombreJoven))
# print("Nacionalidad del piloto más veterano con menos victorias es {0}".format(nacionalidadVeterano))
# print("Promedio de edad de los pilotos que tiene un vehículo con número par es {0}".format(promedioEdad))


#-------------------------------------------------------------------------------------------------------------------------------------------------------


# 3) Copa pistón!!!
# Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
# Se pedirá el ingreso de:
# nombre
#  edad (mayor a 18)
# nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
#  cantidad de carreras ganadas (no pueden ser números negativos)
#  número del vehículo (no puede ser un número negativo)

# se necesita saber:

# *Nacionalidad del piloto más joven.
# *Cantidad de vehículos con número par.
# *Nombre del piloto con menos victorias y el número de auto impar.
# *Cantidad de pilotos mayores de 25 años con número de vehículo impar.
# *Nombre del piloto más joven con más victorias.
# *Nacionalidad del piloto más veterano con menos victorias.
# *Promedio de edad de los pilotos que tiene un vehículo con número par.

edadJoven= 0
nacionalidad_Joven= ""
banderaJoven=0

contador_vehiculo_par= 0

menos_Victorias= 0
nombre_menos_victorias = ""
mensajeImpar= ""
vehiculoImpar_perdedor= 0 
bandera_menos_Victorias= 0

contador25años_vehiculoImpar = 0

nombreJoven_Victoria= ""
mas_Victorias= 0
banderaVictoria= 0
nacionalidadMasEdad=""


mas_edad= 0
banderaVeterano= 0
banderaVeterano2= 0



menos_VictoriasVeterano = 0
nacionalidadVeterano_Perdedor = ""
edadMenosVictoriasVeterano= 0


PromedioEdad= 0
acumuladorEdad = 0
contador= 0

while contador < 3:


    nombre = input("Ingrese el nombre del piloto: ")
    edad= int(input("Ingrese la edad del piloto: (mayor a 18) "))

    nacionalidad_piloto = input("Ingrese la nacionalidad del piloto: argentino, ingles, frances, brasilero o estadounidense")
    while nacionalidad_piloto.lower() not in ["argentino", "ingles", "frances", "brasilero", "estadounidense"]:
        print("La nacionalidad ingresada no es válida. Por favor, ingrese una nacionalidad válida.")
        nacionalidad_piloto = input("Ingrese la nacionalidad del piloto: argentino, ingles, frances, brasilero o estadounidense: ")

    carreras_ganadas = int(input("Ingrese la cantidad de carreras ganadas: (debe ser un número no negativo): "))
    while carreras_ganadas < 0:
        print("Error: el valor ingresado es negativo.")
        carreras_ganadas = int(input("Ingrese la cantidad de carreras ganadas: (debe ser un número no negativo): "))

    numero_Vehiculo= int(input("Ingrese el numero del vehiculo: (no debe ser negativo): "))
    while numero_Vehiculo < 0:
        print("Error: el valor ingresado es negativo.")
        numero_Vehiculo= int(input("Ingrese el numero del vehiculo: (no debe ser negativo): "))


    if edad < edadJoven or banderaJoven== 0:
        edadJoven = edad
        nacionalidad_Joven = nacionalidad_piloto
        banderaJoven = 1
        if carreras_ganadas > mas_Victorias or banderaVictoria == 0:
            mas_Victorias = carreras_ganadas
            nombreJoven_Victoria= nombre
            banderaVictoria= 1

    if numero_Vehiculo % 2 ==0:
        contador_vehiculo_par+=1
        acumuladorEdad+= edad

    if carreras_ganadas < menos_Victorias or bandera_menos_Victorias== 0:
        menos_Victorias = carreras_ganadas
        nombre_menos_victorias= nombre
        if numero_Vehiculo % 2 != 0:
            vehiculoImpar_perdedor= numero_Vehiculo
        bandera_menos_Victorias= 1

    if edad > mas_edad:
        mas_edad = edad
        nacionalidadMasEdad= nacionalidad_piloto
        if carreras_ganadas < menos_VictoriasVeterano or banderaVeterano2== 0:
            menos_VictoriasVeterano = carreras_ganadas
            nacionalidadVeterano_Perdedor = nacionalidad_piloto
            banderaVeterano2= 1
    elif edad == mas_edad and carreras_ganadas < menos_VictoriasVeterano:
        menos_VictoriasVeterano= carreras_ganadas
        nacionalidadVeterano_Perdedor= nacionalidad_piloto

   
    if numero_Vehiculo %2 != 0:
        if edad > 25:
            contador25años_vehiculoImpar+=1

    contador+=1

PromedioEdad = acumuladorEdad // contador

print("Nacionalidad del piloto más joven es {0}.".format(nacionalidad_Joven))
print("Cantidad de vehículos con número par es {0}.".format(contador_vehiculo_par))
print("Nombre del piloto con menos victorias se llama {0}  y el número de auto impar: {1}.".format(nombre_menos_victorias, vehiculoImpar_perdedor))
print("Cantidad de pilotos mayores de 25 años con número de vehículo impar son {0}".format(contador25años_vehiculoImpar))
print("Nombre del piloto más joven con más victorias es {0}.".format(nombreJoven_Victoria))

if edad != mas_edad:

    print("Nacionalidad del piloto más veterano con menos victorias es {0}.".format(nacionalidadMasEdad))
elif edad == mas_edad:
    print("Nacionalidad del piloto más veterano con menos victorias es {0}.".format(nacionalidadVeterano_Perdedor))

print("Promedio de edad de los pilotos que tiene un vehículo con número par {0}.".format(PromedioEdad))




# *Nacionalidad del piloto más joven.
# *Cantidad de vehículos con número par.
# *Nombre del piloto con menos victorias y el número de auto impar.
# *Cantidad de pilotos mayores de 25 años con número de vehículo impar.
# *Nombre del piloto más joven con más victorias.
# *Nacionalidad del piloto más veterano con menos victorias.
# *Promedio de edad de los pilotos que tiene un vehículo con número par.









