#Modulo practico n°6

"""En este ejercicio, solicitamos que el cliente escriba una oracion y despues le solicites que escriba la palabra que desea eliminar"""


hola= "¡Bienvenido señor cliente!"
print(f"{hola}".center(52,"="))




oracion = input("\nIngrese una frase: ")
string= input("\nIngrese la palabra que quiera eliminar: ")

substring= ""

indice= oracion.find(string)

substring = oracion[0:indice] + oracion[indice + len(string) + 1:] 

print(f"\n{substring}.")
