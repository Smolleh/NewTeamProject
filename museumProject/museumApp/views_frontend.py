from django.shortcuts import render, get_object_or_404
from .models import *

def exhibits(request):
    exhibits = Exhibit.objects.all()
    return render(request, "pages/exhibits.html", {"exhibits": exhibits})


def singleExhibit(request, exhibit_id):
    exhibit = get_object_or_404(Exhibit, exhibitId=exhibit_id)

    artefacts = Artefact.objects.filter(exhibitId=exhibit)
    ai_description = AiSystemDescription.objects.filter(exhibitId=exhibit).first()
    contributing_factors = ContributingFactors.objects.filter(exhibitId=exhibit).first()
    failures = FailureDescription.objects.filter(exhibitId=exhibit).first()
    lessons = LessonsLearned.objects.filter(exhibitId=exhibit).first()

    return render(request, "pages/single_exhibit.html", {
        "exhibit": exhibit,
        "artefacts": artefacts,
        "ai_description": ai_description,
        "contributing_factors": contributing_factors,
        "failures": failures,
        "lessons": lessons,
    })

def home(request):
    return render(request, 'pages/home.html', {})

"""

def quiz(request, quizId):
    return render(request, 'pages/quiz.html', {})

def results(request,quizId ): 
    question = get_object_or_404(QuizzQuestion, questionId=quizId)
    return (response, "pags/options.html" )


def results(request,quizId ): 
    response = " "
    return Http404



"""
