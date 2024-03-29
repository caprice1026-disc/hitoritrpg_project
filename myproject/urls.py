"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import home_view, game_start_view, world_setting_view

urlpatterns = [
    path("admin/", admin.site.urls),
    # 認証用URLの追加
    path('accounts/', include('django.contrib.auth.urls')),  
    # 認証用URLを追加
    path('', home_view, name='home'),
    path('game_start/', game_start_view, name='game_start'),
    path('world_setting/', world_setting_view, name='world_setting'),
]
