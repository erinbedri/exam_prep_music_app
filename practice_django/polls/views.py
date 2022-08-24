from django.shortcuts import render

from django.http import HttpResponse, Http404

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_questions
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question': question
        }
    except Question.DoesNotExist:
        raise Http404('Question does now exist')

    return render(request, 'polls/details.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
