from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, cambios , rodado, cantidad, velocidad):
        super().__init__(cantidad , velocidad) #constructor llamando base
        self.cambios = cambios
        self.rodado = rodado
    

    def frenar(self):
        print(f"La bicicleta rodado: {self.rodado}")
        super().frenar()


    def avanzar(self):
        print(f"La bicicleta rodado: {self.rodado}")
        super().avanzar()



    def mostrar(self):
        super().mostrar()
        print(f"Rodado: {self.rodado} --  Marca: {self.cambios}")


