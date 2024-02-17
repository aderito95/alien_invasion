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
            self.ship.rect.x += self._calculate_ship_speed(direction="RIGHT")
        elif keys[pygame.K_LEFT]:
            self.ship.rect.x -= self._calculate_ship_speed(direction="LEFT")
        elif keys[pygame.K_UP]:
            self.ship.rect.y -= self._calculate_ship_speed(direction="UP")
        elif keys[pygame.K_DOWN]:
            self.ship.rect.y += self._calculate_ship_speed(direction="DOWN")

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _calculate_ship_speed(self, direction):
        if direction == "RIGHT":
            if (self.screen.get_width() - self.ship.rect.right) / self.ship.speed > 0:
                return self.ship.speed
            else:
                return self.screen.get_width() - self.ship.rect.right
        elif direction == "LEFT":
            if self.ship.rect.left / self.ship.speed > 0:
                return self.ship.speed
            else:
                return self.ship.rect.left
        elif direction == "UP":
            if self.ship.rect.top / self.ship.speed > 0:
                return self.ship.speed
            else:
                return self.ship.rect.top
        elif direction == "DOWN":
            if (self.screen.get_height() - self.ship.rect.bottom) / self.ship.speed > 0:
                return self.ship.speed
            else:
                return self.screen.get_height() - self.ship.rect.bottom


# This code block will only run if this file is called directly
if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
