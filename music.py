import pygame


class Music:
    def __init__(self):
        pygame.mixer.music.load("./music/space.mp3")
        pygame.mixer.music.play(-1)
        self.crash_sound = pygame.mixer.Sound("./music/arcadegameexplosion.wav")

    def pause_music(self):
        pygame.mixer.music.pause()

    def crash(self):
        pygame.mixer.Sound.play(self.crash_sound)
