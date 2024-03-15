import sys
import pygame

fps = 30
pygame.init()

WIDTH = 1280
HEIGHT = 720
BULLET_COLOR = 255,0,0

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
image = pygame.image.load('./images/ship.bmp')

rect = pygame.Rect(500,500,100,100)
rect = screen.get_rect()
rect = image.get_rect()

screen_rect=pygame.Rect((1280/2,720/2),(200,200))
ship_rect = image.get_rect()
ship_rect.midbottom=screen.get_rect().midbottom
#image_rect.left=1280/2
#image_rect.top=600

#image_rect.midbottom = screen_rect.midbottom
def create_bullet(ship_rect):
    bullet = pygame.Rect(0,0,5,50)
    bullet.midtop = ship_rect.midtop
    return bullet

bullets = []
bullet = create_bullet(ship_rect)
bullets.append(bullet)


bullet = pygame.Rect(0,0,5,50)
bullet.midtop = ship_rect.midtop
bullet_color=(BULLET_COLOR)


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    #exit버튼을 누를때까지 반복
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                SPEED = 5
                ship_rect.left -= SPEED
            elif event.key == pygame.K_RIGHT:
                SPEED = 5
                ship_rect.right += SPEED
            elif event.key == pygame.K_UP:
                SPEED = 5
                ship_rect.top -= SPEED
            elif event.key == pygame.K_DOWN:
                if ship_rect.top+ ship_rect.height <=screen_rect.height:
                    SPEED = 5
                    ship_rect.bottom += SPEED
            elif event.key == pygame.K_SPACE:
                bullets.append(create_bullet(ship_rect))

    # Do logical updates here. 
    # ...

    
    new_bullets = []
    for bullet in bullets:
        if screen_rect.top < bullet.top:
            bullet.top -=1
            new_bullets.append(bullet)
        else: 
        
    
    screen.fill("blue")  # Fill the display with a solid color


    # Render the graphics here.
    # ...
    screen.blit(image,ship_rect)
    for bullet in bullets:
         pygame.draw.rect(screen,bullet_color,bullet)
    #screen.blit(image, pygame.Rect(image))

    pygame.draw.rect(screen,bullet_color,bullet)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(fps)         # wait until next frame (at 60 FPS)