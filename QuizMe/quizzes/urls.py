from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    create_quiz_view,
    create_que_view,
)

app_name = 'quizzes'

urlpatterns = [
    path('', QuizListView.as_view(), name="main-view"),
    path('create/', create_quiz_view, name="create-quiz-view"),
    path('createque/<pk>/', create_que_view, name="create-que-view"),
    path('<pk>/', quiz_view, name="quiz-view"),
    path('<pk>/data/', quiz_data_view, name="quiz-data-view"),
    path('<pk>/save/', save_quiz_view, name="save-view"),
]
