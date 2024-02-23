from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import openai

@login_required
def home_view(request):
    # ホーム画面を表示
    return render(request, 'home.html')
    
    

@login_required
def game_session(request):
    if request.method == 'POST':
        player_input = request.POST.get('player_input')
        gm_response = generate_gm_response(player_input)
        # 応答をテンプレートに渡して表示
        return render(request, 'game_session.html', {'gm_response': gm_response})
    else:
        # ゲームセッションの初期画面を表示
        return render(request, 'game_session.html')

def generate_gm_response(player_input):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
      engine="ChatGTP-4-turbo-preview",
      prompt="",
      max_tokens=100
    )
    return response.choices[0].text.strip()
