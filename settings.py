class Settings():
    """ 工厂模式管理所有的类 """

    def __init__(self):
        """ 初始化设置 """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的速度设置,默认移动1.5个像素
        self.ship_speed_factor = 1.5

        # 子弹的一些参数配置
        # 子弹的飞行速度要大于飞船的速度
        self.bullet_speed_factor = 2.5
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
    

