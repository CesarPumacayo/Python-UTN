import pygame
from pygame.locals import *
import sys


pygame.init()



ANCHO = 1200
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO,ALTO))
rectangulo = pygame.Rect(ANCHO/2 , ALTO/2 ,50,50)


esta_corriendo = True
while esta_corriendo:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(pantalla , "Red", rectangulo)
    
    pygame.display.flip()

            
