import pygame
import sys
 
pygame.init()



size= (800,500)
screen= pygame.display.set_mode(size)
clock = pygame.time.Clock()


pygame.mouse.set_visible(0)


"Coordenadas del cuadrado"
coord_x= 10
coord_y= 10



x_speed=0
y_speed=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        # Eventos teclado


        "Cuando presionas una vez o mantengo presionado"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            
            if event.key == pygame.K_RIGHT:
                x_speed= 3

            if event.key == pygame.K_UP:
                y_speed = -3
            
            if event.key == pygame.K_DOWN:
                y_speed= 3
        "se dispara cuando se suelta una tecla que ha sido presionada previamente"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0

            if event.key == pygame.K_UP:
                y_speed = 0
            
            if event.key == pygame.K_DOWN:
                y_speed= 0
                
    screen.fill("Black")

    coord_x += x_speed
    coord_y += y_speed



    pygame.draw.rect(screen, "Red", (coord_x,coord_y, 100,100))
 
    #60 seran los circulos de la ventana
    pygame.display.flip()
    clock.tick(30) #Creamos puntos aleatorios cada 30 seg
