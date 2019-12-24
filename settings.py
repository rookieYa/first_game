class Settings():
    """ 工厂模式管理所有的类 """

    def __init__(self):
        """ 初始化设置 """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的速度设置,默认移动1.5个像素
        self.ship_speed_factor = 1.5