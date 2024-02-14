import pygame


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.bg_color = (230, 230, 230)
        self.screen = Settings.get_screen_resolution()

    @staticmethod
    def get_screen_resolution():
        """Ottieni la risoluzione dello schermo principale"""
        screen_modes = pygame.display.list_modes(0)
        if screen_modes:
            screen_width, screen_height = screen_modes[0]
        else:
            # Se non è disponibile alcuna informazione sulla risoluzione dello schermo, usa valori predefiniti
            screen_width, screen_height = 800, 600

        # Imposta la dimensione della finestra di gioco in base alla dimensione dello schermo
        return pygame.display.set_mode((screen_width, screen_height - 60))
