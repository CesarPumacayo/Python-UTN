
longitud= int(input("¿Cúantos números enteros contendrá la lista?:"))
numeros= []

for acumulador in range(longitud):
    numeros.append(int(input("introduce un número entero:")))
print(f"Lista:{numeros}\nLa suma de los numeros es: {sum(numeros)}")

    
    
