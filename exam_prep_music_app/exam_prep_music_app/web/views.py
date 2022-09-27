from django.shortcuts import render


def show_homepage(request):
    context = {

    }

    return render(request, 'home-page.html', context)


def add_album(request):
    context = {

    }

    return render(request, 'crea', context)


def show_album(request):
    context = {

    }

    return render(request, '', context)


def edit_album(request):
    context = {

    }

    return render(request, '', context)


def delete_album(request):
    context = {

    }

    return render(request, '', context)


def show_profile(request):
    context = {

    }

    return render(request, '', context)


def delete_profile(request):
    context = {

    }

    return render(request, '', context)

