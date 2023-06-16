import pygame
import random

# Dimensiones de la ventana del juego
WIDTH = 800
HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tamaño del jugador
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 80

# Tamaño de la bala
BULLET_WIDTH = 10
BULLET_HEIGHT = 20

# Velocidad del jugador
PLAYER_SPEED = 8

# Velocidad de la bala
BULLET_SPEED = 10

# Velocidad del enemigo
ENEMY_SPEED = 5

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Clase para representar al jugador
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = BLUE
        self.speed = PLAYER_SPEED
        self.lives = 3

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Limitar el movimiento del jugador dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Clase para representar a las balas
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_WIDTH, BULLET_HEIGHT)
        self.color = RED
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Clase para representar a los enemigos
class Enemy:
    def __init__(self, x):
        self.rect = pygame.Rect(x, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = RED
        self.speed = ENEMY_SPEED

    def update(self):
        self.rect.x -= self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Listas para almacenar a las balas y enemigos
bullets = []
enemies = []

# Crear al jugador
player = Player()

# Bucle principal del juego
running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Disparar una bala cuando se presiona la tecla de espacio
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.y)
            bullets.append(bullet)

    screen.fill(BLACK)

    player.update(keys)
    player.draw()

    # Actualizar y dibujar las balas
    for bullet in bullets:
        bullet.update()
        bullet.draw()

        # Eliminar las balas que salen de la pantalla
        if bullet.rect.right > WIDTH:
            bullets.remove(bullet)

    # Generar nuevos enemigos
    if random.randint(0, 100) < 2:
        enemy = Enemy(WIDTH)
        enemies.append(enemy)

    # Actualizar y dibujar a los enemigos
    for enemy in enemies:
        enemy.update()
        enemy.draw()

        # Comprobar colisiones entre las balas y los enemigos
        for bullet in bullets:
            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

        # Comprobar colisiones entre el jugador y los enemigos
        if player.rect.colliderect(enemy.rect):
            player.lives -= 1
            enemies.remove(enemy)

        # Eliminar los enemigos que salen de la pantalla
        if enemy.rect.right < 0:
            enemies.remove(enemy)

    # Comprobar si el jugador ha perdido todas las vidas
    if player.lives <= 0:
        running = False

    # Dibujar el contador de vidas
    font = pygame.font.Font(None, 36)
    text = font.render(f"Lives: {player.lives}", True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

