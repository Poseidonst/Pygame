import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

game_width = 600
game_heigth = 600
gameDisplay = pygame.display.set_mode((game_width, game_heigth))



def gameLoop():

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.display.set_caption("Boter Kaas en Eieren")
        gameDisplay.fill(red)
        pygame.draw.rect(gameDisplay, black, [50, 50, 500, 500])
        pygame.draw.rect(gameDisplay, white, [100, 100, 100, 100])
        pygame.draw.rect(gameDisplay, white, [250, 100, 100, 100])
        pygame.draw.rect(gameDisplay, white, [400, 100, 100, 100])
        pygame.draw.rect(gameDisplay, white, [100, 250, 100, 100])
        pygame.draw.rect(gameDisplay, white, [250, 250, 100, 100])
        pygame.draw.rect(gameDisplay, white, [400, 250, 100, 100])
        pygame.draw.rect(gameDisplay, white, [100, 400, 100, 100])
        pygame.draw.rect(gameDisplay, white, [250, 400, 100, 100])
        pygame.draw.rect(gameDisplay, white, [400, 400, 100, 100])
        pygame.display.update()

    pygame.quit()
    quit()

gameLoop()
