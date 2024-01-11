import pygame


class Ptero(pygame.sprite.Sprite):
    def __init__(self, screen, left, stats):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("assets/images/ptero.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = left
        self.speed = min((7.5 + stats.score // 250 * 0.6, 14))
        self.rx = float(-1)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, stats):
        self.rx -= self.speed
        self.rect.right = self.rx


class EarthPtero(Ptero):
    def __init__(self, screen, left, stats):
        super().__init__(screen, left, stats)
        self.rect.bottom = self.screen_rect.bottom - 15
        self.rx = float(self.rect.right)


class MiddlePtero(Ptero):
    def __init__(self, screen, left, stats):
        super().__init__(screen, left, stats)
        self.rect.bottom = self.screen_rect.bottom - 70
        self.rx = float(self.rect.right)


class AirPtero(Ptero):
    def __init__(self, screen, left, stats):
        super().__init__(screen, left, stats)
        self.rect.bottom = self.screen_rect.bottom - 125
        self.rx = float(self.rect.right)
