#César Pumacayo 1°E grupo giovanni

#Ejercicio 7
# Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.
def calcular_maximo_divisor(numero_uno, numero_dos):
    
    while numero_dos != 0:
        maximo_comun= numero_uno % numero_dos
        numero_uno = numero_dos
        numero_dos = maximo_comun
    return numero_uno
        
print(calcular_maximo_divisor(8,6))
