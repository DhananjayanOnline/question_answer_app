# Generated by Django 4.1.2 on 2022-12-15 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_remove_likes_answers_remove_likes_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='describtion',
            field=models.CharField(max_length=2000),
        ),
    ]
