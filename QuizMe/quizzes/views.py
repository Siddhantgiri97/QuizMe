from django.shortcuts import render, redirect
from .models import Quiz, Question, Answer
from django.views.generic import ListView
from django.http import JsonResponse
from results.models import Result
from .import forms
# Create your views here.


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/main.html'


def create_quiz_view(request):
    if request.method == 'POST':
        form = forms.CreateQuiz(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            # instance.author = request.user
            instance.save()
            return redirect('quizzes:main-view')
    else:
        form = forms.CreateQuiz()
    return render(request, 'quizzes/create_quiz.html', {'form': form})


def create_que_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.CreateQuestion(request.POST, request.FILES)
        if form.is_valid():
            question = Question.objects.create(
                question=question, instance=quiz)
            for a, c in zip(text, correct):
                answer = Answer.objects.create(text=a, correct=c)
                question.save()
                quiz.save()

            return redirect('quizzes:main-view')
    else:
        form = forms.CreateQuestion()
    return render(request, 'quizzes/create_que.html', {'form': form})


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizzes/quiz.html', {'obj': quiz})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.no_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append(
                    {str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})
