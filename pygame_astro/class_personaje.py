from configuraciones import reescalar_imagen, obtener_rectangulo


class Personaje: 
    #(altura del personaje)▼       ▼(diccionario)
    def __init__(self, tamanio, animaciones, posicion_inicial, velocidad): #tamaño tupla, posicion_inicial(x,y)
        #CONFECCION
        self.ancho = tamanio[0] #tupla TAMANIO indice W
        self.alto = tamanio[1] #indice H

        #GRAVEDAD
        self.gravedad = 1 # como va caer(gravedad) , 'mientras mas grande mas rapido va caer..'
        self.potencia_salto = -15   #VELOCIDAD SALTO ,PARA SUBIR(DECREMENTA)
        self.limite_velocidad_caida = 15 # LIMITE VELOCIDAD DE CAER
        self.esta_saltando=  False # ESTADO DE CAIDA, EN CASO DE ESTAR SUSPENDIDO EN UNA PLATAFORMA O NO SALTAR SINO BAJAR DE LA PLATAFORMA 

        #ANIMACIONES
        self.contador_pasos = 0 #ARRANCA QUIETO self hace referencia al personaje actual
        self.que_hace = "quieto"
        self.animaciones = animaciones #En una lista, estan tamanio chiquitas(hay q escalarlo)
        self.reescalar_animaciones()
        
        #RECTANGULOS (si tengo superficie creada me lo robo para el RECTANGULO, exponiendo este metodo 'get_rect' )
        rectangulo = self.animaciones["camina_derecha"][0].get_rect() #self.animacion[][] es una lista y img = superficie --> rectangulo principal para todas las img
        rectangulo.x = posicion_inicial[0] #ancho del personaje
        rectangulo.y = posicion_inicial[1] #altura del personaje
        self.lados = obtener_rectangulo(rectangulo) #asi rectangulo se vuelve principal

        #MOVIMIENTO
        self.velocidad = velocidad # vel mover
        self.desplazamiento_y = 0 #donde caigo, velocidad con lo que va subir



    #quieto - salta - camina_derecha - camina izquierda (claves)
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            #▼ set de imagenes que quiero reescalar dentro del dict[Clave]
            reescalar_imagen(self.animaciones[clave], (self.ancho , self.alto))
                #        ▼(BLIT)    ▼(clave del dict que ejecut al moment)
    def animar(self, pantalla, que_animacion:str): #animar generico que se adapte a ese momento
        animacion = self.animaciones[que_animacion]
        largo = len(animacion) 
        if self.contador_pasos >= largo:
            self.contador_pasos = 0 #repetir el ciclo caminar al terminar etc
                                #     ▼(pasa las img c/u) ▼(el rectangulo principal) 
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
        
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad #moves los rectangulos y sus claves

    
    def update(self, pantalla, piso):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:  # ▼(que_animacion)
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad) 
            case "izquierda":
                if not self.esta_saltando: #hace q no se buguee el personaje
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad * -1) #convertirlo negativo para q vaya atras 
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    #empieze en -15 y vaya aumentando la gravedad (ej: -14 -13 -12 -11 -10 ... mientras ese decremento sea menor a la velocidad de caida)
                    self.desplazamiento_y= self.potencia_salto 
                
                
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")

        self.aplicar_gravedad(pantalla, piso)

                        
    def aplicar_gravedad(self, pantalla, piso):
        #SALTO ----"APLICACION DE LA GRAVEDAD" , animar en 'y' mover en 'y' 
        if self.esta_saltando:
            self.animar(pantalla, "salta")

            for lado in self.lados: # MECANICA QUE SALTE | mover todos los rectangulos (self.lados= diccionario)
                self.lados[lado].y += self.desplazamiento_y # sube rectangulos, es como el def mover()
        
        #CAIDA------¿Puedo seguir cayendo? MECANICA DE CAIDA
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida: 
                self.desplazamiento_y += self.gravedad #esta cayendo  1  pixel de gravedad hasta limite_inferior (piso)  / CUANDO LLEGUE AL LIMITE  DECAE
        
        if self.lados["bottom"].colliderect(piso["top"]): # si los lados del rect del jugador colisiona con el top del piso...
            self.desplazamiento_y = 0 #ya cayo
            self.esta_saltando = False #no esta saltando
            self.lados["main"].bottom = piso["main"].top #posicionar al personaje al bottom (personaje) y top(piso) | bottom del rect prinipal

        