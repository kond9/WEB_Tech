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
            user.save()

            profile = Profile(user=user, nickname=f'nick-{i}cool', bio=f'I am user-{i}')
            temp_data_profile.append(profile)

            tag = Tag(tag_name=f'tag{i}')
            temp_data_tag.append(tag)
        Profile.objects.bulk_create(temp_data_profile)
        Tag.objects.bulk_create(temp_data_tag)

        for i in range(ratio):
            profile = Profile.objects.get(id=(i + 1))

            for j in range(10):
                q = Question(
                    question_title=f'What should I do, if I have {10 * i + j} questions?',
                    question_text=f'Recently I had a problem. As soon as I sit down to work, there are working people around me who disturb me. '
                                  f'Because of this, I have {j} questions out of {10 * i + j} that exist on the Internet.',
                    author=profile
                )
                temp_data_ques.append(q)
                print(f'question {10 * i + j} created')
        Question.objects.bulk_create(temp_data_ques)

        temp_data_ques = []
        for i in range(ratio):
            profile = Profile.objects.get(id=(i + 1))
            for j in range(10):
                q = Question.objects.get(id=(10 * i + j + 1))
                for k in range(10):
                    a = Answer(
                        answer_text=f'I think that you just need to rest and all your {(i * 10 + j) * 10 + k} questions out of all will go away)',
                        author=profile, question=q)
                    temp_data_ans.append(a)
                    print(f'answer {(i * 10 + j) * 10 + k} created')

        Answer.objects.bulk_create(temp_data_ans)
        print('DATA BASE')

        temp_data_ans = []
        temp_data_profile = []
        f = 0
        for s in range(10):
            profile = Profile.objects.get(id=(s + 1))
            t = Tag.objects.get(id=(s + 1))
            for i in range(ratio):
                for j in range(10):
                    q = Question.objects.get(id=(10 * i + j + 1))
                    q.tags.add(t)

                    l = Like_for_question.objects.get(id=(s * ratio * 10 + 10 * i + j + 1))

                    q.count_of_likes += int(l.value)
                    q.count_of_answers += 1
                    profile.count_of_likes += int(l.value)
                    temp_data_like_q.append(l)
                    temp_data_ques.append(q)
                    for k in range(2):
                        a = Answer.objects.get(id=((i * 10 + j) * 10 + k + 1))
                        l2 = Like_for_answer.objects.get(id=(k + 1 + f))
                        a.count_of_likes += int(l2.value)
                        profile.count_of_likes += int(l2.value)

                        temp_data_ans.append(a)
                        temp_data_like_a.append(l2)
                        print(f'like {(i * 10 + j) * 10 + k} added')
                    f += 2

            Answer.objects.bulk_update(temp_data_ans, ['count_of_likes'], batch_size=999)
            temp_data_ans = []
            print('SOSO')
            Question.objects.bulk_update(temp_data_ques, ['count_of_likes', 'count_of_answers'], batch_size=999)
            temp_data_ques = []

            temp_data_profile.append(profile)
            Like_for_question.objects.bulk_create(temp_data_like_q)
            temp_data_like_q = []
            Like_for_answer.objects.bulk_create(temp_data_like_a)
            temp_data_like_a = []

            Profile.objects.bulk_update(temp_data_profile, ['count_of_likes'])
        # Question.objects.bulk_update(temp_data_ques, ['count_of_likes', 'count_of_answers'])
        # Answer.objects.bulk_update(temp_data_ans, ['count_of_likes'])
