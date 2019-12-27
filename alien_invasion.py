import game_functions as gf
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    bullets = Group()
    aliens = Group()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
