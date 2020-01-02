class GameState():
    """ 跟踪游戏的统计信息 """

    def __init__(self, ai_settings):
        """ 初始化统计信息 """
        self.ai_settings = ai_settings
        # 游戏刚启动时为活跃状态，只有剩下的飞船大于0的时候才有效
        self.game_active = True
        self.reset_state()
    
    def reset_state(self):
        """ 初始化游戏运行期间，可能变化的统计信息 """
        self.ships_left = self.ai_settings.ship_limit
