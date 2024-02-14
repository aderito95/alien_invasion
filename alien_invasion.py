import sys
import pygame

from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = self.settings.screen

        pygame.display.set_caption("Alien invasion")
        # Imposta il colore di sfondo
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible
            pygame.display.flip()
            # Pygame will do its best to make the loop run exactly 60 times per second
            self.clock.tick(60)


# This code block will only run if this file is called directly
if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
