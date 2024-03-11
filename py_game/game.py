import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load('./images/ship.bmp')

rect = pygame.Rect(500,500,100,100)
rect = screen.get_rect()
rect = image.get_rect()

screen_rect=pygame.Rect((1280/2,720/2),(200,200))
image_rect = image.get_rect()
#image_rect.left=1280/2
#image_rect.top=600
image_rect.midbottom=screen.get_rect().midbottom
#image_rect.midbottom = screen_rect.midbottom


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    #exit버튼을 누를때까지 반복
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                image_rect.left -= 1
            elif event.key == pygame.K_RIGHT:
                image_rect.right += 1
            elif event.key == pygame.K_UP:
                image_rect.top -=1
            elif event.key == pygame.K_DOWN:
                if image_rect.top < screen_rect.height:
                    image_rect.bottom +=1

    # Do logical updates here.
    # ...

    screen.fill("blue")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    screen.blit(image,image_rect)
    #screen.blit(image, pygame.Rect(image))
    

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)