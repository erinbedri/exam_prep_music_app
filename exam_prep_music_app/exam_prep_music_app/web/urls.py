from django.urls import path

from exam_prep_music_app.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),

    path('album/add/', views.add_album, name='add album page'),
    path('album/details/<int:id>/', views.show_album, name='show album details page'),
    path('album/edit/<int:id>/', views.edit_album, name='edit album page'),
    path('album/delete/<int:id>/', views.delete_album, name='delete album page'),

    path('profile/details/', views.show_profile, name='show profile details page'),
    path('profile/delete/', views.delete_profile, name='delete profile page'),
]
