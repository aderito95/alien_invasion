import pygame


class Music:
    """A class to handle audio effects for the game"""

    def __init__(self):
        pygame.mixer.music.load("./music/space.mp3")
        self.crash_sound = pygame.mixer.Sound("./music/arcadegameexplosion.wav")

    def pause_music(self):
        pygame.mixer.music.pause()

    def play_music(self):
        pygame.mixer.music.play(-1)

    def crash(self):
        pygame.mixer.Sound.play(self.crash_sound)
