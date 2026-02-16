from django.contrib import admin
from .models import *



class AnswerInLine(admin.TabularInline):
    model = Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    
admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)


