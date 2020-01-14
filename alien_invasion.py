import game_functions as gf
import pygame

from settings import Settings
from ship import Ship
from button import Button
from game_state import GameState
from pygame.sprite import Group
from scoreboard import ScoreBoard


def run_game():
    pygame.init()
    ai_settings = Settings()
    bullets = Group()
    aliens = Group()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    # 创建并且绘制一个button
    play_button = Button(ai_settings, screen, "PLAY")
    # 创建一个用于存储游戏统计信息的实例

    ship = Ship(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameState(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    while True:
        gf.check_events(ai_settings, screen, aliens, stats, play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb)
            gf.update_aliens(ai_settings, ship, aliens, stats, screen, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)


run_game()
