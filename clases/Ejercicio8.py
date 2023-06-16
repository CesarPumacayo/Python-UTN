numero= int(input("¿Qué tabla de multiplicar quieres ver?: "))
resultado =0
print(f"La tabla del {numero} es: ")
for multiplicar in range(0,11):
    resultado= multiplicar * numero
    print(f"{numero} * {multiplicar} =", resultado)
          

