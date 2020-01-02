import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ 表示的是机器人的类 """

    def __init__(self, ai_settings, screen):
        """ 初始化外星人的位置和基本设置图片 """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 设置初始化的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储精确的位置
        self.x = float(self.rect.x)

    def blitme(self):
        """ 指定位置绘画外星人 """
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """ 根据方向不同指引外星人的移动速度"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        """ 检查屏幕边缘如果处于边缘返回 true """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False