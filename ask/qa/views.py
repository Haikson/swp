from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import Question, Answer
from forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import authenticate, login as dlogin, logout as dlogout


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
    user = request.user

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            user = request.user
            if not user.is_authenticated():
                return redirect('login')
            answer = answer_form.save(user=user)
            #return redirect('question', question.pk)
    else:
        answer_form = AnswerForm(initial={'question': question.pk})

    context = {
        'user': user,
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
                return redirect('login')
            question = ask_form.save(user=user)
            return redirect('question', question.pk)
    else:
        ask_form = AskForm()

    context = {
        'ask_form': ask_form,
    }

    return render(request, template, context)


def signup(request):
    template = 'signup.html'
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            data = signup_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                dlogin(request, user)
                return redirect('home')
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, template, context)


def login(request):
    template = 'login.html'
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                dlogin(request, user)
                return redirect('home')
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }
    return render(request, template, context)

def logout(request):
    dlogout(request)
    return redirect('home')

def test(request, *args, **kwargs):
    return HttpResponse('OK')
