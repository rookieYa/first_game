import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """ 初始化飞船的位置 """
        self.screen = screen

        self.image = pygame.image.load("images/ship.bmp")

        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        
        self.rect.centery = self.screen_rect.centery

        self.rect.bottom = self.screen_rect.bottom

        self.move_right = False
        
        self.move_left = False

        self.move_up = False
        
        self.move_down = False

        self.ai_settings = ai_settings
        
        # 飞船属性中 存储小数值
        self.center_x = float(self.rect.centerx)

        self.center_y = float(self.rect.centery)

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """ 进行左右的更新移动 """
        self._ship_move_left_right()
        self._ship_move_up_down()
        self.rect.centerx = self.center_x
        
        self.rect.centery = self.center_y

    def _ship_move_left_right(self):
        """ 进行飞船的左右移动 """
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center_x -= self.ai_settings.ship_speed_factor
        # 从右边进去，左边出来
        if self.move_right and self.rect.right >= self.screen_rect.right:
            self.center_x = self.screen_rect.left
        # 从左边进去，右边出来
        if self.move_left and self.rect.left <= self.screen_rect.left:
            self.center_x = self.screen_rect.right
    
    def _ship_move_up_down(self):
        """ 进行飞船的上下移动 """
        if self.move_up and self.rect.top < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor
        if self.move_down and self.rect.bottom > self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor
        # 从上边进去，下边出来
        if self.move_up and self.rect.top >= self.screen_rect.bottom:
            self.center_y = self.screen_rect.top
        # 从下边进去，上边出来
        if self.move_down and self.rect.bottom <= self.screen_rect.top:
            self.center_y = self.screen_rect.bottom 