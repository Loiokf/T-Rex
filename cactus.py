import pygame
from random import choice


class Cactus(pygame.sprite.Sprite):
    def __init__(self, screen, left, stats):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(choice(("assets/images/cactus1.png", "assets/images/cactus2.png")))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = left
        self.rect.bottom = self.screen_rect.bottom - 15
        self.rx = float(self.rect.right)
        self.speed = min((6.0 + stats.score // 250 * 0.5, 11.5))

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, stats):
        self.rx -= self.speed
        self.rect.right = self.rx
