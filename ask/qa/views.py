from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import Question, Answer


def home(request):
    template = 'home.html'
    limit = 10
        
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1

    paginator = Paginator(Question.objects.new(), limit)
    questions = paginator.page(page)
    context = {
        'questions': questions,
    }
    return render(request, template, context)


def popular(request):
    template = 'popular.html'
    limit = 10
        
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1

    paginator = Paginator(Question.objects.popular(), limit)
    questions = paginator.page(page)
    context = {
        'questions': questions,
    }
    return render(request, template, context)


def question(request, question_pk):
    template = 'question.html'
    question = get_object_or_404(Question, pk=question_pk)
    context = {
        'question': question,
    }

    return render(request, template, context)


def test(request, *args, **kwargs):
    return HttpResponse('OK')
