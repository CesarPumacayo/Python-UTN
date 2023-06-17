import pygame
from pygame.locals import *
import sys

pygame.init()

RELOJ = pygame.time.Clock()
FPS = 60
ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))

superficie_rectangulo = pygame.Surface((50, 50))
superficie_rectangulo.fill("Red")
rectangulo = superficie_rectangulo.get_rect()
rectangulo.center = (ANCHO/2, ALTO/2)

superficie_otro_rectangulo = pygame.Surface((50, 50))
superficie_otro_rectangulo.fill("Blue")
otro_rectangulo = superficie_otro_rectangulo.get_rect()
otro_rectangulo.center = (ANCHO/2, 500)


def mover_rectangulo(rectangulo, velocidad_y, alto_pantalla):
    rectangulo.y += velocidad_y
    if rectangulo.top > alto_pantalla:
        rectangulo.bottom = 0
    elif rectangulo.bottom < 0:
        rectangulo.top = alto_pantalla

def verificar_colision(rectangulo : pygame.Rect, otro_rectangulo, superficie_rectangulo, superficie_otro_rectangulo):
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

    pantalla.fill("Black")
    pygame.draw.rect(pantalla, "Red", rectangulo)
    pygame.draw.rect(pantalla, "Blue", otro_rectangulo)

    mover_rectangulo(rectangulo, 5, ALTO)
    mover_rectangulo(otro_rectangulo, -5, ALTO)
    verificar_colision(rectangulo, otro_rectangulo, superficie_rectangulo, superficie_otro_rectangulo)

    pantalla.blit(superficie_rectangulo, rectangulo)
    pantalla.blit(superficie_otro_rectangulo, otro_rectangulo)

    pygame.display.flip()
