#Modulo Practico de la compañía multinacional Rappi
print("********************************")
print("\nSistema vacacional del Rappi\n")
print("********************************")
nombre = input("Ingrese el nombre del cliente: ")

clave = int(input("\nIngrese la clave de departamento: \n"
                  "1.Departamento del atencion al cliente \n"
                  "2.Departamento de Logística \n"
                  "3.Departamento de Gerencia \n"))

antiguedad= int(input("Ingrese la antiguedad del trabajador: \n"
                      "Opcion 1: 1 año\n"
                      "Opcion 2: 2 a 6 años \n"
                      "Opcion 3: 7 años \n"))
if antiguedad== 1 and clave == 1:
    print('¡¡' + nombre + ", tus dias de vacaciones son de 6 dias. Gracias por trabajar en atencion al cliente por 1 año!!")

elif antiguedad == 2 and clave == 1:
    print("¡¡" +nombre + ", tus dias de vacaciones son de 14 dias. Gracias por trabajar en atencion al cliente por 2 a 6 años!!")
elif antiguedad == 3 and clave == 1:
    print("¡¡" +nombre + ", tus dias de vacaciones son de 20 dias. Gracias por trabajar en atencion al cliente por 7 años!!")

if clave == 2 and antiguedad == 1:
    print("¡¡" +nombre + ", tus dias de vacaciones son de 7 dias. Gracias por trabajar en Logística por 1 año!!")

elif clave == 2 and antiguedad == 2:
    print("¡¡" +nombre + ", tus dias de vacaciones son de 15 dias. Gracias por trabajar en Logística por 2 a 6 años!!")
elif clave == 2 and antiguedad == 3:
    print("¡¡" +nombre + ", tus dias de vacaciones son de 22 dias. Gracias por trabajar en Logística por 7 años!!")

if clave == 3 and antiguedad == 1:
    print("¡¡" +nombre + ", tus dias de vacaciones son de 10 dias. Gracias por trabajar en nuestra Gerencia por 1 año!!")
elif clave == 3 and antiguedad == 2:
    
    print("¡¡" + nombre + ", tus dias de vacaciones son de 20 dias. Gracias por trabajar en nuestra Gerencia por 2 a 6 años, CAPOOOOO!!")
elif clave == 3 and antiguedad == 3:

    print("¡¡" + nombre + ", tus dias de vacaciones son de 30 dias. Gracias por trabajar en nuestra Gerencia por 7 años, IDOLOOOOOOO!!")

if clave > 3 or antiguedad > 3:
    print("Error, Reingrese mas Tarde")


    

print("Fin.")
