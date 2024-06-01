import pygame

pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption('LearningPygame')

square = pygame.Surface((180,50))
square.fill('Green')

bg = pygame.image.load('images/backgroundfon.jpg')
bg = pygame.transform.scale(bg, (600,300))
player = pygame.image.load('images/PlayerLearnPython/Player_left/PlayerAnimationLeft1.xcf')
#player = pygame.transform.scale(player, (110,100))

cycle = True
while cycle:

    screen.blit(bg,(0,0))
    screen.blit(player, (630, 175))
    #screen.blit(player,(500,300))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cycle = False
            pygame.quit()