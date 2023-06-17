print("Hola mundo") #esto es un comentario

numero = 1
numero = "1"

numero_uno= 5 #numeroUno
numero_dos = 5

edad = 10

print(id(numero_uno))
print(id(numero_dos))
print(hex(id(numero_uno)))

if edad > 18:  #el parentesis es innecesario
    print("Usted es mayor de edad")
elif edad > 12:
    print("es un adolescente")
else:
    print("es un niño")

    print("Esto se ejecuta si es falso")

while edad < 18:
    print("Esto se va ejecutar eternamente")

for i in range(5):
    print(i)

print("Estoy fuera del if")
