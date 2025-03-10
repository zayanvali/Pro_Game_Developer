from random import randint
import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)
color = R, G, B

screen.fill(color)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()