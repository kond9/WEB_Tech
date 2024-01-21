from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#class QuestionManager(models.Manager):

class QuestionQuerySet(models.QuerySet):
    def get_latest_questions(self):
        return self.order_by('-pub_date')
    def get_best_questions(self):
        return self.order_by('-count_of_likes')
    def get_questions_by_tag(self, question_tag):
        return self.filter(tags__tag_name=question_tag)
    def get_question_by_pk(self, question_pk):
        return self.get(pk=question_pk)
class QuestionManager(models.Manager):
    def get_queryset(self):
        return QuestionQuerySet(self.model)
    def get_latest_questions(self):
        return self.get_queryset().get_latest_questions()
    def get_best_questions(self):
        return self.get_queryset().get_best_questions()
    def get_questions_by_tag(self, question_tag):
        return self.get_queryset().get_questions_by_tag(question_tag)
    def get_question_by_pk(self, question_pk):
        return self.get_queryset().get_question_by_pk(question_pk)

class AnswerQuerySet(models.QuerySet):
    def get_answers_by_id(self, question_id):
        return self.filter(question=question_id)
class AnswerManager(models.Manager):
    def get_queryset(self):
        return AnswerQuerySet(self.model)
    def get_answers_by_id(self, question_id):
        return self.get_queryset().get_answers_by_id(question_id)
class Question(models.Model):
    question_title = models.CharField(max_length=255)
    question_text = models.TextField(blank=True)
    author = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')
    count_of_answers = models.IntegerField(default=0)
    count_of_likes = models.IntegerField(default=0)

    objects=models.Manager()
    mymanager=QuestionManager()

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    answer_text = models.CharField(max_length=255)
    author = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    count_of_likes = models.IntegerField(default=0)
    correct_answers = models.BooleanField(default=False)

    objects=models.Manager()
    mymanager=AnswerManager()
    def __str__(self):
        return self.answer_text


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Like_for_question(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey('Question', related_name='like_for_ques', on_delete=models.CASCADE)
    value = models.IntegerField(blank=True)


class Like_for_answer(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey('Answer', related_name='like_for_ans', on_delete=models.CASCADE)
    value = models.IntegerField(blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True)
    birthDate = models.DateField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    count_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
