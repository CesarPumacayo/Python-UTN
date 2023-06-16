import pygame
import sys
 
pygame.init()



size= (800,500)
screen= pygame.display.set_mode(size)
clock = pygame.time.Clock()


pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    screen.fill("Black")

    pygame.draw.rect(screen, "Red", (x,y, 100,100))
 
    #60 seran los circulos de la ventana
    pygame.display.flip()
    clock.tick(30) #Creamos puntos aleatorios cada 30 seg
