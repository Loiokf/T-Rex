import pygame


class Dino:
    jump_height = 24

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assets/images/running_dino1.png")
        self.image_num = 1
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = 30
        self.rect.bottom = self.screen_rect.bottom - 15
        self.down = float(self.rect.bottom)
        self.jumping = False
        self.jump_c = Dino.jump_height
        self.bending = False
        self.queue_to_jump = False
        self.queue_to_bend = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update_image(self):
        self.image = pygame.image.load(
            "assets/images/running_dino1.png") if self.image_num < 4 else pygame.image.load(
            "assets/images/running_dino2.png")
        self.image_num = self.image_num % 8 + 1

    def jump(self):
        if self.jump_c == Dino.jump_height:
            sound = pygame.mixer.Sound("assets/sounds/jump.wav")
            sound.set_volume(0.001)
            sound.play()
        if self.jump_c >= -Dino.jump_height:
            self.down -= self.jump_c / 2
            self.rect.bottom = self.down
            self.jump_c -= 1
            self.image = pygame.image.load("assets/images/dino.png")
        else:
            self.jump_c = Dino.jump_height

    def end_jumping(self):
        return Dino.jump_height == self.jump_c

    def lose(self):
        if self.bending:
            self.end_bend()
        self.image = pygame.image.load("assets/images/losing_dino.png")

    def restart(self, screen):
        # self.rect.bottom = self.screen_rect.bottom - 15
        # self.jump_c = Dino.jump_height
        # self.down = float(self.rect.bottom)
        # self.jumping = False
        # self.bending = False
        # self.image = pygame.image.load("assets/images/running_dino1.png")
        self.__init__(screen)
        self.draw()

    def bend(self):
        self.image = pygame.image.load(
            "assets/images/bending_dino1.png") if self.image_num < 4 else pygame.image.load(
            "assets/images/bending_dino2.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.bottom - 15
        self.rect.left = 30

    def end_bend(self):
        self.image = pygame.image.load("assets/images/dino.png")
        self.rect = self.image.get_rect()
        self.rect.left = 30
        self.rect.bottom = self.screen_rect.bottom - 15
        self.down = float(self.rect.bottom)
        self.jumping = False
        self.bending = False
        self.queue_to_bend = False

    def pause(self):
        if self.bending:
            self.end_bend()
