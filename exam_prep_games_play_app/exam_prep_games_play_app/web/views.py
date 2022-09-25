from django.shortcuts import render, redirect

from exam_prep_games_play_app.web.forms import CreateProfileForm
from exam_prep_games_play_app.web.models import Profile, Game


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def show_home(request):
    profile = get_profile()

    return render(request, 'home-page.html', {'profile': profile})


def show_dashboard(request):
    games = Game.objects.all()

    return render(request, 'dashboard.html', {'games': games})


def create_game(request):
    return render(request, 'create-game.html')


def show_game_details(request, pk):
    return render(request, 'details-game.html')


def edit_game(request, pk):
    return render(request, 'edit-game.html')


def delete_game(request, pk):
    return render(request, 'delete-game.html')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def show_profile(request):
    return render(request, 'details-profile.html')


def edit_profile(request):
    return render(request, 'edit-profile.html')


def delete_profile(request):
    return render(request, 'delete-profile.html')



