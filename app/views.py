from django.shortcuts import render
from django.core.paginator import Paginator

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'Long lorem ipsum {i}'
    } for i in range(160)
]


def paginate(objects, page, per_page=30):
    paginator = Paginator(objects, per_page)

    return paginator.page(page)


# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, page)})


def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'question.html', {'question': item})

def hot(request):
    page = request.GET.get('page', 1)
    return render(request, 'hot.html', {'questions': paginate(QUESTIONS, page)})

def tag(request, tag_name):
    page = request.GET.get('page', 1)
    return render(request, 'tag.html', {'questions': paginate(QUESTIONS, page), 'tag':tag_name})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def ask(request):
    return render(request, 'ask.html')



