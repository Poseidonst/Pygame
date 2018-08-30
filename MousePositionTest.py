import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Slither")

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

while not gameExit:
    position = [i for i in pygame.mouse.get_pos()]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -5
            if event.key == pygame.K_RIGHT:
                lead_x_change = 5
            if event.key == pygame.K_UP:
                lead_y_change = -5
            if event.key == pygame.K_DOWN:
                lead_y_change = 5
        if event.type == pygame.MOUSEBUTTONDOWN:
            lead_x = position[0]
            lead_y = position[1]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                lead_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0

    lead_x += lead_x_change
    lead_y += lead_y_change

    if lead_x > 800:
        lead_x = 0
        x = True
    elif lead_x < 0:
        lead_x = 800
    elif lead_y > 600:
        lead_y = 0
    elif lead_y < 0:
        lead_y = 600

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
