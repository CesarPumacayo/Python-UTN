mensaje= input("Introduce una frase:")

string= input("¿Con que letra deseas terminar el bucle?:")

substring= ""

resultado = ""

indice= mensaje.find(string.lower())

vocales = ["a","e","i","o","u","A","E","I","O","U"]

for i in range(len(mensaje.lower() and mensaje.upper())):
    if mensaje[i] not in vocales:
        resultado = resultado + mensaje[i]


substring = resultado[0:indice]
print(f"{substring}")
