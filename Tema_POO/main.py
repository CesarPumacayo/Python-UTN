from bicicleta import Bicicleta
from Auto import Auto
from Transporte import Transporte


"Atributos:  cant.ruedas|marca|pasajero| km"
mi_auto = Auto(4, "Ford", 5 , 170)

mi_bicicleta= Bicicleta(16,24,1,50)

otro_auto= Auto(5, "Fiat", 8, 200)

otra_bicicleta= Bicicleta(8,12,2,25)

lista_transporte=[mi_auto , mi_bicicleta , otro_auto , otra_bicicleta]

for t in lista_transporte: #t(transporte)
    #POLIMORFISMO ¿Cómo sabe? Como todo son del tranporte(padre) todos ellos lo heredan y el uso de métodos con el mismo nombre en diferentes clases y tengan un método llamado mostrar().
    t.mostrar() 

# Examples: 

# mi_bicicleta.avanzar()
# mi_bicicleta.frenar()
# mi_bicicleta.mostrar()


# mi_auto.mostrar()
# mi_auto.frenar()
# mi_auto.avanzar()


# mi_transporte = Transporte(2, 50)
# print(mi_transporte.km_totales)


# mi_transporte.mostrar()
# mi_transporte.avanzar()
# mi_transporte.frenar()