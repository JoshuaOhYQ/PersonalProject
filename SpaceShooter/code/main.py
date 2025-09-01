import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
caption = "Space Shooter"
pygame.display.set_caption(caption)
running = True

# Plain Surface
surf = pygame.Surface((100, 200))
surf.fill('darkblue')
x = 100

#Import images
player_surf = pygame.image.load('../images/player.png')




while running:
    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    #Game Drawing
    x += 0.1
    display_surface.fill('gray')
    display_surface.blit(surf, (x, 150))
    pygame.display.update()


pygame.quit()




