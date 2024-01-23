import math

from django.contrib import auth
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404

from .forms import LoginForm, RegisterForm, QuestionForm
from .models import Question, Answer, Tag, Profile, QuestionManager
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def paginate(objects_list, request, per_page=20):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page', 1)
    if str(page).isdigit() and int(page) <= int(math.ceil(len(objects_list) / per_page)):
        return paginator.page(page)
    return paginator.page(1)


# Create your views here.
@login_required(login_url='log_in/', redirect_field_name='continue')
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
    if request.method == 'GET':
        login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request, **login_form.cleaned_data)
            print(user)
            if user is not None:
                login(request, user)
                print('Successfully logged in')
                return redirect(request.GET.get('continue', '/'))
            else:
                login_form.add_error(None, "Wrong password or user does not exist.")
    return render(request, 'login.html', context={"form": login_form})


def log_out(request):
    auth.logout(request)
    return redirect(reverse('login'))


def signup(request):
    print(request.GET)
    print(request.POST)
    if request.method == 'GET':
        user_form = RegisterForm()
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            print('qq')
            user = user_form.save()
            print(user)

            if user:
                return redirect(reverse('index'))
            else:
                user_form.add_error(None, "User saving error!")
    return render(request, 'signup.html', context={"form": user_form})


def ask(request):
    print(request.GET)
    print(request.POST)
    if request.method == 'GET':
        question_form = QuestionForm()
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            print('qq')

            question_form.save()
            return render(request, 'ask.html')
            # else:
            #     question_form.add_error(None, "Question saving error!")
    return render(request, 'ask.html', context={"form": question_form})
    # if request.method == 'POST':
    #     question_title=request.POST['title']
    #     question_text=request.POST['text']
    #     tags=request.POST['tags']
    #     print(question_title, question_text, tags)
    # return render(request, 'ask.html')



def settings(request):
    return render(request, 'settings.html')
