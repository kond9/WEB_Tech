import math

from django.contrib import auth
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404


from .models import Question, Answer, Tag, Profile, QuestionManager
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.urls import reverse

def paginate(objects_list, request, per_page=20):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page', 1)
    if str(page).isdigit() and int(page) <= int(math.ceil(len(objects_list) / per_page)):
        return paginator.page(page)
    return paginator.page(1)


# Create your views here.
def index(request):
    questions = Question.mymanager.get_latest_questions()
    return render(request, 'index.html', {'questions': paginate(questions, request)})



def question(request, question_id):
    try:
        question_item = Question.mymanager.get_question_by_pk(question_id)
    except:
        raise Http404("Question does not exist")
    answers = Answer.mymanager.get_answers_by_id(question_item)
    return render(request, 'question.html', {'question': question_item, 'answers': paginate(answers, request, 30)})


def hot(request):
    questions = Question.mymanager.get_best_questions()
    return render(request, 'hot.html', {'questions': paginate(questions, request)})


def tag(request, tag_name):
    questions_by_tag = Question.mymanager.get_questions_by_tag(tag_name)
    return render(request, 'tag.html', {'questions': paginate(questions_by_tag, request), 'tag': tag_name})


def log_in(request):
    print(request.GET)
    print(request.POST)
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print('Successfully logged in')
            return redirect(reverse('index'))
    return render(request, 'login.html')

def log_out(request):
    auth.logout(request)
    return redirect(reverse('login'))

def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')

