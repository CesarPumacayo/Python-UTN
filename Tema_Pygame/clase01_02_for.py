import pygame , sys


pygame.init()

size = (800,500) #tupla tam ventana

#crear ventana
screen = pygame.display.set_mode(size)

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
 
#bucle infinito

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BLACK)
    "-- ZONA DE DIBUJO --"
    # pygame.draw.line(screen, GREEN , [0,100], [200,300], 5)
    pygame.draw.rect(screen, WHITE, (100,100,80,80))
    # pygame.draw.circle(screen, YELLOW, (300,300), 75)
    for x in range(100, 700, 100):
        pygame.draw.rect(screen, YELLOW, (x, 230, 50, 50 ))
        pygame.draw.line(screen, GREEN, (x,0), (x,100),5)
    
    "-- ZONA DE DIBUJO --"
    # metodo para actualizar pantalla
    pygame.display.flip()