import math

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from app.models import Question, Answer, Tag, Profile
from django.views import generic


def paginate(objects_list, request, per_page=20):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page', 1)
    if str(page).isdigit() and int(page) <= int(math.ceil(len(objects_list) / per_page)):
        return paginator.page(page)
    return paginator.page(1)


# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': paginate(questions, request)})



def question(request, question_id):
    try:
        question_item = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")
    answers = Answer.objects.filter(question=question_item)
    return render(request, 'question.html', {'question': question_item, 'answers': paginate(answers, request, 30)})


def hot(request):
    questions = Question.objects.order_by('-count_of_likes')
    return render(request, 'hot.html', {'questions': paginate(questions, request)})


def tag(request, tag_name):
    questions_by_tag = Question.objects.filter(tags__tag_name=tag_name)
    return render(request, 'tag.html', {'questions': paginate(questions_by_tag, request), 'tag': tag_name})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')

