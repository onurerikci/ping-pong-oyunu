from pygame import *

window_width, window_height = 600, 500

window = display.set_mode((window_width, window_height))

display.set_caption("Ping-Pong Oyunu")

background = (200, 255, 255)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height - 125:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 125:
            self.rect.y += self.speed

player_1 = Player1("player1.png", 35, window_height - 100, 25, 120, 10)

player_2 = Player2("player2.png", window_width - 60, 5, 25, 120, 10)

ball = GameSprite("ball.png", window_width / 2, window_height / 2, 25, 25, 10)

font.init()

font = font.Font(None, 35)

lose1 = font.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOSE!", True, (180, 0, 0))

run = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if finish is not True:
        window.fill(background)
        player_1.update()
        player_2.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1

        if ball.rect.y > window_height -25 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        
        if ball.rect.x > window_width - 25:
            finish = True
            window.blit(lose2, (200, 200))

        player_1.reset()
        player_2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)