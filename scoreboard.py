import pygame.font


class ScoreBoard():
    """ 现实得分信息信息的类 """

    def __init__(self, ai_settings, screen, stats):
        """ 初始化得分模版的各种得分属性 """
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示记分板上的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 将文本渲染成图片
        self.prep_score()
        # 渲染最高分
        self.prep_high_score()
        # 展示当前游戏等级
        self.prep_level()

    def prep_score(self):
        """ 进行 文字组件的渲染 """
        score_str = round(self.stats.score, -1)
        score_str = "{:,}".format(score_str)
        self.score_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # 找到放得分版的位置
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """ 在屏幕上显示得分"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score, self.high_score_rect)
        self.screen.blit(self.level_score, self.high_score_rect)
    
    def prep_high_score(self):
        """ 进行最高分的渲染 """
        score_str = round(self.stats.high_score, -1)
        score_str = "{:,}".format(score_str)
        self.high_score = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # 找到放得分版的位置
        self.high_score_rect = self.high_score.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """ 展示目前的游戏等级 """
        self.level_score = self.font.render(self.stats.level, True, self.text_color, self.ai_settings.bg_color)
        # 找到放得分版的位置
        self.level_score_rect = self.level_score.get_rect()
        self.level_score_rect.right = self.screen_rect.right
        self.level_score_rect.top = self.score_rect.bottom + 10