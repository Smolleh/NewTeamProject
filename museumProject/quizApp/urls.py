from django.urls import path
from .views import QuizListView, quizListCreateView, StartQuizView, SubmitQuizView, QuizEditView, QuizQuestionListCreateView, QuestionEditView


urlpatterns = [
    #moderator-only paths
    path("manage/", quizListCreateView.as_view()),
    path("manage/<int:pk>/", QuizEditView.as_view()),
    
    #can have any number of answers.
    #put request formart: 
    # {"question_text": "Where is Germany?",
    #   "answers": [
    #     {
    #     "answer_text": "Europe",
    #     "is_correct": true
    #     },
    #     {
    #     "answer_text": "Asia",
    #     "is_correct": false
    #     },
    #     {
    #     "answer_text": "Africa",
    #     "is_correct": false
    #     }
    # ]
    # }
    path("manage/<int:quiz_id>/questions/", QuizQuestionListCreateView.as_view()),
    path("manage/question/<int:pk>/", QuestionEditView.as_view()),

    #user accessible paths
    path("", QuizListView.as_view()),
    path("<int:pk>/start/", StartQuizView.as_view(), name="quiz-start"),
    
    #the key represents the result Id.
    #any unanswered quiz questions should not be submitted in the request
    #format of patch request :  
    #{ "answers": [
    #{"question_id": 1, "answer_id": 1},
    #{"question_id": 2, "answer_id": 6},
    #{"question_id": 3, "answer_id": 10}
    #]
    #}
    path("<int:quiz_id>/submit/", SubmitQuizView.as_view()),
]