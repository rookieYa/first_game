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