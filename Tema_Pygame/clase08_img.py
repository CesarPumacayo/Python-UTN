import pygame, sys

pygame.init()

screen = pygame.display.set_mode([850, 750])   
clock = pygame.time.Clock()

background = pygame.image.load("Pygame_curso_web\\media\\akuma.png").convert()
background = pygame.transform.scale(background, (850,750))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()

    screen.blit(background, [0,0])

    clock.tick(60)

    pygame.display.flip()

