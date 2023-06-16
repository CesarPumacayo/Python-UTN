import pygame

#==================================================================================
def reescalar_imagen(lista_imagenes, tamanio): #escala las imagenes de misma ancho y altura 
    for i in range(len(lista_imagenes)):
        lista_imagenes[i]=  pygame.transform.scale(lista_imagenes[i], tamanio)

def girar_imagenes(lista_original, flip_x , flip_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada


#       ↓  xq al diccionario principal yo tendre q acompañar a un rectangulo, que rect a la derecha arriba abajo o izquida voy a tener
# Define el rectangulo de la der , iz , arriba y abajo
def obtener_rectangulo(principal) -> dict:
    diccionario = {}
    diccionario["main"] = principal                                            #WIDTH        HEIGHT               
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario
#==================================================================================

personaje_quieto = [
                    pygame.image.load("Quieto\\4.png"),
                    pygame.image.load("Quieto\\5.png"),
                    pygame.image.load("Quieto\\6.png"),
                    pygame.image.load("Quieto\\7.png")
                    ]

personaje_camina = [
                    pygame.image.load("Camina\Adelante\\0.png"),
                    pygame.image.load("Camina\Adelante\\1.png"),
                    pygame.image.load("Camina\Adelante\\3.png"),
                    pygame.image.load("Camina\Adelante\\5.png"),

                   ]
personaje_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta =[pygame.image.load("Salta\\0.png")]
