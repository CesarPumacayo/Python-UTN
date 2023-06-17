import pygame
from pygame.locals import *
import sys


pygame.init()

RELOJ = pygame.time.Clock()
FPS = 60

ANCHO = 1200
ALTO = 600

def mover_rectangulo(rectangulo: pygame.Rect, velocidad_y, alto_pantalla):
    rectangulo.y+= velocidad_y
    if rectangulo.top > ALTO:
        rectangulo.bottom = 0
    elif rectangulo.bottom < 0:
        rectangulo.top = alto_pantalla

def verificar_colision(rectangulo: pygame.Rect, otro_rectangulo):
    if rectangulo.colliderect(otro_rectangulo):
        print("Colisionaron") #imprime cada seg que colisiona y sigue colisionando los rectangulos



pantalla = pygame.display.set_mode((ANCHO,ALTO))
rectangulo = pygame.Rect(ANCHO/2 , ALTO/2 ,50,50)
otro_rectangulo = pygame.Rect(ANCHO/2 , 500  ,50,50)




esta_corriendo = True
while esta_corriendo:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    pantalla.fill("Black")
    pygame.draw.rect(pantalla , "Red", rectangulo)
    pygame.draw.rect(pantalla , "Blue", otro_rectangulo)

    mover_rectangulo(rectangulo, 5, pantalla)
    mover_rectangulo(otro_rectangulo, -5, ALTO)

    verificar_colision(rectangulo, otro_rectangulo)



    
    pygame.display.flip()

            
