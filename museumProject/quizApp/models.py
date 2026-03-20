from django.db import models
from museumApp.models import Exhibit
from django.contrib.auth.models import User
from django_enum.fields import EnumField
import random

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    num_questions = models.IntegerField()
    passing_score = models.FloatField(default=0)
    max_points = models.IntegerField(default=10)
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
    points = models.IntegerField(default=0)
    completed = models.BooleanField(default = False)
    passed = models.BooleanField(default = False)
    selected_question_ids = models.JSONField(default=list)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["quiz", "user"], name="one_attempt")]
        
        
# class QuestionAttempt(models.Model):
#     result = models.ForeignKey(Result, on_delete = models.CASCADE, null=False)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, null= False)
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=False)
#     class Meta:
#         constraints = [models.UniqueConstraint(fields=["result", "question"], name="unique_question")]
    
    
    
class UserAchievements(models.Model):
    class Badges(models.IntegerChoices):
        NEWBIE = 0, "Newbie"
        BRONZE = 1, "Bronze"
        SILVER = 2, "Silver"
        GOLD = 3, "Gold"
        PLATINUM = 4, "Patinum"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="achievements")
    points = models.IntegerField(default=0)
    badge = models.IntegerField(choices=Badges.choices, default=Badges.NEWBIE)
    
        
    def add_points(self, points: int):
        """adds points to the user's points and updates their badge 
        
        kwargs:
        points (int) -- number of points to be added 
        
        """
        self.points += points
        
        #update badge
        p = self.points
        if(p<10): 
            self.badge = self.Badges.NEWBIE
        elif (p<30): 
            self.badge = self.Badges.BRONZE
        elif (p<70): 
            self.badge = self.Badges.SILVER
        elif (p<100): 
            self.badge = self.Badges.GOLD
        else:
            self.badge = self.Badges.PLATINUM

        self.save(update_fields=["badge", "points"])
    
    
    
    