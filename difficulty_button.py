import pygame
from button import Button


class DifficultyButton(Button):
    def __init__(self, ai_game, msg):
        """難易度選択ボタンを初期化"""
        super().__init__(ai_game, msg)
        self.width, self.height = 140, 70
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen.get_rect().center
        self.font = pygame.font.SysFont(None, 48)
        self.difficulty = msg

        # 難易度によってボタンを設定
        if self.difficulty == "Easy":
            self.button_color = (0, 200, 0)
        elif self.difficulty == "Medium":
            self.button_color = (255, 200, 0)
        elif self.difficulty == "Difficult":
            self.button_color = (255, 0, 0)
        self._prep_msg(msg)