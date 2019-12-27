import sys

from bullet import Bullet
from alien import Alien
import pygame


def check_events(ai_settings, screen, ship, bullets):
    """ 响应外部监听事件的 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_up_events(event, ship)


def check_down_events(event, ai_settings, screen, ship, bullets):
    """ 检查按键向下按 """
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_down = True
    elif event.key == pygame.K_DOWN:
        ship.move_up = True
    elif event.key == pygame.K_SPACE:
        # 创建子弹
        fire_bullets(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_up_events(event, ship):
    """ 检查按键松开按 """
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_down = False
    elif event.key == pygame.K_DOWN:
        ship.move_up = False


def update_screen(ai_settings, screen, ship, alien, bullets):
    """ 进行屏幕的更新"""
    screen.fill(ai_settings.bg_color)
    # 把子弹画出来
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    """  更新子弹的位置，并删除已经消失的子弹 """
    bullets.update()
    # 进行内存回收
    for bullet in bullets.copy():
        # 消失在屏幕外之后
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullets(bullets, ai_settings, screen, ship):
    """ 发射子弹的逻辑 """
    # 创建子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """ 创建外星人群 """
    # 创建一个外星人，并计算最多一行可以有多少个机器人
    # 外星人间距为为外星人宽度
    alien = Alien(ai_settings, screen)
    # 一个外星人的宽度
    alien_width = alien.rect.width

    avaliable_spacebox_x = ai_settings.screen_width - 2 * alien_width

    number_alien_x = avaliable_spacebox_x / (2 * alien_width)

    # 循环创建所有外星人
    for alien_num in range(number_alien_x):
        # 工厂模式生成一个个的外星人
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_num