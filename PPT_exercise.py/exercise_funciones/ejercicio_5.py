#César Pumacayo 1°E grupo giovanni

#Ejercicio 5
# Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.

def es_primo(numero):
    '''
    Mostrar si es primo o no
    Recibe numero
    Retorna True o False

    '''
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


print(es_primo(2))
    
    