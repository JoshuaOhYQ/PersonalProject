import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((500, 720))
pygame.display.set_caption("Tatabahasa")


# Fonts & Colors
font = pygame.font.Font(None, 40)
WHITE, BLACK, GREEN, RED = (255,255,255), (0,0,0), (0,200,0), (200,0,0)

# Question & Answers
question = "Which is a verb?"
options = ["Dog", "Run", "Blue", "Table"]
correct_answer = "Run"

def draw_text(text, pos, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, pos)

running = True
while running:
    screen.fill(WHITE)

    # Draw Question
    draw_text(question, (50, 50))

    # Draw Options
    for i, option in enumerate(options):
        draw_text(f"{i+1}. {option}", (50, 120 + i*50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                choice = options[int(event.unicode)-1]
                if choice == correct_answer:
                    draw_text("Correct! 🎉", (50, 320), GREEN)
                else:
                    draw_text("Try again!", (50, 320), RED)

    pygame.display.flip()

pygame.quit()
sys.exit()
