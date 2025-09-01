import pygame
from os.path import join
from random import randint

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
player_surf = pygame.image.load(join('SpaceShooter', 'images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('SpaceShooter', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    #Game Drawing
    x += 0.1
    display_surface.fill('dark blue')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()



    


pygame.quit()




