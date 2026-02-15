from django.db import models
from museumApp.models import Exhibit
from django.contrib.auth.models import User
import random

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    num_questions = models.IntegerField()
    passing_score = models.IntegerField()
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.num_questions]
    
        
    
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.question_text)
    
    def get_answers(self):
        return self.answer_set.all()
    
class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    
    
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    score = models.FloatField(default=0)
    completed = models.BooleanField(default = False)
    selected_question_ids = models.JSONField(default=list)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["quiz", "user"], name="one_attempt")]

    
    

    
    
    
    
    