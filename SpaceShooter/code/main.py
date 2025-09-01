import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
caption = "Space Shooter"
pygame.display.set_caption(caption)
running = True

while running:
    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    #Game Drawing
    display_surface.fill('red')
    pygame.display.update()


pygame.quit()




