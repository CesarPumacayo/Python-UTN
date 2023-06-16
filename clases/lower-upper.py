variable= "La Geekipedia"
print(variable.islower())
variable = variable.lower()
print(variable)
print(variable.isupper())
print(variable.upper())
print(variable)


#Ejemplo

string= input("Introduce un string:")

print(f"\n ¿Todas las letras están en minúscula?: {string.islower()}")
string= string.lower()
print(f"String en minuscula: {string}")


print(f"\n¿Todas la letras están en mayúsculas?: {string.isupper()}")
print(f"String en mayúsculas: {string.upper()}")
print(f"String original: {string}")
