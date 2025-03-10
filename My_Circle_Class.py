import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0,)
white = (255, 255, 255)
screen.fill(white)

class my_circle():
    def __init__(self, color, pos, rad, width = 0):
        self.color = color
        self.pos = pos
        self.width = width
        self.rad = rad
        self.scrn = screen
    
    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.width)

    def grow(self, x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.width)

#Drawing a circle
position = (300, 300)
radius = 50
width = 2
pygame.draw.circle(screen, red, position, radius, width)
pygame.display.update()

blue_circle = my_circle(blue, position, radius + 60)
red_circle = my_circle(red, position, radius + 40)
yellow_circle = my_circle(yellow, position, radius, 5)
green_circle = my_circle(green, position, 20)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (event.type == pygame.MOUSEBUTTONDOWN):
            blue_circle.draw()
            red_circle.draw()
            yellow_circle.draw()
            green_circle.draw()
            pygame.display.update()

        elif (event.type == pygame.MOUSEBUTTONUP):
            blue_circle.grow(2)
            red_circle.grow(2)
            yellow_circle.grow(2)
            green_circle.grow(2)
            pygame.display.update()

        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            black_circle = my_circle(black, pos, 5)
            black_circle.draw()
            pygame.display.update()