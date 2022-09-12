from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'JS'},
    {'id': 3, 'name': 'Java'},
]


def home(request):
    context = {'rooms': rooms}

    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None

    for r in rooms:
        if r['id'] == int(pk):
            room = r

    context = {'room': room}

    return render(request, 'base/room.html', context)
