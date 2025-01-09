import json
import sys
from time import sleep
from pathlib import Path
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from difficulty_button import DifficultyButton
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    def __init__(self):
        """ゲームを初期化、ゲームのリソースを生成"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("エイリアン侵略")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play")
        self._create_difficulty_buttons()


    def run_game(self):
        """ゲームのメインループを開始"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)


    def _create_fleet(self):
        """エイリアン艦隊を生成"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # 横幅いっぱいからエイリアン一体分の余白を空けるための - (2 * alien_width)
        # 横幅いっぱいからエイリアン一体分の余白を空けるための // (2 * alien_width)
        # available_space_x = self.settings.screen_width - (2 * alien_width)
        # number_aliens_x = available_space_x // (2 * alien_width)
        available_space_x = self.settings.screen_width - (alien_width)
        number_aliens_x = available_space_x // (alien_width)
        ship_height = self.ship.rect.height

        # 縦幅いっぱいからエイリアン二体分の余白を空けるための - (3 * alien_height)
        # 縦幅いっぱいからエイリアン二体分の余白を空けるための // (2 * alien_height)
        # available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        # number_rows = available_space_y // (2 * alien_height)
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """エイリアンを生成後、エイリアン艦隊の中に配置"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # エイリアン同士の並びから一体分の余白を空けるための 2 * alien_width
        # alien.x = alien_width + 2 * alien_width * alien_number
        alien.x = alien_width + alien_width * alien_number
        alien.rect.x = alien.x

        # エイリアン同士の並びから一体分の余白を空けるための 2 * alien.rect.height
        # alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.y = alien.rect.height + alien.rect.height * row_number
        self.aliens.add(alien)


    def _create_difficulty_buttons(self):
        """難易度選択ボタンを生成"""
        self.easy_button = DifficultyButton(self, "Easy")
        self.medium_button = DifficultyButton(self, "Medium")
        self.difficult_button = DifficultyButton(self, "Difficult")

        # 重ならないようにボタンを配置
        self.medium_button.rect.top = (self.play_button.rect.top + 1.5 * self.play_button.rect.height)
        self.easy_button.rect.top = self.medium_button.rect.top
        self.difficult_button.rect.top = self.medium_button.rect.top
        button_spacing = 150
        self.medium_button.rect.centerx = self.play_button.rect.centerx
        self.easy_button.rect.centerx = self.medium_button.rect.centerx - button_spacing
        self.difficult_button.rect.centerx = self.medium_button.rect.centerx + button_spacing
        self.easy_button._update_msg_position()
        self.medium_button._update_msg_position()
        self.difficult_button._update_msg_position()


    def _check_events(self):
        """キーボードとマウスのイベントを判定"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_buttons(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _close_game(self):
        """ハイスコアを保存して終了"""
        saved_high_score = self.stats.get_saved_high_score()
        if self.stats.high_score > saved_high_score:
            path = Path('high_score.json')
            contents = json.dumps(self.stats.high_score)
            path.write_text(contents)
        sys.exit()


    def _check_play_button(self, mouse_pos):
        """Playボタンのクリックによって新規ゲームを開始"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()


    def _start_game(self):
        """新規ゲームを開始"""
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_difficulty()
        self.sb.prep_ships()
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)


    def _check_difficulty_buttons(self, mouse_pos):
        """難易度選択ボタンのクリックによって難易度を設定"""
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        diff_button_clicked = self.difficult_button.rect.collidepoint(mouse_pos)
        if easy_button_clicked:
            self.settings.difficulty_level = "easy"
        elif medium_button_clicked:
            self.settings.difficulty_level = "medium"
        elif diff_button_clicked:
            self.settings.difficulty_level = "difficult"
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.sb.prep_difficulty()
        self.sb.prep_ships()


    def _check_keydown_events(self, event):
        """キーを押すイベント"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._close_game()
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()


    def _check_keyup_events(self, event):
        """キーを離すイベント"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """新しい弾を生成後、bulletsグループに追加"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        # 弾の発射後に衝突判定
        self._check_bullet_alien_collisions()


    def _update_bullets(self):
        """弾の位置を更新後、画面外の弾を廃棄"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # 弾が移動するたびに衝突判定
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """弾とエイリアンの衝突を判定"""
        # 引数をFalseにすれば、二回以上の衝突で消えるエイリアン、貫通弾にパワーアップするアイテムなど実装可能
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # 衝突時の追加処理
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        # エイリアン艦隊を撃破するたびに弾を廃棄後、新しいエイリアン艦隊を生成
        if not self.aliens:
            self._start_new_level()


    def _start_new_level(self):
        """エイリアン艦隊を撃破後、新しいレベルを開始"""
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
        self.stats.level += 1
        self.sb.prep_level()


    def _update_aliens(self):
        """エイリアン艦隊と画面端の衝突を判定後、エイリアンの位置を更新"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        """エイリアンの画面端の処理"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """エイリアン艦隊を下に移動後、横移動の方向を変更"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_aliens_bottom(self):
        """エイリアンと画面下の衝突を判定"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _ship_hit(self):
        """エイリアンと自機の衝突を判定"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _update_screen(self):
        """画面上の画像を更新後、新しい画面に更新"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        # ゲームが非アクティブ状態のときにボタンを描画
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.difficult_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    """ゲームのインスタンスを生成後、ゲームを実行"""
    ai = AlienInvasion()
    ai.run_game()