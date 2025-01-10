import pygame
import random
from pygame.sprite import Sprite


class Bell(Sprite):
    def __init__(self, ai_game):
        """ベルを初期化、開始時の位置を設定"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # ベルの画像を読み込み、サイズを取得
        self.image = pygame.image.load('images/bell.bmp')
        self.rect = self.image.get_rect()
        self.last_bell_time = 0
        self.initialize_bell()
        self.random_bell()


    def initialize_bell(self):
        """ゲーム中に変更される設定値を初期化"""
        self.screen_rect = self.screen.get_rect()
        self.rect.y = self.screen_rect.bottom + self.rect.height
        self.bell_active = False


    def random_bell(self):
        """ベルをランダムに配置"""
        current_time = pygame.time.get_ticks()
        self.bell_interval = random.randint(10000, 20000)
        if current_time - self.last_bell_time >= self.bell_interval:
            self.last_bell_time = pygame.time.get_ticks()
            self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
            self.rect.y = -self.rect.height
            self.y = float(self.rect.y)
            self.bell_active = True
        else:
            self.bell_active = False


    def update(self):
        """ベルを下に移動"""
        if self.bell_active:
            self.y += self.settings.bell_drop_speed
            self.rect.y = self.y


    def blitme(self):
        """ベルを現在位置に描画"""
        self.screen.blit(self.image, self.rect)