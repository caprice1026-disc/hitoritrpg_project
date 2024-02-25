from django import forms
from .models import WorldSetting

class WorldSettingForm(forms.ModelForm):
    class Meta:
        model = WorldSetting
        fields = ['theme', 'stage', 'chaos_level']  # userフィールドは除外
        labels = {
            'theme': '世界観',
            'stage': '舞台',
            'chaos_level': 'カオス度',
        }