# Generated by Django 4.2.7 on 2024-01-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_answer_dislike_like_profile_question_tag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='question',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
