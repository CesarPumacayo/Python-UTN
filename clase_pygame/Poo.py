import pygame
from pygame.locals import *
import sys


class Paleta:
    def __init__(self, posicion, tamanio, velocidad, color) ->None:
        self.surface = pygame.surface(tamanio)
        self.surface.fill(color)
        self.rectangulo = self.surface.get.rect()

        self.rectangulo.center = posicion
        self.velicidad = velocidad

    def mover_y(self, alto_pantalla):
        if self.rectangulo.top > ALTO:
            self.rectangulo.bottom = 0
        elif self.rectangulo.bottom < 0:
            self.rectangulo.top = alto_pantalla
    
    def verificar_colision(self, otra_paleta):
        if self.rectangunlo.collide_rect(otra_paleta.rectangulo):
            self.surface.fill("Green")
            otra_paleta.surface.fill("Yellow")

    def draw(self, pantalla):
        pantalla.blit(self.surface, self.rectangulo)
    
    def update(self, pantalla):
        self.mover_y(pantalla.get.height())
        self.draw(pantalla)
    




pygame.init()

RELOJ = pygame.time.Clock()
FPS = 60
ANCHO = 1200
ALTO = 600


pantalla = pygame.display.set_mode((ANCHO,ALTO))
rectangulo = pygame.Rect(ANCHO/2 , ALTO/2 ,50,50)
otro_rectangulo = pygame.Rect(ANCHO/2 , 500  ,50,50)


superficie_rectangulo = pygame.Surface((50,50))
superficie_rectangulo.fill("Red")
rectangulo = superficie_rectangulo.get_rect()
rectangulo.center= (ANCHO/2 , ALTO/2) 


superficie_otro_rectangulo = pygame.Surface((50,50))
superficie_otro_rectangulo.fill("Blue")
otro_rectangulo = superficie_otro_rectangulo.get_rect()
otro_rectangulo.center= (ANCHO/2 , 500) 

paleta_uno = Paleta(((ANCHO/2 , ALTO/2)), (50,50), 5, "Red")
paleta_dos = Paleta(((ANCHO/2 , 500)), (50,50), 5, "Blue")


def mover_rectangulo(rectangulo: pygame.Rect, velocidad_y, alto_pantalla):
    rectangulo.y+= velocidad_y
    if rectangulo.top > ALTO:
        rectangulo.bottom = 0
    elif rectangulo.bottom < 0:
        rectangulo.top = alto_pantalla

def verificar_colision(rectangulo: pygame.Rect, superficie_rectangulo , otro_rectangulo, superficie_otro_rectangulo):
    if rectangulo.colliderect(otro_rectangulo):
        superficie_rectangulo.fill("Green")
        superficie_otro_rectangulo.fill("Yellow")
    else:
        superficie_rectangulo.fill("Red")
        superficie_otro_rectangulo.fill("Blue")



esta_corriendo = True
while esta_corriendo:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    paleta_uno.update(pantalla)
    paleta_dos.update(pantalla)
    


    pantalla.fill("Black")
    pygame.draw.rect(pantalla , "Red", rectangulo)
    pygame.draw.rect(pantalla , "Blue", otro_rectangulo)

    mover_rectangulo(rectangulo, 5, pantalla)
    mover_rectangulo(otro_rectangulo, -5, ALTO)
    verificar_colision(rectangulo, superficie_otro_rectangulo,superficie_rectangulo,otro_rectangulo)

    pantalla.blit(superficie_rectangulo, rectangulo)
    pantalla.blit(superficie_otro_rectangulo, otro_rectangulo)


    pygame.display.flip()

            
