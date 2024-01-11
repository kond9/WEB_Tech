from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Question, Answer, Like_for_question, Like_for_answer, Tag
import random


class Command(BaseCommand):
    help = 'Filling database with random data for questions and answers'

    def add_arguments(self, parser):
        parser.add_argument(
            'ratio', type=int
        )

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio']
        temp_data_ques = []
        temp_data_ans = []
        temp_data_tag = []
        temp_data_like_q = []
        temp_data_like_a = []
        temp_data_profile = []
        for i in range(ratio):
            user = User.objects.create_user(f'user-{i}')
            profile = Profile(user=user, nickname=f'nick-{i}cool', bio=f'I am user-{i}')
            tag = Tag(tag_name=f'tag{i}')

            temp_data_tag.append(tag)

            for j in range(10):
                q = Question(
                    question_title=f'What should I do, if I have {j} questions?',
                    question_text=f'Recently I had a problem. As soon as I sit down to work, there are working people around me who disturb me. '
                                  f'Because of this, I have {j} questions out of {10 * i + j} that exist on the Internet.',
                    author=profile
                )
                q.tags.add(tag)

                for k in range(9):
                    a = Answer(answer_text=f'I think that you just need to rest and all your (i * 10 + j) * 10 + k} questions out of all will go away)',
                               author=profile, question=q)

                    l = Like_for_question(profile=profile, question=q, value=random.choice([1 -1]))

                    q.count_of_likes += int(l.value)
                    q.count_of_answers += 1
                    profile.count_of_likes += int(l.value)

                    temp_data_like_q.append(l)

                    l2 = Like_for_answer(profile=profile, answer=a, value=random.choice([1, -1]))
                    a.count_of_likes += int(l2.value)

                    temp_data_like_a.append(l2)
                    temp_data_ans.append(a)
                print(f'question {i} created')

                temp_data_ques.append(q)

            temp_data_profile.append(profile)

        print('start')

        Profile.objects.bulk_create(temp_data_profile)
        Tag.objects.bulk_create(temp_data_tag)
        Question.objects.bulk_create(temp_data_profile)
        Answer.objects.bulk_create(temp_data_profile)
        Like_for_question.objects.bulk_create(temp_data_profile)
        Like_for_answer.objects.bulk_create(temp_data_profile)

        print('finish')