import pygame


class Mario(pygame.sprite.Sprite):
    def __init__(self, screen, left, stats):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("assets/images/mario.png")
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


class Hello_it_is_me_MARIO(Mario):
    def __init__(self, screen, left, stats):
        super().__init__(screen, left, stats)
        self.rect.bottom = self.screen_rect.bottom - 15
        self.rx = float(self.rect.right)

