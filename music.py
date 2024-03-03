import pygame


class Music:
    """A class to handle audio effects for the game"""

    def __init__(self):
        pygame.mixer.music.load("./music/space.mp3")
        self.crash_sound = pygame.mixer.Sound("./music/arcadegameexplosion.wav")
        self.car_explosion = pygame.mixer.Sound("./music/car_explosion.wav")
        self.win_sound = pygame.mixer.Sound("./music/win.mp3")

    def pause_music(self):
        pygame.mixer.music.pause()

    def play_music(self):
        pygame.mixer.music.play(-1)

    def crash(self):
        pygame.mixer.Sound.play(self.crash_sound)

    def ship_explosion(self):
        pygame.mixer.Sound.play(self.car_explosion)

    def win(self):
        pygame.mixer.Sound.play(self.win_sound)
