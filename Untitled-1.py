from pygame import*
from random import randint

class Game_sprite(sprite.Sprite):
    def __init__(self, img, w, h, x, y):
        super().__init__()
        self.image = transform.scale(img, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        screen.blit(self.image, self.rect)


class Dino(Game_sprite):
    def __init__(self):
        super().__init__(image.load('dino-removebg-preview.png'), 100, 300, 100, 108 )
        self.isJump = False
        self.jumpCount = -15
        
    def update(self):
        if self.isJump:
            self.rect.y += self.jumpCount
            self.jumpCount += 1
            if self.jumpCount > 15:
                self.jumpCount = -15
                self.isJump = False

        super().update()


class Enemy(Game_sprite):
    def __init__(self):
        super().__init__(image.load('enemy-removebg-preview.png'), 100, 100, 900, 258 )
    def update(self):
        if self.rect.x <= -60:
            self.rect.x = 900
        self.rect.x -= 10

        super().update()




        
screen = display.set_mode((800, 600))
display.set_caption('Game')
background = image.load('background.png')
background=transform.scale(background, (800,500))

dino = Dino()
enemy = Enemy()

button_play = transform.scale(image.load('play.png'), (200, 80))
button_quit = transform.scale(image.load('quit.png'), (200, 80))




clock = time.Clock()
finish = False
menu =  False
game = True
while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    x, y = mouse.get_pos()
                    if menu:
                        if x > 350 and x < 550 and y > 200 and y < 280:
                            menu = False
                            finish = False
                            dino = Dino()
                            enemy = Enemy()
                            #что здесь перезапуск персонажей
                        if x > 350 and x < 550 and y > 400 and y < 480:
                            game = False  
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                dino.isJump = True
    if menu:
        screen.blit(background, (0,0))       
        screen.blit(button_play, (350, 200))
        screen.blit(button_quit, (350, 400))
    elif not(finish):
        if dino.rect.colliderect(enemy.rect):
            finish = True
            menu = True
            dino = Dino()
            enemy = Enemy()
        screen.blit(background, (0,0))       
        dino.update()
        enemy.update()   
    display.update()
    