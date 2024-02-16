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
        print(
            f"right x: {self.ship.rect.right}\nscreen width: {self.screen.get_width()}\nship speed: {self.ship.speed}\ndifference: {(2560-1910)%50}\n"
        )

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            sys.exit()
        elif keys[pygame.K_RIGHT]:
            self._check_for_outer_collisions()
        elif keys[pygame.K_LEFT]:
            if self.ship.rect.left < 0:
                pass
            else:
                self.ship.rect.x -= self.ship.speed
        elif keys[pygame.K_UP]:
            if self.ship.rect.top < 0:
                pass
            else:
                self.ship.rect.y -= self.ship.speed
        elif keys[pygame.K_DOWN]:
            if self.ship.rect.bottom > self.screen.get_height():
                pass
            else:
                self.ship.rect.y += self.ship.speed

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _check_for_outer_collisions(self):
        if (self.screen.get_width() - self.ship.rect.right) / self.ship.speed > 0:
            self.ship.rect.x += self.ship.speed
        else:
            self.ship.speed = self.screen.get_width() - self.ship.rect.right
            self.ship.rect.x += self.ship.speed
            self.ship.speed = self.ship.default_speed


# This code block will only run if this file is called directly
if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
