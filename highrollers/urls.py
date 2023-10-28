"""
URL configuration for highrollers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from .GameManager import GameManager

from . import views

game_manager = GameManager()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.draw_page, {"game":'test'}),
    path('api/test/', game_manager.handle_client_message, {"game":'test'}),
    path('blackjack/', views.draw_page, {"game":'blackjack'}),
    path('api/blackjack/', game_manager.handle_client_message, {"game":'blackjack'}),
]
