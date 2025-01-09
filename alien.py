import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        """エイリアンを初期化、開始時の位置を設定"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # エイリアンの画像を読み込み、サイズを取得
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.alien_limit = 0


    def check_edges(self):
        """エイリアンが画面端に衝突した場合、Trueを返す"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """エイリアンを右または左に移動"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x