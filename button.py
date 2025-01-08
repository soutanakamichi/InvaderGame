import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        """ボタンの属性を初期化"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 180, 90
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """msgを画像に変換後、ボタン中央に配置"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def _update_msg_position(self):
        """ボタンが移動した場合、テキストの位置を更新"""
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """空白のボタンを描画後、メッセージを描画"""
        pygame.draw.rect(self.screen, self.button_color, self.rect, border_radius=20)
        self.screen.blit(self.msg_image, self.msg_image_rect)