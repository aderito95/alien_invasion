import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        # Ottieni la risoluzione dello schermo principale
        screen_modes = pygame.display.list_modes(0)
        if screen_modes:
            self.screen_width, self.screen_height = screen_modes[0]
        else:
            # Se non è disponibile alcuna informazione sulla risoluzione dello schermo, usa valori predefiniti
            self.screen_width, self.screen_height = 800, 600

        # Imposta la dimensione della finestra di gioco in base alla dimensione dello schermo
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height - 60)
        )
        pygame.display.set_caption("Alien invasion")
        # Imposta il colore di sfondo
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        # Calcola l'altezza della barra del titolo dopo l'inizializzazione della finestra

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
