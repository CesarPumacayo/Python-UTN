import pygame , sys, random

pygame.init()


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame_curso_web\media\pngegg.png")
        self.image = pygame.transform.scale(self.image, (50,80))
        self.rect = self.image.get_rect()

    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame_curso_web\media\\nave.png")
        self.image= pygame.transform.scale(self.image, [70,100]) #ancho, altura
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]# donde se posiciona el jugador
        player.rect.y = 510 # se quede abajo de la pantalla el jug


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame_curso_web\media\laser.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5 #que vaya arriba (negativo)




screen = pygame.display.set_mode([900,600])
clock = pygame.time.Clock()
score = 0


all_sprite_list= pygame.sprite.Group() #agrupa el player y meteoros con la ventana
meteor_list = pygame.sprite.Group() #agrupa meteoros for
laser_list= pygame.sprite.Group() #agrupa laseres


for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(880) #ancho 
    meteor.rect.y = random.randrange(450) #altura

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        "Dentro del FOR"
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = player.rect.x + 31 # que el laser este en el centro de la imagen superior
            laser.rect.y = player.rect.y - 30 # salga mas arriba
            all_sprite_list.add(laser)
            laser_list.add(laser)

    all_sprite_list.update() #tiene q quedar arriba de la ventana q pintamos
    screen.fill("Black")
    
    "ZONA DE DIBUJO"
    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score+=1
            print(score)
        if laser.rect.y < -10:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)

    all_sprite_list.draw(screen)
    clock.tick(60)
    pygame.display.flip()
