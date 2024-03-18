import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
FONT_SIZE = 50
GUESS_X = 100
GUESS_Y = 500
HIDDEN_WORD = "HELLO"
MAX_TRIES = 6

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")

# Set up fonts
font = pygame.font.SysFont(None, FONT_SIZE)
guess_font = pygame.font.SysFont(None, FONT_SIZE)
result_font = pygame.font.SysFont(None, FONT_SIZE)

# Helper function to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Function to draw the hangman
def draw_hangman(tries):
    parts = [
        (100, 400, 100, 50),   # base
        (150, 400, 150, 100),  # upright
        (150, 200, 300, 200),  # crossbar
        (300, 200, 300, 250),  # rope
        (300, 250, 350, 300),  # head
        (300, 300, 350, 350),  # body
        (300, 320, 280, 340),  # left arm
        (300, 320, 320, 340),  # right arm
        (300, 350, 280, 370),  # left leg
        (300, 350, 320, 370)   # right leg
    ]
    for i in range(tries):
        if i < len(parts):
            pygame.draw.line(screen, BLACK, parts[i][0:2], parts[i][2:4], 5)

# Function to check if the guess is correct
def check_guess(guess, hidden_word):
    if len(guess) != len(hidden_word):
        return False
    for i in range(len(guess)):
        if guess[i].upper() != hidden_word[i]:
            return False
    return True

# Main game loop
def main():
    guessed_letters = set()
    tries = 0
    running = True

    while running:
        screen.fill(WHITE)

        # Draw hidden word
        for i in range(len(HIDDEN_WORD)):
            if HIDDEN_WORD[i].upper() in guessed_letters:
                draw_text(HIDDEN_WORD[i].upper(), font, BLACK, screen, 300 + i * FONT_SIZE, 100)
            else:
                pygame.draw.line(screen, BLACK, (300 + i * FONT_SIZE, 120), (350 + i * FONT_SIZE, 120), 3)

        # Draw guessed letters
        guessed_str = ' '.join(guessed_letters)
        draw_text("Guessed: " + guessed_str, guess_font, BLACK, screen, GUESS_X, GUESS_Y)

        # Draw hangman
        draw_hangman(tries)

        # Check win or lose
        if tries >= MAX_TRIES:
            draw_text("You lose! The word was {}".format(HIDDEN_WORD), result_font, RED, screen, 200, 250)
            running = False
        elif set(HIDDEN_WORD.upper()) == guessed_letters:
            draw_text("You win!", result_font, GREEN, screen, 300, 250)
            running = False

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    guess = event.unicode.upper()
                    if guess not in guessed_letters:
                        guessed_letters.add(guess)
                        if guess not in HIDDEN_WORD.upper():
                            tries += 1

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
