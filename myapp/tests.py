from django.test import TestCase
from django.contrib.auth.models import User
from .models import Player

class PlayerTestCase(TestCase):
    def setUp(self):
        # テスト用のユーザーとプレイヤーを作成してみる
        user = User.objects.create_user(username='testuser', password='12345')
        Player.objects.create(user=user, name='Test Player', job='Warrior')

    def test_player_creation(self):
        # プレイヤーが正しく作成されたかテストを行う
        player = Player.objects.get(name='Test Player')
        self.assertEqual(player.user.username, 'testuser')
        self.assertEqual(player.job, 'Warrior')
