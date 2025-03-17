import pygame

pygame.init()
WIDTH = 700
HEIGHT = 500

caption = "Rocket In Space"

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(caption)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/valim/Downloads/JetLearn/Pro Game Developer/images/character.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()

    #Move the sprite based on key pressed
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)

        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)

        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.top <=0:
            self.rect.top = 0

        elif self.rect.top >= HEIGHT:
            self.rect.top = HEIGHT

#Making a group of all the sprites
sprites = pygame.sprite.Group()

def startgame():
    player = Player()
    sprites.add(player)

    #Start the game loop
    while True:
        #Look at every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        #get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        #Add backgroung image
        screen.blit(pygame.image.load("C:/Users/valim/Downloads/JetLearn/Pro Game Developer/images/space.png"), (0, 0))

        #Draw the sprites
        sprites.draw(screen)

        pygame.display.update()

startgame()