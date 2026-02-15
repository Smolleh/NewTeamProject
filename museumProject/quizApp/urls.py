from django.urls import path
from .views import QuizListView, quizListCreateView, StartQuizView, SubmitQuizView, QuizEditView, QuizQuestionListCreateView, QuestionEditView


urlpatterns = [
    #moderator-only paths
    path("manage/", quizListCreateView.as_view()),
    path("manage/<int:pk>/", QuizEditView.as_view()),
    path("manage/<int:quiz_id>/questions/", QuizQuestionListCreateView.as_view()),
    path("manage/question/<int:pk>/", QuestionEditView.as_view()),

    #user accessible paths
    path("", QuizListView.as_view()),
    path("<int:pk>/start/", StartQuizView.as_view(), name="quiz-start"),
    path("<int:pk>/submit/", SubmitQuizView.as_view()),
]