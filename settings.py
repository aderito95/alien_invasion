import pygame


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.bg_color = (230, 230, 230)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bullets_allowed = 3
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        self.ship_limit = 3
