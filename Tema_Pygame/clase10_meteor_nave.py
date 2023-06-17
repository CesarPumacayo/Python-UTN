import pygame, sys , random
pygame.init()

class Meteor(pygame.sprite.Sprite): #(subclase de un sprite)
    def __init__(self): #self(instancia)
        super().__init__()
        self.image= pygame.image.load("Pygame_curso_web\media\pngegg.png").convert()
        self.image = pygame.transform.scale(self.image, (50,80))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("Pygame_curso_web\media\\nave.png").convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

score = 0
screen = pygame.display.set_mode([850, 750])   
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)



meteor_list = pygame.sprite.Group() #lista de grupos de los 50 meteor
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    meteoro = Meteor()
    meteoro.rect.x= random.randrange(850)
    meteoro.rect.y= random.randrange(750)
    
    meteor_list.add(meteoro)
    all_sprite_list.add(meteoro)

player = Player()
all_sprite_list.add(player)

background = pygame.image.load("Pygame_curso_web\\media\\akuma.png").convert()
background = pygame.transform.scale(background, (850,750))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]


    meteor_hit_list = pygame.sprite.spritecollide(player , meteor_list, True) #si es false no elimina meteoros

    for meteor in meteor_hit_list:
        score+= 1
        print(score)

    screen.blit(background, [0,0])
    all_sprite_list.draw(screen) # imprime todos los meteoros



    
    clock.tick(60)

    pygame.display.flip()

