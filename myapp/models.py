from django.db import models
from django.contrib.auth.models import User
import json

class WorldSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='world_setting')
    theme = models.CharField(max_length=100, help_text="世界観を決定します。例: サイバーパンク、中世")
    stage = models.CharField(max_length=100, help_text="ゲームの舞台を決定します。例: 洞窟、スラム")
    chaos_level = models.IntegerField(default=0, help_text="カオス度。0〜100までの整数で、どれだけ理不尽なことが起こるかを示します。")

    def __str__(self):
        return f"{self.theme} - {self.stage} - カオス度: {self.chaos_level}"

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    status = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    def initialize_status(self):
        # ステータスのデフォルト値を設定するメソッド
        default_status = {
            "STR": 0,
            "DEX": 0,
            "INT": 0,
            "AGI": 0,
            "LUCK": 0,
            "HP": 0,  # DEXの5倍で計算される、初期値は0
            "SAN": 100  # 最大値100で開始
        }
        self.status = json.dumps(default_status)
        self.save()

class GameState(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='game_state')
    current_stage = models.CharField(max_length=100, help_text="プレイヤーが現在いるステージ")
    # GMとユーザーのログを格納するprogressフィールド
    progress = models.JSONField(default=list, help_text="GMとユーザーの対話ログ")
    # アイテムの名前と個数を管理するインベントリ
    inventory = models.JSONField(default=dict, help_text="プレイヤーの持っているアイテムとその個数")

    def __str__(self):
        return f"ゲーム状況: {self.player.name}"
