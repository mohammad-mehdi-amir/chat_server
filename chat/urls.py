from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='conccet_to_chat'),
    path('', views.index, name='home'),
]