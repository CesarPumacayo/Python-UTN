import pygame
import sys
import random

pygame.init()



size= (800,500)
screen= pygame.display.set_mode(size)
clock = pygame.time.Clock()
coord_list=[]
for i in range(60):
    x= random.randint(0,800)
    y= random.randint(0,500)
    coord_list.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill("Black")

    for coord in coord_list:
        # x= coord[0] solamente ilustra el ejemplo
        # y= coord[1]
        pygame.draw.circle(screen, "Red", coord , 2)
        coord[1] += 1
        if coord[1] > 500:
            coord[1] = 0
 
    #60 seran los circulos de la ventana
    pygame.display.flip()
    clock.tick(30) #Creamos puntos aleatorios cada 30 seg
