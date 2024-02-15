import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = self.settings.screen
        pygame.display.set_caption("Alien invasion")
        self.ship = Ship(self)
        print(self.ship.rect.bottom)

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()
            self._update_screen()
            # Pygame will do its best to make the loop run exactly 60 times per second
            self.clock.tick(60)

    # helper method: does work inside a class but it isn't mean to be used  by code outside the class
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        self.move_ticker = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.ship.rect.x += 1
        elif keys[pygame.K_LEFT]:
            self.ship.rect.x -= 1
        elif keys[pygame.K_UP]:
            self.ship.rect.y -= 1
        elif keys[pygame.K_DOWN]:
            if self.ship.rect.bottom == self.screen.get_height():
                pass
            else:
                self.ship.rect.y += 1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()


# This code block will only run if this file is called directly
if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
