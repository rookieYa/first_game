import game_functions as gf
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from game_state import GameState
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
    # 创建一个用于存储游戏统计信息的实例
    stats = GameState(ai_settings)

    ship = Ship(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, ship, aliens, stats, screen, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
