import sys

import pygame


def check_events(ship):
    """ 响应外部监听事件的 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_up_events(event, ship)


def check_down_events(event, ship):
    """ 检查按键向下按 """
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_down = True
    elif event.key == pygame.K_DOWN:
        ship.move_up = True


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


def update_screen(ai_settings, screen, ship):
    """ 进行屏幕的更新"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()