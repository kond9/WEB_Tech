from django.contrib import admin
from .models import Question, Answer, Tag, Like_for_question, Like_for_answer, Profile
# Register your models here.
admin.site.register(Question),
admin.site.register(Answer),
admin.site.register(Tag),
admin.site.register(Like_for_question),
admin.site.register(Like_for_answer),
admin.site.register(Profile),