import pygame
from dino import Dino
import controls
from stats import Stats
from screen_image import ScreenImage


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 900
HEIGHT = 377
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SPRITES_COLOR = (100, 100, 100)
pygame.init()


def start():
    pygame.init()
    pygame.display.set_caption("T-rex")
    icon = pygame.image.load("assets/images/dino-rex.png")
    pygame.display.set_icon(icon)
    pygame.mixer.music.load("assets/sounds/fon.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    # pygame.mixer.music.load("assets/sounds/fon2.wav")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.load("assets/sounds/fon3.wav")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.load("assets/sounds/fon4.wav")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.load("assets/sounds/fon5.wav")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.3)
    screen_im = ScreenImage(screen)
    dino = Dino(screen)
    cactuses = pygame.sprite.Group()
    pteros = pygame.sprite.Group()
    marios = pygame.sprite.Group()
    stats = Stats()
    clock = pygame.time.Clock()

    while True:
        if stats.run:
            controls.run_events(dino, stats)
            if not stats.pause:
                stats.update_time()
                controls.move_dino(dino)
                controls.create_and_remove_enemies(screen, cactuses, pteros, marios, stats)
                controls.update(screen, screen_im, SPRITES_COLOR, dino,
                                cactuses, pteros, stats)
            else:
                controls.pause(screen, screen_im, SPRITES_COLOR, dino, cactuses, pteros, stats)
        else:
            controls.lose(screen, dino, SPRITES_COLOR, screen_im, cactuses, pteros, stats)
            controls.lose_events(screen, dino, cactuses, pteros, stats, screen_im)
        clock.tick(60)
    screen.blit(dino, (900 // 2 - dino.get_width() // 2, 378 // 2 - dino.get_height() // 2))
    pygame.display.flip()


start()
