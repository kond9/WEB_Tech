# Generated by Django 4.2.7 on 2024-01-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_user_like_for_answer_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_for_answer',
            name='value',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='like_for_question',
            name='value',
            field=models.IntegerField(blank=True),
        ),
    ]
