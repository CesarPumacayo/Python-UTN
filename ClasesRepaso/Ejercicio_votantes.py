#Es la gala final de Gran Hermano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que ganará el juego.
#Los participantes finalistas son: Nacho, Julieta y Marcos.
#El televidente debe ingresar:
#● Nombre del votante
#● Edad del votante (debe ser mayor a 13)
#● Género del votante (masculino, femenino, otro)
#● El nombre del participante a quien le dará el voto positivo.
#No se sabe cuántos votos entrarán durante la gala.
#Se debe informar al usuario:
#A. El promedio de edad de las votantes de género femenino
#B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.
#C. Nombre del votante más joven que votó a Nacho.
#D. Nombre de cada participante y porcentaje de los votos qué recibió.
#E. El nombre del participante que ganó el reality (El que tiene más votos)




promedioEdad=0
acumuladorEdad= 0
contador= 0

contadorM25y40deNyJ= 0

masJoven=0
nombreJovenNacho=0
bandera=0

porcentajeNacho=0
porcentajeJulieta=0
porcentajeMarcos= 0

acumuladorNacho= 0
acumuladorJulieta=0
acumuladorMarcos=0

nombreGanador=""




while contador < 3:
    nombre= input("Ingrese el nombre del votante: ")
    edad= int(input("Ingrese la edad del votante: "))
    while edad < 13:
        print("ERROR, al ingresar edad")
        edad= int(input("Ingrese la edad del votante: "))
        
    genero= input("Ingrese el genero (m , f , otro): ")
    while genero.lower() not in ["m", "f", "otro"]:
        print("Error, al ingresar")
        genero= input("Ingrese el genero (m , f , otro): ")


    voto= input("Ingrese el participante Nacho , Julieta y Marcos : ")
    while voto.lower() not in ["nacho", "julieta", "marcos"]:
        print("ERROR, al ingresar participante")
        voto= input("Ingrese el participante Nacho , Julieta y Marcos : ")
    
    if genero == "f":
        acumuladorEdad+= edad
    elif genero == "m" and edad >= 25 and edad <= 40 and voto == "nacho" or voto == "julieta":
        contadorM25y40deNyJ+=1
    if voto == "nacho":
        if edad < masJoven or bandera ==0:
            masJoven= edad
            nombreJovenNacho= nombre
            bandera= 1
    

    if voto== "nacho":
        acumuladorNacho+=1
    elif voto == "julieta":
        acumuladorJulieta+= 1
    else:
        acumuladorMarcos+= 1

    contador+=1


porcentajeJulieta= (acumuladorJulieta *100) /contador
porcentajeMarcos= (acumuladorMarcos *100) /contador
porcentajeNacho= (acumuladorNacho *100) / contador

if porcentajeJulieta > porcentajeNacho and porcentajeJulieta > porcentajeMarcos:
    nombreGanador= "Julieta"
elif porcentajeNacho > porcentajeMarcos and porcentajeNacho > porcentajeJulieta:
    nombreGanador= "Nacho"
elif porcentajeMarcos > porcentajeNacho and porcentajeMarcos > porcentajeJulieta:
    nombreGanador= "Marcos"
elif porcentajeNacho == porcentajeJulieta and porcentajeJulieta == porcentajeMarcos and porcentajeMarcos == porcentajeNacho:
    nombreGanador= "Tienen los mismos resultados"

promedioEdad= acumuladorEdad // contador

print("El promedio de edad de las votantes de género femenino es {0}".format(promedioEdad))
print("Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta son {0}".format(contadorM25y40deNyJ))
print("Nombre del votante más joven que votó a Nacho es {0}.".format(nombreJovenNacho))
print("Porcentaje de Nacho: {0}".format(porcentajeNacho))
print("Porcentaje de Julieta: {0}".format(porcentajeJulieta))
print("Porcentaje de Marcos: {0}".format(porcentajeMarcos))
print("El nombre del participante que ganó el reality (El que tiene más votos) : {0}".format(nombreGanador))



#A. El promedio de edad de las votantes de género femenino
#B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.
#C. Nombre del votante más joven que votó a Nacho.
#D. Nombre de cada participante y porcentaje de los votos qué recibió.
#E. El nombre del participante que ganó el reality (El que tiene más votos)




