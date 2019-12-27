import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ 工厂模式管理飞船发射出去的子弹 """
    def __init__(self, ai_settings, screen, ship):
        # 设置一个子弹对象
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 相同的道理，用一个数承接小数部分
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ 向上移动子弹 """
        self.y -= self.speed_factor
        # 移动完之后更新位置
        self.rect.y = self.y
    
    def draw_bullet(self):
        """ 进行子弹的绘制 """
        pygame.draw.rect(
            self.screen, self.color, self.rect
        )
