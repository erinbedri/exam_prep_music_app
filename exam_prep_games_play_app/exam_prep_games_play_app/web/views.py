from django.shortcuts import render, redirect

from exam_prep_games_play_app.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm
from exam_prep_games_play_app.web.models import Profile, Game


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def show_home(request):
    profile = get_profile()

    return render(request, 'home-page.html', {'profile': profile})


def show_dashboard(request):
    profile = get_profile()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }

    return render(request, 'dashboard.html', context)


def create_game(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = CreateGameForm()

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-game.html', context)


def show_game_details(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)

    context = {
        'profile': profile,
        'game': game,
    }

    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = EditGameForm(instance=game)

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            game.delete()
            return redirect('show dashboard')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'delete-game.html', context)


def create_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def show_profile(request):
    profile = get_profile()
    games_count = len(Game.objects.all())
    average_game_rating = sum([g.rating for g in Game.objects.all()])

    context = {
        'profile': profile,
        'games_count': games_count,
        'average_game_rating': average_game_rating,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)



