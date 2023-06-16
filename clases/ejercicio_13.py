filas = int(input("¿Cuántas filas tendrá la matriz?:"))

columnas= int(input("¿Cúantas columnas tendrá la matriz?:"))

elemento=[]


for acumulador in range(filas):
    
    filas= []
    
    for element in range(columnas):
        
        filas.append(int(input(f"Introduce  un elemento a la fila {acumulador}:")))
    elemento.append(filas)

for row in elemento:
    print(row)


 
