from django.urls import path

from exam_prep_music_app.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),
]