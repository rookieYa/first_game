import sys

from bullet import Bullet
from alien import Alien
from time import sleep
import pygame


def check_events(ai_settings, screen, aliens, stats, play_button, ship, bullets):
    """ 响应外部监听事件的 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_events(event, ai_settings, screen, ship, bullets, stats, aliens)
        elif event.type == pygame.KEYUP:
            check_up_events(event, ship)
        # 监控鼠标的输入
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, aliens, bullets, ship, stats, play_button, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, aliens, bullets, ship, stats, play_button, mouse_x, mouse_y):
    """ 在玩家单机play按钮的时候开始游戏"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        # 防止不停的刷新
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
            # 隐藏 鼠标的光标
            pygame.mouse.set_visible(False)
            ai_settings.initialize_dynamic_settings()
            start_game(stats, ai_settings, screen, aliens, bullets, ship)


def check_down_events(event, ai_settings, screen, ship, bullets, stats, aliens):
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
        if stats.game_active:
            fire_bullets(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        # 按下P的时候进行开始游戏
        if not stats.game_active:
            ai_settings.initialize_dynamic_settings()
            start_game(stats, ai_settings, screen, aliens, bullets, ship)


def start_game(stats, ai_settings, screen, aliens, bullets, ship):
    """ 开始游戏 """
    stats.reset_state()
    stats.game_active = True
    # 进行屏幕的初始化
    screen_init(ai_settings, screen, aliens, bullets, ship)


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


def update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button):
    """ 进行屏幕的更新"""
    screen.fill(ai_settings.bg_color)
    # 把子弹画出来
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    """  更新子弹的位置，并删除已经消失的子弹 """
    bullets.update()
    # 进行内存回收
    for bullet in bullets.copy():
        # 消失在屏幕外之后
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullets_aliens_collections(bullets, aliens, ai_settings, screen, ship)


def check_bullets_aliens_collections(bullets, aliens, ai_settings, screen, ship):
    """ 检查子弹和外星人的碰撞 """
    # 检查碰撞，碰撞成功之后进行消除
    collections = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 此时外星人已经被全部消灭
    if len(aliens) == 0:
        # 清空所有子弹，然后新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def update_aliens(ai_settings, ship, aliens, stats, screen, bullets):
    """ 更新外星人的位置 """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_boom(ai_settings, stats, screen, ship, aliens, bullets)
    # 外星人是不是到家了
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_boom(ai_settings, stats, screen, ship, aliens, bullets):
    """ 飞船被击毙的时候 """
    if stats.ships_left > 0:
        stats.ships_left -= 1
        screen_init(ai_settings, screen, aliens, bullets, ship)
        # 暂停
        sleep(0.5)
    else:
        # 暂停
        sleep(0.5)
        stats.game_active = False
        pygame.mouse.set_visible(True)


def screen_init(ai_settings, screen, aliens, bullets, ship):
    """ 进行屏幕的数据的初始化 """
    # 清屏
    aliens.empty()
    bullets.empty()
    # 创建外星人，同时初始化位置
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def fire_bullets(bullets, ai_settings, screen, ship):
    """ 发射子弹的逻辑 """
    # 创建子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人群 """
    alien = Alien(ai_settings, screen)
    # 一个外星人的宽度
    alien_width = alien.rect.width
    number_alien_x = get_number_aliens_x(ai_settings, alien_width)
    num_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 循环创建所有外星人
    for row_number in range(num_rows):
        for alien_num in range(number_alien_x):
            # 工厂模式生成一个个的外星人
            create_alien(ai_settings, screen, aliens, alien_num, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """ 计算每行可容纳多少个外星人 """
    # 创建一个外星人，并计算最多一行可以有多少个机器人
    # 外星人间距为为外星人宽度

    avaliable_spacebox_x = ai_settings.screen_width - 2 * alien_width

    number_alien_x = int(avaliable_spacebox_x / (2 * alien_width))

    return number_alien_x


def create_alien(ai_settings, screen, aliens, alien_num, row_number):
    """ 创建外星人 """
    # 工厂模式生成一个个的外星人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """ 计算屏幕可容纳的多少外星人 """
    avaliable_spacebox_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    num_rows = int(avaliable_spacebox_y / (2 * alien_height))

    return num_rows


def check_fleet_edges(ai_settings, aliens):
    """ 检查机群的位置 """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ 改变机群的位置先向下移动，再改变方向 """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    # 变向
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ 检查外星人群是不是到达了底部 """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 同样的重新开始游戏
            ship_boom(ai_settings, stats, screen, ship, aliens, bullets)
            break
    