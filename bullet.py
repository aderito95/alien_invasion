import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.speed = 5.0
        self.width = 3
        self.height = 15
        self.color = (60, 60, 60)

        self.screen = ai_game.screen

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        """self.image = pygame.transform.scale(
            pygame.image.load("./images/bullet.png"), (100, 100)
        )
        self.rect = self.image.get_rect()"""
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up to the screen"""
        self.y -= self.speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
