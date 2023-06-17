from typing import Any
import pygame, sys , random
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

class Meteor(pygame.sprite.Sprite): #(subclase de un sprite)
    def __init__(self): #self(instancia)
        super().__init__()
        self.image= pygame.image.load("Pygame_curso_web\media\pngegg.png").convert()
        self.image = pygame.transform.scale(self.image, (50,80))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y+=1

        if self.rect.y > SCREEN_WIDTH: #si el eje y es mayor a alto de la pantalla..
            self.rect.y= -10
            self.rect.x= random.randrange(SCREEN_WIDTH)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("Pygame_curso_web\media\\nave.png").convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]

class Game(object):
    def __init__(self):
        self.score= 0
        self.meteor_list= pygame.sprite.Group()
        self.all_sprite_list= pygame.sprite.Group()

        for i in range(50):
            meteoro = Meteor()
            meteoro.rect.x= random.randrange(SCREEN_WIDTH)
            meteoro.rect.y= random.randrange(SCREEN_HEIGHT)
            
            self.meteor_list.add(meteoro)
            self.all_sprite_list.add(meteoro)
        self.player = Player()
        self.all_sprite_list.add(self.player)
    

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    def run_logic(self):
        self.all_sprite_list.update()

        meteor_hit_list = pygame.sprite.spritecollide(self.player , self.meteor_list, True) #si es false no elimina meteoros

        for meteoro in meteor_hit_list:
            self.score +=1
            print(self.score)
    def display_frame(self, screen):
        screen.fill("White")
        self.all_sprite_list.draw(screen)
        pygame.display.flip()


class main():
    pygame.init()
    
    screen= pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    done = False
    clock = pygame.time.Clock()


    game = Game()
    while not done: 
        done = game.process_events()

        game.run_logic()

        game.display_frame(screen)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__": #Ejecutar el main
    main()





