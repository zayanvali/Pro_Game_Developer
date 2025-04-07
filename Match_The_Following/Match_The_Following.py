import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
pygame.display.update()
subway_surfer = pygame.image.load("C:/Users/valim/Downloads/JetLearn/Pro Game Developer/images/subwaysurfer.png")
ludo = pygame.image.load("C:/Users/valim/Downloads/JetLearn/Pro Game Developer/images/ludo.png")
temple_run = pygame.image.load("C:/Users/valim/Downloads/JetLearn/Pro Game Developer/images/templerun.png")
candy_crush = pygame.image.load("C:/Users/valim/Downloads/JetLearn/Pro Game Developer/images/candycrush.jpg")

screen.blit(subway_surfer, (150, 100))
screen.blit(ludo, (150, 200))
screen.blit(temple_run, (150, 300))
screen.blit(candy_crush, (150, 400))
font = pygame.font.SysFont("Times New Roman", 36)

text1 = font.render("Ludo", True, (0, 0, 0))
text2 = font.render("Candy Crush", True, (0, 0, 0))
text3 = font.render("Subway Surfer", True, (0, 0, 0))
text4 = font.render("Temple Run", True, (0, 0, 0))
screen.blit(text1, (350, 100))
screen.blit(text2, (350, 200))
screen.blit(text3, (350, 300))
screen.blit(text4, (350, 400))
pygame.display.update()

running = True
while running:
    
    event =  pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0, 0, 0), (pos), 20, 0)
        pygame.display.update()
        
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,0), (pos), (pos2),5)
        pygame.draw.circle(screen, (0,0,0) ,(pos2), 20, 0)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

pygame.quit()