
import pygame
from random import *
import time

start_time = time.clock()

pygame.init()
pygame.mixer.init()
pygame.font.init()
timing = time.time()

W = 700
H = 500
FPS = 60

font = pygame.font.Font(None, 70)
win = font.render("YOU WIN!", True, (255, 215, 0))
lose = font.render("YOU LOSE!!!", True, (180, 0, 0))


window = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (W, H)) #!

pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        self.image = pygame.transform.scale(pygame.image.load(image), (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < W - 80:
            self.rect.x += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
            # print("pug")
        if self.rect.y <= 470:
            self.direction = "right"

        if self.direction == "left":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



player = Player("tenis_ball.png", 300, 400, 5)


enemy_1 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_2 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_3 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_4 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_5 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_6 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_7 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_8 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_9 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_10 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_11 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))
enemy_12 = Enemy("asteroid.png", randint(100, 600), randint(10, 20), randint(1, 10))

loop = True
Play = True

f = 0
g = 0
h =0




while loop:
    # print(val_time)
    clock.tick(FPS)
    window.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    val_time = round(time.clock() - start_time)
    manr = font.render( str(val_time), True, (180, 0, 0))
    
    window.blit( manr, (100, 100))
    if (pygame.sprite.collide_rect(player, enemy_1)
    or pygame.sprite.collide_rect(player, enemy_2)
    or pygame.sprite.collide_rect(player, enemy_3)
    or pygame.sprite.collide_rect(player, enemy_4)
    or pygame.sprite.collide_rect(player, enemy_5)
    or pygame.sprite.collide_rect(player, enemy_6)
    or pygame.sprite.collide_rect(player, enemy_7)
    or pygame.sprite.collide_rect(player, enemy_8)
    or pygame.sprite.collide_rect(player, enemy_9)
    or pygame.sprite.collide_rect(player, enemy_10)
    or pygame.sprite.collide_rect(player, enemy_11)
    or pygame.sprite.collide_rect(player, enemy_12)
    ):
        Play = False
        window.blit(lose, (200, 200))
    
        
    
    
    if Play != False:
         
        
        player.update()
        player.reset()
  
    
        enemy_1.update()
        enemy_1.reset()
        enemy_2.update()
        enemy_2.reset()
        enemy_3.update()
        enemy_3.reset()


        if time.time() - timing > 5.0:
            enemy_4.update()
            enemy_4.reset()
            enemy_5.update()
            enemy_5.reset()
            enemy_6.update()
            enemy_6.reset()
            enemy_7.update()
            enemy_7.reset()
        
        if time.time() - timing > 10.0:
            enemy_8.update()
            enemy_8.reset()
            enemy_9.update()
            enemy_9.reset()
            enemy_10.update()
            enemy_10.reset()
            enemy_11.update()
            enemy_11.reset()
            enemy_12.update()
            enemy_12.reset()
        
                


 
    if time.time() - timing > 15.0:
        Play = False
        window.blit(win, (200, 200))

    pygame.display.update()


