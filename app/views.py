import math

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'Long lorem ipsum {i}'
    } for i in range(40)
]


def paginate(objects_list, request, per_page=30):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page', 1)
    if str(page).isdigit() and int(page) <= int(math.ceil(len(objects_list) / per_page)):
        return paginator.page(page)
    return paginator.page(1)


# Create your views here.
def index(request):
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, request)})


def question(request, question_id):
    try:
        question = QUESTIONS[question_id]
    except:
        raise Http404("Question does not exist")
    item = QUESTIONS[question_id]
    item_for_answer = QUESTIONS[question_id]
    return render(request, 'question.html', {'question': item, 'answers': item_for_answer})


def hot(request):
    return render(request, 'hot.html', {'questions': paginate(QUESTIONS, request)})


def tag(request, tag_name):
    return render(request, 'tag.html', {'questions': paginate(QUESTIONS, request), 'tag': tag_name})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')
