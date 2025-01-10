import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    def __init__(self, ai_game):
        """得点を記録するための属性を初期化"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_difficulty()
        self.prep_ships()


    def prep_score(self):
        """得点を描画用の画像に変換"""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """ハイスコアを描画用の画像に変換"""
        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 90
        self.high_score_rect.top = self.score_rect.top


    def check_high_score(self):
        """新しいハイスコアを描画"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        """レベルを描画用の画像に変換"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.left + 190
        self.level_rect.top = self.score_rect.top


    def prep_difficulty(self):
        """難易度を描画用の画像に変換"""
        difficulty_str = str(self.settings.difficulty_level)
        self.difficulty_image = self.font.render(difficulty_str, True, self.text_color, self.settings.bg_color)
        self.difficulty_rect = self.score_image.get_rect()
        self.difficulty_rect.left = self.screen_rect.left + 20
        self.difficulty_rect.top = self.score_rect.top


    def prep_ships(self):
        """自機の残数を表示"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_limits):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(ship.image, (ship.image.get_width() // 2, ship.image.get_height() // 2))
            ship.rect = ship.image.get_rect()
            ship.rect.x = ship_number * ship.rect.width + 210
            ship.rect.y = self.score_rect.top
            self.ships.add(ship)


    def show_score(self):
        """画面に得点を描画"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.difficulty_image, self.difficulty_rect)
        self.ships.draw(self.screen)