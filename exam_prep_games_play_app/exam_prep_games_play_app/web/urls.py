from django.urls import path

from exam_prep_games_play_app.web import views

urlpatterns = [
    path('', views.show_home, name='show home'),
    path('dashboard/', views.show_dashboard, name='show dashboard'),

    path('game/create/', views.create_game, name='create game'),
    path('game/details/<int:pk>', views.show_game_details, name='show game details'),
    path('game/edit/<int:pk>', views.edit_game, name='edit dame'),
    path('game/delete/<int:pk>', views.delete_game, name='delete dame'),

    path('profile/create/', views.create_profile, name='create profile'),
    path('profile/details/', views.show_profile, name='show profile'),
    path('profile/edit/', views.edit_profile, name='edit profile'),
    path('profile/delete/', views.delete_profile, name='delete profile'),
]

