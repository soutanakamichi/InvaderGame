import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        """自機を初期化、開始時の位置を設定"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 自機の画像を読み込み、サイズを取得
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """左右の移動フラグによって自機の位置を更新"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x


    def blitme(self):
        """自機を現在位置に描画"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """自機を画面中央に配置"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)