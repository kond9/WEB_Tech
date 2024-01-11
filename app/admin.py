from django.contrib import admin
from .models import Question
from .models import Answer
from .models import Tag
from .models import Like_for_question
from .models import Like_for_answer
from .models import Profile
# Register your models here.
admin.site.register(Question),
admin.site.register(Answer),
admin.site.register(Tag),
admin.site.register(Like_for_question),
admin.site.register(Like_for_answer),
admin.site.register(Profile),