from django.shortcuts import render, redirect

from exam_prep_music_app.web.forms import CreateProfileForm
from exam_prep_music_app.web.models import Profile


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def show_homepage(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def add_album(request):
    context = {

    }

    return render(request, 'add-album.html', context)


def show_album(request):
    context = {

    }

    return render(request, 'album-details.html', context)


def edit_album(request):
    context = {

    }

    return render(request, 'edit-album.html', context)


def delete_album(request):
    context = {

    }

    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    context = {

    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    context = {

    }

    return render(request, 'profile-delete.html', context)

