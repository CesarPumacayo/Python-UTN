print("*****************************************")
print("¡Bienvenido a la calculadora Inteligente!")
print("*****************************************")



numero=int(input("=================\n"
                 "Menú de opciones:\n"
                 "=================\n"
                 "Elija la opcion que quiere operar...\n"
                 "1.Suma\n"
                 "2.Resta\n"
                 "3.Multiplicacion\n"
                 "4.Division\n"
                 "5.Exponente\n"
                 "6.Modulo o Resto\n"
                 "7.Division Entera\n"
                 "8.Fin.\n"))




if numero == 1:
    
    numero=int(input("Ingrese el primer numero: "))
    numero+=int(input("Ingrese el segundo numero:"))
    
    print("Resultado: " , numero)
elif numero == 2:
    numero=int(input("Ingrese el primer numero: "))
    numero-=int(input("Ingrese el segundo numero:"))

    print("Resultado: " , numero)
elif numero == 3:
    numero=int(input("Ingrese el primer numero: "))
    numero*=int(input("Ingrese el segundo numero:"))
 
    print("Resultado: " , numero)
elif numero == 4:
    numero=int(input("Ingrese el primer numero: "))
    numero/=int(input("Ingrese el segundo numero:"))

    print("Resultado: " ,numero)
elif numero ==5:
    numero=int(input("Ingrese el primer numero: "))
    numero**=int(input("Ingrese el segundo numero:"))

    print("Resultado: " , numero)
elif numero == 6:
    numero=int(input("Ingrese el primer numero: "))
    numero%=int(input("Ingrese el segundo numero:"))
   
    print("Resultado: " , numero)
elif numero == 7:
    numero=int(input("Ingrese el primer numero: "))
    numero//=int(input("Ingrese el segundo numero:"))
    
    print("Resultado: " , numero)
elif numero == 8:
    print("No´re vimo capoooo. ¡SOY LIBREEEE!")
    




