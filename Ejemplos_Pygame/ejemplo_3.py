import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([1000, 800]) #Se crea una ventana
imagen = pygame.image.load("Tema_Pygame\media\snoopy.png")
imagen = pygame.transform.scale(imagen, (150,150))

font = pygame.font.SysFont("Bauhaus 93", 50)
text = font.render("Hola", True, (50, 50, 50))
# font2= pygame.font.Font(None, 40)
# text2 = font2.render("Hola, Bienvenido a PYGAME!!", True, (100, 100, 100))

rect_imagen= imagen.get_rect()
centerx = 300
centery= 80

running = True

time= 0.5

while running:
    # se verifica si el usuario cerro la ventana

    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_LEFT]:
        centerx -= time
    if pressed_keys[pygame.K_RIGHT]:
        centerx += time
    if pressed_keys[pygame.K_UP]:
        centery -= time
    if pressed_keys[pygame.K_DOWN]:
        centery += time
            
    if event.type == pygame.QUIT:
        running = False
    screen.fill((250, 250, 250)) #se pinta el fondo de la ventana
            
    screen.blit(imagen, (centerx, centery), rect_imagen)
    screen.blit(text, (100,0))




    pygame.draw.circle(screen, (255, 0, 0), (250, 250), 75)
    pygame.display.flip() # muestra los cambios en la pantalla
pygame.quit() #fin