import pygame
y = 385
x = 470
lives = 3
speed = 0.3

def presionar_tecla(tecla):
    global up, down, left, right, y, x, lives
    up = False
    down = False
    left = False
    right = False
    match tecla:
        case "r":
            y = 385
            x = 470
            lives = 3
        case "w":
           up = True
        case "a":
            left = True
        case "d":
            right = True
        case "s":
            down = True
    
     
pygame.init()
screen = pygame.display.set_mode([600,500])
running = True
up = False
down = False
left = False
right = False
while running:
    linea_ganadora = pygame.draw.line(screen, (255,255,255), (100,70),(160,70),5)
    screen.fill((0, 0, 0))
    circle = pygame.draw.circle(screen,(0,255,0),(x,y),20)

    left_line = pygame.draw.line(screen,(255,0,0),(100,70),(100,420),5)
    down_line = pygame.draw.line(screen,(255,0,0),(100,420),(500,420),5)
    right_line = pygame.draw.line(screen,(255,0,0),(500,420),(500,70),5)
    up_line = pygame.draw.line(screen,(255,0,0),(500,70),(160,70),5)

    center_line_1 = pygame.draw.line(screen,(255,0,0),(500,350),(170,350),5)

    center_line_2 = pygame.draw.line(screen,(255,0,0),(100,280),(150,280),5)
    center_line_3 = pygame.draw.line(screen,(255,0,0),(220,280),(500,280),5)

    center_line_4 = pygame.draw.line(screen,(255,0,0),(100,210),(350,210),5)
    center_line_5 = pygame.draw.line(screen,(255,0,0),(420,210),(500,210),5)

    center_liner_6 = pygame.draw.line(screen,(255,0,0),(100,140),(250,140),5)
    center_line_7 = pygame.draw.line(screen,(255,0,0), (320,140), (500,140),5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            presionar_tecla ("space")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            presionar_tecla("a")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            presionar_tecla("s")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            presionar_tecla("w")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            presionar_tecla("d")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and lives < 1 or event.type == pygame.KEYDOWN and event.key == pygame.K_r and circle.colliderect(linea_ganadora):
            presionar_tecla("r")
    if up:
        y -= speed
    elif down:
        y += speed
    elif right:
        x += speed
    elif left:
        x-= speed
    font = pygame.font.SysFont("Arial Narrow", 50)
    text_lives = font.render("lives: {0}".format(lives), True, (255,0,0))
    screen.blit(text_lives,(0,0))
    text = font.render("Your lose", True, (255, 0, 0))
    text_2 = font.render("Press R for restart", True, (255, 0, 0))
    winner_text = font.render("Congrats,your win", True,(255, 0, 0,))
    winner_text_2 = font.render("Bien ahi bichito de luz", True,(255, 0, 0,))
    if circle.colliderect(left_line) or circle.colliderect(right_line) or circle.colliderect(up_line) or circle.colliderect(down_line) or circle.colliderect(center_line_5) or circle.colliderect(center_liner_6) or circle.colliderect(center_line_1) or circle.colliderect(center_line_2) or circle.colliderect(center_line_3) or circle.colliderect(center_line_4) or circle.colliderect(center_line_5) or circle.colliderect(center_liner_6) or circle.colliderect(center_line_7):
        presionar_tecla("space")
        lives -= 1
        x = 470
        y = 385
    elif circle.colliderect(linea_ganadora):
        presionar_tecla("space")
        screen.fill((50, 50, 50))
        screen.blit(winner_text,(150,200))
        screen.blit(winner_text_2,(120,250))
    if lives < 1:
        presionar_tecla("space")
        screen.fill((0, 0, 0))
        screen.blit(text,(220,200))
        screen.blit(text_2,(150,250))

    pygame.display.flip()

pygame.quit()
