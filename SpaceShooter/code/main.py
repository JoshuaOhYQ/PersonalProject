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
clock = pygame.time.Clock()

# Plain Surface
surf = pygame.Surface((100, 200))
surf.fill('darkblue')
x = 100


# Import images
player_surf = pygame.image.load(join('SpaceShooter', 'images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1, 1)
player_speed = 300

star_surf = pygame.image.load(join('SpaceShooter', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join('SpaceShooter', 'images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('SpaceShooter', 'images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))


while running:
    dt = clock.tick() / 1000

    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # Game Drawing
    display_surface.fill('dark blue')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # player movement
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
        player_direction.y *= -1

    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1

    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_rect)
    
    
    pygame.display.update()


pygame.quit()




