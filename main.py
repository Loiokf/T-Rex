import pygame
from dino import Dino
import controls
from stats import Stats
from screen_image import ScreenImage

WIDTH = 900
HEIGHT = 377
SPRITES_COLOR = (100, 100, 100)


def start():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dinosaur")
    icon = pygame.image.load("assets/images/dino.png")
    pygame.display.set_icon(icon)

    screen_im = ScreenImage(screen)
    dino = Dino(screen)
    cactuses = pygame.sprite.Group()
    pteros = pygame.sprite.Group()
    stats = Stats()
    clock = pygame.time.Clock()

    while True:
        if stats.run:
            controls.run_events(dino, stats)
            if not stats.pause:
                stats.update_time()
                controls.move_dino(dino)
                controls.create_and_remove_enemies(screen, cactuses, pteros, stats)
                controls.update(screen, screen_im, SPRITES_COLOR, dino,
                                cactuses, pteros, stats)  # обновляем экран
            else:
                controls.pause(screen, screen_im, SPRITES_COLOR, dino, cactuses, pteros, stats)
        else:
            controls.lose(screen, dino, SPRITES_COLOR, screen_im, cactuses, pteros, stats)
            controls.lose_events(screen, dino, cactuses, pteros, stats, screen_im)
        clock.tick(60)


start()
