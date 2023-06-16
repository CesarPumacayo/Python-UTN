print("Introduce dos números a comparar: \n")


primer=int(input("Introduce el primer número:"))
segundo=int(input("Introduce el segundo número: "))

print("Los números a comparar son: " , primer , " y " , segundo, "\n")

if primer > segundo:
    print("Es mayor...")
    
    if primer >= segundo:
        print("Es mayor o igual...")
        
if primer < segundo:
    print("Es menor...")
    
    if primer <= segundo:
        print("Es menor o igual que...")
        
if primer == segundo:
        print("Es igual que...")

if primer != segundo:
        print("Es diferente...")
print("Fin.")
 
