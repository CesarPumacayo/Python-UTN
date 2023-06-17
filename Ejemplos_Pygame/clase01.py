import pygame

pygame.init() # se inializa pygame
screen = pygame.display.set_mode([500, 500]) #Se crea una ventana
running = True
while running:
    # se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0)) #se pinta el fondo de la ventana
    #se dibuja un circulo azul en el centro
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip() # muestra los cambios en la pantalla
pygame.quit() #fin


