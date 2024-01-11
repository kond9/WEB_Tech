from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    question_title = models.CharField(max_length=255)
    question_text = models.TextField(blank=True)
    author = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')
    count_of_answers = models.IntegerField(default=0)
    count_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_title

class Answer(models.Model):
    answer_text = models.CharField(max_length=255)
    author = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField('date published')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    count_of_likes = models.IntegerField(default=0)
    correct_answers = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Like_for_question(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey('Question', related_name='like_for_ques', on_delete=models.CASCADE)
    value = models.CharField(max_length=2, blank=True)


class Like_for_answer(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey('Answer', related_name='like_for_ans', on_delete=models.CASCADE)
    value = models.CharField(max_length=2, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True)
    birthDate = models.DateField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    count_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
