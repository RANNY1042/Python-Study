import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./images/ship.bmp')
rect=image.get_rect()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    #exit버튼을 누를때까지 반복

    # Do logical updates here.
    # ...

    screen.fill("blue")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    screen.blit(image,rect)
    

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)