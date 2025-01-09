import json
from pathlib import Path
import pygame


class GameStats:
    def __init__(self, ai_game):
        """統計情報を初期化"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.get_saved_high_score()


    def reset_stats(self):
        """ゲーム中に変更される統計情報を初期化"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.last_bullet_time = pygame.time.get_ticks()


    def get_saved_high_score(self):
        """ハイスコアをファイルから取得"""
        path = Path('high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0