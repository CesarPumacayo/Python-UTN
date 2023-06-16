#Características
#cant_pasajero
#velocidad
#km_totales
#distancia_recorrida

#Comportamiento


class Transporte:
    def __init__(self, cantidad: int, velocidad: float): #no poner retorno
        self.cantidad_pasajeros = cantidad #publico
        self.velocidad = velocidad #privado   si es.. self__.velocidad = velocidad 
        self.km_totales = 0 #protegido
        self.distancia_recorrida = 0
    
    def frenar(self):
        print("Esta frenando....")
    def avanzar(self):
        print("Esta avanzando....")

    def mostrar(self):
        print(f"----------------{type(self)}-------------------")
        print(f"Cantidad: {self.cantidad_pasajeros} - Velocidad: {self.velocidad} - Destino: {self.km_totales}")
