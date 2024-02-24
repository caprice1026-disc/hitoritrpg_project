from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Player, GameState, WorldSetting
from openai import OpenAI
import os

client = OpenAI()

@login_required
def home_view(request):
    # ホーム画面を表示
    return render(request, 'home.html')

@login_required
def game_start_view(request):
    user = request.user
    
    # プレイヤーとそのゲーム状態を取得（存在しない場合は作成）
    player, _ = Player.objects.get_or_create(user=user)
    game_state, created = GameState.objects.get_or_create(player=player)
    
    # セッションが既に存在し、かつゲームオーバー/クリアでない場合は、ゲーム画面にリダイレクト。これはif game_state.is_overの部分に合わせる
    if not created and not game_state.is_over:
        return redirect('game_play')  # 'game_play'はゲームプレイ画面のURL名
    '''
    # セッションでゲームオーバーまたはゲームクリアが発生した場合、セッションをリセット。この部分はgame_playビューに実装するのがよさそう。
    if game_state.is_over:
        # 必要に応じてゲーム状態のリセット処理をここに実装すること。
        # 例: game_state.reset()
    '''
    # 新しいゲームセッションを開始するための準備（世界観選択など）
    return redirect('world_setting')  # 世界観設定やプレイヤー設定画面のURL名

@login_required
def world_setting_view(request):
    if request.method == 'POST':
        # フォームからの入力を処理するようにする
        # 世界観設定とプレイヤー設定を保存するようにする
        return redirect('game_main')  # ゲームのメイン画面にリダイレクト
    else:
        # 世界観選択とプレイヤー設定フォームを表示
        return render(request, 'world_setting.html')
