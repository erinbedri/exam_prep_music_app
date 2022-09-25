from django.shortcuts import render

from exam_prep_games_play_app.web.models import Profile


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def show_home(request):
    profile = get_profile()

    return render(request, 'home-page.html', {'profile': profile})


def show_dashboard(request):
    return render(request, 'dashboard.html')


def create_game(request):
    return render(request, 'create-game.html')


def show_game_details(request, pk):
    return render(request, 'details-game.html')


def edit_game(request, pk):
    return render(request, 'edit-game.html')


def delete_game(request, pk):
    return render(request, 'delete-game.html')


def create_profile(request):
    return render(request, 'create-profile.html')


def show_profile(request):
    return render(request, 'details-profile.html')


def edit_profile(request):
    return render(request, 'edit-profile.html')


def delete_profile(request):
    return render(request, 'delete-profile.html')



