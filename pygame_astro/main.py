from configuraciones import *
import pygame , sys
from pygame.locals import * 
from class_personaje import Personaje
from modo import *

# ----------------------------------------------------
#TAREA ACTUALIZAR ESTO PARA PLATAFORMA UNA LISTA DE PLATAFORMA DE CADA LADO
def actualizar_pantalla(pantalla, un_personaje: Personaje, fondo, lados_piso):
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(plataforma,(rectangulo_plataforma.x,rectangulo_plataforma.y))

    #No traspasar fondo------------------
    # Asegurar que el rectángulo principal y sus lados del personaje estén dentro de los límites del fondo
    # if not fondo.get_rect().contains(un_personaje.lados["main"]):
    #     un_personaje.lados["main"].clamp_ip(fondo.get_rect())

    # for lado in un_personaje.lados:
    #     if not fondo.get_rect().contains(un_personaje.lados[lado]):
    #         un_personaje.lados[lado].clamp_ip(fondo.get_rect())
    #-------------------------------------
    # Blitear el personaje en la pantalla
    un_personaje.update(pantalla, lados_piso)


# ----------------------------------------------------

#PANTALLA
W, H = 1900, 900
TAMANIO= (W, H) #disociado para despues usar w y h en otras funciones
FPS=30 #18
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO)

fondo  = pygame.image.load("juego\\fondo_space.png")
fondo = pygame.transform.scale(fondo, TAMANIO)

pygame.init()

#PERSONAJE    (piso exact)  x      y
posicion_inicial = (H//2 - 300 , 650) 
tamanio =(75,85) #TAM personaje

diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_izquierda

#funcion de blitear (actualizar al personaje)
mi_personaje = Personaje(tamanio, diccionario_animaciones, posicion_inicial, velocidad=10) #10



#PISO debe tener su lados del rectangulo
piso = pygame.Rect(0,0, W, 20) #se veria el rectangulo arriba
piso.top = mi_personaje.lados["main"].bottom #se pondria debajo del personaje
lados_piso = obtener_rectangulo(piso) #el piso obtiene todos rect en sus lados

#Plataforma
plataforma = pygame.image.load("juego\plataforma.png")
plataforma= pygame.transform.scale(plataforma, (400 , 75))
rectangulo_plataforma = plataforma.get_rect() 
rectangulo_plataforma.x = 500
rectangulo_plataforma.y = 620

# lista_plataformas = [piso , rectangulo_plataforma]

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB: #un evento capsula varias cosas
                cambiar_modo()
             

    keys = pygame.key.get_pressed()                                     #↓(sin esto se restaria 2 pixeles)
    if keys[pygame.K_RIGHT] and mi_personaje.lados["main"].x < W - mi_personaje.velocidad - mi_personaje.ancho:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT] and mi_personaje.lados["main"].x > 0 + mi_personaje.velocidad:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    else:
        mi_personaje.que_hace = "quieto"
    
    #-----------------NO TRANSPASE EL FONDO------------------------
    # if not fondo.get_rect().contains(mi_personaje.lados["main"]):
    #     mi_personaje.lados["main"].clamp_ip(fondo.get_rect())

    # for lado in mi_personaje.lados:
    #     if not fondo.get_rect().contains(mi_personaje.lados[lado]):
    #         mi_personaje.lados[lado].clamp_ip(fondo.get_rect())
    #----------------------------------
    actualizar_pantalla(PANTALLA, mi_personaje, fondo , lados_piso)

    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, "Blue", lados_piso[lado], 2)

        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, "Orange", mi_personaje.lados[lado], 2)
            


    pygame.display.update()

    