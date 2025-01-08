class GameStats:
    def __init__(self, ai_game):
        """統計情報を初期化"""
        self.high_score = 0
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False


    def reset_stats(self):
        """ゲーム中に変更される統計情報を初期化"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1