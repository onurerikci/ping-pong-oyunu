from pygame import *

window_width, window_height = 800, 600

window = display.set_mode((window_width, window_height))

display.set_caption("Ping-Pong Oyunu")

background = transform.scale(image.load("galaxy.jpg"), (window_width, window_height))

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
        if keys[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 100:
            self.rect.y += self.speed

player_1_image = "player1.png"
player_1 = Player1(player_1_image, 5, window_height - 100, 100, 100, 20)

player_2_image = "player2.png"
player_2 = Player2(player_2_image, window_width - 100, 5, 100, 100, 20)

ball_image = "ball.png"
ball = GameSprite(ball_image, window_width / 2, window_height / 2, 25, 25, 20)

clock = time.Clock()
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(background, (0, 0))

    player_1.update()
    player_1.reset()
    player_2.update()
    player_2.reset()
    ball.update()
    ball.reset()
    display.update()
    clock.tick(60)