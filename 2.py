import pygame
import sys

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Grammar Adventure")
font = pygame.font.Font(None, 36)
WHITE, BLACK, GREEN, RED = (255,255,255), (0,0,0), (0,200,0), (200,0,0)

# Story Data
story = [
    {
        "text": "You enter the Magic Forest. A wise owl asks: 'Which word is a noun?'",
        "options": ["Run", "Tree", "Blue"],
        "answer": "Tree"
    },
    {
        "text": "The wizard ___ a spell to open the gate.",
        "options": ["casts", "cast", "casting"],
        "answer": "casts"
    },
    {
        "text": "You see a dragon! Choose the correct sentence:",
        "options": ["The dragon fly fast.", "The dragon flies fast.", "The dragon flying fast."],
        "answer": "The dragon flies fast."
    }
]

current_level = 0
feedback = ""

def draw_text(text, pos, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, pos)

running = True
while running:
    screen.fill(WHITE)

    # Current story block
    block = story[current_level]
    draw_text(block["text"], (50, 50))

    # Draw options
    for i, option in enumerate(block["options"]):
        draw_text(f"{i+1}. {option}", (50, 150 + i*50))

    # Feedback
    if feedback:
        color = GREEN if "Correct" in feedback else RED
        draw_text(feedback, (50, 400), color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode in ["1", "2", "3"]:
                choice = block["options"][int(event.unicode)-1]
                if choice == block["answer"]:
                    feedback = "✅ Correct! Adventure continues..."
                    pygame.time.delay(800)
                    current_level += 1
                    feedback = ""
                    if current_level >= len(story):
                        feedback = "🎉 You finished the adventure!"
                else:
                    feedback = "❌ Wrong! Try again."

    pygame.display.flip()

pygame.quit()
sys.exit()
