import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.bullets = pygame.sprite.Group()

        self.screen = self.settings.screen
        pygame.display.set_caption("Alien invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_bullets()
            # redraw the screen
            self._update_screen()
            # Pygame will do its best to make the loop run exactly 60 times per second
            self.clock.tick(60)

    # helper method: does work inside a class but it isn't mean to be used  by code outside the class
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._fire_bullets()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            sys.exit()
        elif keys[pygame.K_RIGHT]:
            self.ship.update(self, direction="RIGHT")
        elif keys[pygame.K_LEFT]:
            self.ship.update(self, direction="LEFT")
        elif keys[pygame.K_UP]:
            self.ship.update(self, direction="UP")
        elif keys[pygame.K_DOWN]:
            self.ship.update(self, direction="DOWN")

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        # Draw all created bullets
        for bullet in self.bullets:
            bullet.draw_bullet()
        # Draw ship
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _fire_bullets(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # the group automatically calls update() for each sprite in the group
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


# This code block will only run if this file is called directly
if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
