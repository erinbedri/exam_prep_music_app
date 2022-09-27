from django.urls import path

from exam_prep_music_app.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),

    path('album/add/', views.add_album, name='add album page'),
    path('album/details/<int:pk>/', views.show_album, name='show album details page'),
    path('album/edit/<int:pk>/', views.edit_album, name='edit album page'),
    path('album/delete/<int:pk>/', views.delete_album, name='delete album page'),

    path('profile/create/', views.create_profile, name='create profile'),
    path('profile/details/', views.show_profile, name='show profile details page'),
    path('profile/delete/', views.delete_profile, name='delete profile page'),
]
