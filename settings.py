class Settings:
    def __init__(self):
        """ゲームの設定値を初期化"""
        # 画面の設定
        self.screen_width = 700
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # 自機の設定
        self.ship_limit = 2

        # 弾の設定
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullets_interval = 150

        # エイリアン艦隊の設定
        self.fleet_drop_speed = 10

        # ベルの設定
        self.bell_drop_speed = 5
        self.bell_points = 200

        # スピードアップの設定
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.difficulty_level = "medium"
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """ゲーム中に変更される設定値を初期化"""
        if self.difficulty_level == "easy":
            self.ship_limit = 3
            self.bullets_allowed = 6
            self.ship_speed = 4.0
            self.bullet_speed = 4.0
            self.alien_speed = 3.0
            self.alien_points = 25
        elif self.difficulty_level == "medium":
            self.ship_limit = 2
            self.bullets_allowed = 4
            self.ship_speed = 4.0
            self.bullet_speed = 4.0
            self.alien_speed = 3.0
            self.alien_points = 50
        elif self.difficulty_level == "difficult":
            self.ship_limit = 1
            self.bullets_allowed = 2
            self.ship_speed = 4.0
            self.bullet_speed = 4.0
            self.alien_speed = 3.0
            self.alien_points = 100
        self.fleet_direction = 1


    def increase_speed(self):
        """スピードアップ"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


    def set_difficulty(self, diff_setting):
        """難易度を設定"""
        if diff_setting == "easy":
            print("easy")
        elif diff_setting == "medium":
            print("medium")
        elif diff_setting == "difficult":
            print("difficult")