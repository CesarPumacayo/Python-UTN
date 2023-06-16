import pygame , sys


pygame.init()

"            Definicion de colores                "
# La pequeña tabla de los colores:
BLACK					=			(  0,   0,   0)
# DARK_BLUE				=			(  0,   0, 100)
BLUE					=			(  0,   0, 255)
# DARK_GREEN			=			(  0, 100,   0)
# GREENISH_BLUE			=			(  0, 100, 100)
# LIGHT_TURQUOISE		=			(  0, 100, 255)
GREEN					=			(  0, 255,   0)
# WATERY_GREEN			=			(  0, 255, 100)
# CYAN					=			(  0, 255, 255)

RED						=			(255,   0,   0)
# DARK_PINK				=			(255,   0, 100)
# PINK					=			(255,   0, 255)
# ORANGE				=			(255, 100,   0)
# RED_PINK				=			(255, 100, 100)
# MAGENT				=			(255, 100, 255)
YELLOW				    =			(255, 255,   0)
# LIGHT_YELLOW			=			(255, 255, 100)
WHITE					=			(255, 255, 255)

# REDDISH_BROWN		    =			(100,   0,   0)
# PURPLE				=			(100,   0, 100)
# MUSTARD				=			(100,   0, 255)
# GREENISH_BROWN		=			(100, 100,   0)
# GREY					=			(100, 100, 100)
# TURQUOISE				=			(100, 100, 255)

size = (800,500) #tupla tam ventana


# Coordenadas del cuadrado
cord_x= 400
cord_y= 200


# Velocidad a la que se movera mi cuadrado
speed_x = 3
speed_y = 3
 
# Crear ventana
screen = pygame.display.set_mode(size)
#Controlar FPS
clock = pygame.time.Clock()

 
#bucle infinito

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    "------LOGICA-----"
    if cord_x > 720 or cord_x < 0:
        speed_x *= -1
    if cord_y > 420 or cord_y < 0:
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y
    "------LOGICA------"

    screen.fill(BLACK)

    "-- ZONA DE DIBUJO --"         #400     240
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80 ,80))
    "-- ZONA DE DIBUJO --"
    
    # metodo para actualizar pantalla
    pygame.display.flip()
    clock.tick(60)