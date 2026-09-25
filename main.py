# Imports:
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


# Main
def main():

    pygame.init()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game Objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Game Variables
    dt: float = 0.0

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000


# Only start main if main.py is run via UV
if __name__ == "__main__":
    main()
