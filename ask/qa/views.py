from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import Question, Answer
from forms import AskForm, AnswerForm


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

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)

        if answer_form.is_valid():
            user = request.user
            if not user.is_authenticated():
                user = None
            answer = answer_form.save(user=user)
            #return redirect('question', question.pk)
    else:
        answer_form = AnswerForm(initial={'question': question.pk})

    context = {
        'question': question,
        'answer_form': answer_form,
    }

    return render(request, template, context)


def ask(request):
    template = 'ask.html'

    if request.method == 'POST':
        ask_form = AskForm(request.POST)

        if ask_form.is_valid():
            user = request.user
            if not user.is_authenticated():
                user = None
            question = ask_form.save(user=user)
            return redirect('question', question.pk)
    else:
        ask_form = AskForm()

    context = {
        'ask_form': ask_form,
    }

    return render(request, template, context)



def test(request, *args, **kwargs):
    return HttpResponse('OK')
