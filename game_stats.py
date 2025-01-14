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
        self.player_name = ""


    def reset_stats(self):
        """ゲーム中に変更される統計情報を初期化"""
        self.ship_limits = self.settings.ship_limit
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


    def save_scores(self):
        """名前とスコアを保存"""
        saved_scores = self.get_saved_scores()
        saved_scores.append({
            'player_name': self.player_name,
            'score': self.score
        })
        saved_scores.sort(key=lambda x: x['score'], reverse=True)
        path = Path('scores.json')
        with open(path, 'w') as file:
            json.dump(saved_scores, file, ensure_ascii=False, indent=4)


    def get_saved_scores(self):
        """スコアをファイルから取得"""
        path = Path('scores.json')
        if path.exists():
            with open(path, 'r') as file:
                return json.load(file)
        return []