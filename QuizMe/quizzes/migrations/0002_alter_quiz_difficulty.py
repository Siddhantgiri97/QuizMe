# Generated by Django 3.2.2 on 2021-05-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Beginner'), ('medium', ' Intermediate'), ('hard', 'Advanced')], max_length=6),
        ),
    ]
