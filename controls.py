import pygame
import sys
from creater_enemies import easy_score, normal_score, hard_score
from random import choice


def run_events(dino, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if not dino.bending:
                    dino.jumping = True
                dino.queue_to_jump = True
            elif event.key == pygame.K_DOWN:
                if dino.end_jumping():
                    dino.bending = True
                else:
                    dino.queue_to_bend = True
            elif event.key == pygame.K_RETURN:
                stats.pause = not stats.pause
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                dino.jumping = False
                dino.queue_to_jump = False
            elif event.key == pygame.K_DOWN:
                if dino.bending:
                    dino.end_bend()
                dino.bending = False
                dino.queue_to_bend = False


def lose_events(screen, dino, cactuses, pteros, stats, screen_im):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                dino.restart(screen)
                cactuses.empty()
                pteros.empty()
                stats.restart()
                screen_im.restart()


def draw_screen(screen, screen_image, sprites_color, dino, cactuses, pteros, stats):
    screen_image.draw()
    dino.draw()
    for cactus in cactuses.sprites():
        cactus.draw()
    for ptero in pteros.sprites():
        ptero.draw()
    print_score(screen, stats, sprites_color)
    print_record(screen, stats, sprites_color)

                        
def update(screen, screen_image, sprites_color, dino, cactuses, pteros, stats):
    screen_image.unpause()
    draw_screen(screen, screen_image, sprites_color, dino, cactuses, pteros, stats)
    dino.update_image()
    screen_image.move_background()
    for cactus in cactuses.sprites():
        cactus.update(stats)
    for ptero in pteros.sprites():
        ptero.update(stats)
    stats.update_score()
    pygame.display.flip()
    if pygame.sprite.spritecollideany(dino, cactuses) or pygame.sprite.spritecollideany(dino, pteros):
        sound = pygame.mixer.Sound("assets/sounds/lose.wav")
        sound.set_volume(0.1)
        sound.play()
        stats.run = False


def lose(screen, dino, color, screen_image, cactuses, pteros, stats):
    dino.lose()
    draw_screen(screen, screen_image, color, dino, cactuses, pteros, stats)
    font = pygame.font.SysFont("times new roman", 30)
    game_over_txt = font.render("YOU DIED! Press Enter to play again", True, color)
    rect = game_over_txt.get_rect()
    rect.midbottom = screen.get_rect().center
    screen.blit(game_over_txt, rect)
    pygame.display.flip()


def move_dino(dino):
    if dino.queue_to_bend and dino.end_jumping():
        dino.bending = True
        dino.queue_to_bend = False
    elif dino.queue_to_jump and not dino.bending:
        dino.jumping = True
    if dino.bending:
        dino.bend()
    elif dino.jumping or not dino.end_jumping():
        dino.jump()


def create_and_remove_enemies(screen, cactuses, pteros, marios, stats):
    for cactus in cactuses.copy():
        if cactus.rect.right < 0:
            cactuses.remove(cactus)
    for ptero in pteros.copy():
        if ptero.rect.right < 0:
            pteros.remove(ptero)
    spawn_deltas = (1, 1.25, 1.5, 1.75) if stats.score < 250 else (1.25, 1.5, 1.75)
    if stats.time / 60 >= choice(spawn_deltas):
        if stats.score // 10 < 100:
            choice(easy_score)(screen, cactuses, pteros, marios, stats)
        elif stats.score // 10 < 250:
            choice(normal_score)(screen, cactuses, pteros, marios, stats)
        else:
            choice(hard_score)(screen, cactuses, pteros, marios, stats)
        stats.time = 0


def print_score(screen, stats, color):
    font = pygame.font.SysFont("times new roman", 25)
    score = font.render(stats.get_score(), True, color)
    rect = score.get_rect()
    screen_rect = screen.get_rect()
    rect.top = screen_rect.top
    rect.right = screen_rect.right - 5
    screen.blit(score, rect)


def print_record(screen, stats, color):
    if int(stats.get_record()) < stats.score // 10:
        stats.rewrite_record(stats.get_score())
    font = pygame.font.SysFont("times new roman", 25)
    score = font.render(f"HIGH SCORE: {stats.get_record()}", True, color)
    rect = score.get_rect()
    screen_rect = screen.get_rect()
    rect.top = screen_rect.top
    rect.left = screen_rect.centerx
    screen.blit(score, rect)


def pause(screen, screen_image, sprites_color, dino, cactuses, pteros, stats):
    dino.pause()
    screen_image.pause()
    draw_screen(screen, screen_image, sprites_color, dino, cactuses, pteros, stats)
    screen_image.move_background()
    font = pygame.font.SysFont("times new roman", 30)
    pause_txt = font.render("Paused! Press Enter to continue game", True, sprites_color)
    rect = pause_txt.get_rect()
    rect.midbottom = screen.get_rect().center
    screen.blit(pause_txt, rect)
    pygame.display.flip()
