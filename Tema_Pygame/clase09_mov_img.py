import pygame, sys

pygame.init()

screen = pygame.display.set_mode([850, 750])   
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


background = pygame.image.load("Pygame_curso_web\\media\\akuma.png").convert()
background = pygame.transform.scale(background, (850,750))

player = pygame.image.load("Pygame_curso_web\media\\nave.png").convert()
player = pygame.transform.scale(player, (100,100))
player.set_colorkey((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
    mouse_pos = pygame.mouse.get_pos()

    print(mouse_pos)
    x = mouse_pos[0]
    y = mouse_pos[1]



    screen.blit(background, [0,0])
    screen.blit(player, [x,y])


    clock.tick(60)

    pygame.display.flip()

