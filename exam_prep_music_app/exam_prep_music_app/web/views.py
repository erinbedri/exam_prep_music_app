from django.shortcuts import render


def show_homepage(request):
    context = {

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
    context = {

    }

    return render(request, 'home-no-profile.html')


def show_profile(request):
    context = {

    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    context = {

    }

    return render(request, 'profile-delete.html', context)

