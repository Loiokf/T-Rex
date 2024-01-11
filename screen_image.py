import pygame


class ScreenImage:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assets/images/long_screen.png")
        self.x = 0
        self.speed = 1

    def draw(self):
        self.screen.blit(self.image, (self.x, 0))

    def move_background(self):
        self.x -= self.speed
        if self.x < -900:
            self.x = 0

    def restart(self):
        self.x = 0

    def pause(self):
        self.speed = 0.3

    def unpause(self):
        self.speed = 1
