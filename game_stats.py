class GameStats:
    """跟踪游戏的统计信息。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings
        self.reset_status()

        # 游戏刚启动时处于活动状态。
        self.game_active = False

        # 从high_score.txt中读取high_score。
        with open('alien_invasion/high_score.txt') as file_object:
            self.high_score = int(file_object.read())


    def reset_status(self):
        """初始化在游戏运行期间有可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1