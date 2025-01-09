import pygame
from pygame.sprite import Sprite
from alien import Alien


class AlienRed(Alien):
    def __init__(self, ai_game):
        """エイリアン（赤）を初期化"""
        super().__init__(ai_game)

        # エイリアン（赤）の画像を読み込み、サイズを取得
        self.image = pygame.image.load('images/alien_red.bmp')
        self.alien_limit = 1