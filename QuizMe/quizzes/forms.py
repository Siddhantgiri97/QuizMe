from django import forms
from .import models
from quizzes.models import Quiz,Question, Answer


class CreateQuiz(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = '__all__'


class CreateQuestion(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = '__all__'


class CreateAnswer(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = '__all__'
