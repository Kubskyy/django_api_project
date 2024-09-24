from django.urls import path
from . import views

urlpatterns = [
    path('toggle/<int:character_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('dashboard/', views.dashboard, name='dashboard'),
]