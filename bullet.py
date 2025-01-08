import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        """自機の現在位置から弾のオブジェクトを生成"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)


    def update(self):
        """画面上の弾を移動"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        """画面に弾を描画"""
        pygame.draw.rect(self.screen, self.color, self.rect)