from django.apps import AppConfig


class QuizAppConfig(AppConfig):
    name = 'quizApp'
    
    def ready(self):
        import quizApp.signals

