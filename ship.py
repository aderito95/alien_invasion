import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("./images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship ay the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 15.0

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self, ai, direction):
        if direction == "RIGHT":
            if (ai.screen.get_width() - self.rect.right) / self.speed > 0:
                self.x += self.speed
            else:
                self.x += ai.screen.get_width() - self.rect.right
        elif direction == "LEFT":
            if self.rect.left / self.speed > 0:
                self.x -= self.speed
            else:
                self.x -= self.rect.left
        elif direction == "UP":
            if self.rect.top / self.speed > 0:
                self.y -= self.speed
            else:
                self.y -= self.rect.top
        elif direction == "DOWN":
            if (ai.screen.get_height() - self.rect.bottom) / self.speed > 0:
                self.y += self.speed
            else:
                self.y += ai.screen.get_height() - self.rect.bottom
        self.rect.x = self.x
        self.rect.y = self.y
