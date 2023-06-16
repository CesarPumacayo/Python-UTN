#César Pumacayo 1°E grupo giovanni

#Ejercicio 8
# Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.

def mostrar_par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(mostrar_par_impar(1))