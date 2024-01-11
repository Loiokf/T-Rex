from cactus import Cactus
from ptero import EarthPtero, MiddlePtero, AirPtero
from random import choice


def create_cactus(screen, group1, group2, stats):
    cactus = Cactus(screen, screen.get_rect().right, stats)
    cactus.draw()
    group1.add(cactus)


def create_two_cactuses(screen, group1, group2, stats):
    cactus1 = Cactus(screen, screen.get_rect().right, stats)
    cactus1.draw()
    group1.add(cactus1)
    cactus2 = Cactus(screen, screen.get_rect().right - 40, stats)
    cactus2.draw()
    group1.add(cactus2)


def create_ptero(screen, group1, group2, stats):
    ptero = choice((EarthPtero, MiddlePtero, AirPtero))(screen, screen.get_rect().right, stats)
    ptero.draw()
    group2.add(ptero)


def create_three_cactuses(screen, group1, group2, stats):
    cactus1 = Cactus(screen, screen.get_rect().right, stats)
    cactus1.draw()
    group1.add(cactus1)
    cactus2 = Cactus(screen, screen.get_rect().right - 40, stats)
    cactus2.draw()
    group1.add(cactus2)
    cactus3 = Cactus(screen, screen.get_rect().right - 80, stats)
    cactus3.draw()
    group1.add(cactus3)


def create_ptero_and_cactus(screen, group1, group2, stats):
    ptero = AirPtero(screen, screen.get_rect().right - 40, stats)
    ptero.draw()
    group2.add(ptero)
    cactus = Cactus(screen, screen.get_rect().right + 75, stats)
    cactus.draw()
    group1.add(cactus)


def create_ptero_and_two_cactuses(screen, group1, group2, stats):
    ptero = choice((MiddlePtero, AirPtero))(screen, screen.get_rect().right - 40, stats)
    ptero.draw()
    group2.add(ptero)
    cactus1 = Cactus(screen, screen.get_rect().right + 75, stats)
    cactus1.draw()
    group1.add(cactus1)
    cactus2 = Cactus(screen, screen.get_rect().right + 115, stats)
    cactus2.draw()
    group1.add(cactus2)


def create_ptero_and_cactus_only_jump(screen, group1, group2, stats):
    ptero = MiddlePtero(screen, screen.get_rect().right - 40, stats)
    ptero.draw()
    group2.add(ptero)
    cactus = Cactus(screen, screen.get_rect().right, stats)
    cactus.draw()
    group1.add(cactus)


def create_two_pteros(screen, group1, group2, stats):
    ptero_type = choice((EarthPtero, MiddlePtero, AirPtero))
    ptero1 = ptero_type(screen, screen.get_rect().right, stats)
    ptero1.draw()
    group2.add(ptero1)
    ptero2 = ptero_type(screen, screen.get_rect().right - 70, stats)
    ptero2.draw()
    group2.add(ptero2)


easy_score = [create_cactus,
              create_two_cactuses]

normal_score = [create_cactus,
                create_two_cactuses,
                create_ptero,
                create_two_pteros,
                create_ptero]

hard_score = [create_two_pteros,
              create_three_cactuses,
              create_ptero_and_two_cactuses,
              create_ptero_and_cactus,
              create_ptero_and_cactus_only_jump]
