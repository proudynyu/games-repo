import pygame
import random

pygame.init()

screen = (500, 500)
win = pygame.display.set_mode(screen)
pygame.display.set_caption('Snake Game')

class Snake():
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.width = 25
        self.height = 25
        self.vel = vel

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.x == 0:
                pass
            else:
                self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            if self.x + self.width >= 500:
                pass
            else:
                self.x += self.vel

        if keys[pygame.K_UP]:
            if self.y == 0:
                pass
            else:
                self.y -= self.vel

        if keys[pygame.K_DOWN]:
            if self.y + self.height >= 500:
                pass
            else:
                self.y += self.vel
    
class Food():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)
        self.width = 20
        self.height = 20
        self.pos = (self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.pos) 

snake = Snake(0, 0, 12)

def reDrawWin():
    win.fill((0,0,0))
    snake.draw(win)
    pygame.display.update()

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.move()

    reDrawWin()


    
pygame.quit()