import pygame

pygame.init()

BLANCO = (255,255,255)
NEGRO = (0, 0, 0)


clock = pygame.time.Clock()
ancho = 800
alto = 500

ventana  = pygame.display.set_mode((ancho,alto))

#hacer que no aparezca el mouse en la pantalla
pygame.mouse.set_visible(False)
#jugador 1 (el de la izquierda)
x1 = 20
y1 = (alto/2)-50
speed_y1 = 0

#jugador 2 (el de la derecha)
x2 = ancho - 40
y2 = (alto/2)-50
speed_y2 = 0

#pelota
x3 = ancho/2
y3 = alto/2
speed_x3 = 4
speed_y3 = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #eventos del teclado
        if event.type == pygame.KEYDOWN:
            #movimiento del jugador 1
            if event.key == pygame.K_w:
                speed_y1 = -6
            if event.key == pygame.K_s:
                speed_y1 = 6
            #movimiento del jugador 2
            if event.key == pygame.K_UP:
                speed_y2 = -6
            if event.key == pygame.K_DOWN:
                speed_y2 = 6
        if event.type == pygame.KEYUP:
            #movimiento del jugador 1
            if event.key == pygame.K_w:
                speed_y1 = 0
            if event.key == pygame.K_s:
                speed_y1 = 0
            #movimiento del jugador 2
            if event.key == pygame.K_UP:
                speed_y2 = 0
            if event.key == pygame.K_DOWN:
                speed_y2 = 0



    ventana.fill(NEGRO)
    #--zona dibujo--
    jugador1 = pygame.draw.rect(ventana,BLANCO,(x1,y1,20,100))
    jugador2 = pygame.draw.rect(ventana,BLANCO,(x2,y2,20,100))
    pelota = pygame.draw.circle(ventana,BLANCO,(x3,y3),10)
    #--zona dibujo--

    #--movimiento jugadores--
    y1 += speed_y1
    y2 += speed_y2

    #colision con la pelota y el jugador 1/2
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        speed_x3 *= -1

    

    # movimiento pelota
    x3 += speed_x3
    y3 += speed_y3

    #verificar que los jugadores no puedan moverse afuera de la pantalla
    if y1>alto-100 or y1<0:
        speed_y1 = 0

    if y2>alto-100 or y2<0:
        speed_y2 = 0 
    
       
    #--movimiento jugadores--
    
    #--colisiones--
    if x3>ancho or x3<0:
        x3 = ancho/2
        y3 = alto/2
        speed_x3 *= -1
    if y3>alto or y3<0:
        speed_y3 *= -1
    #--colisiones--

    pygame.display.update()
    clock.tick(60)