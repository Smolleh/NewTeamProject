from django.shortcuts import render, get_object_or_404
from .models import *

def exhibits(request):
    exhibits = Exhibit.objects.all()
    return render(request, "pages/exhibits.html", {"exhibits": exhibits})


def single_exhibit(request,  exhibitId):
    exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)

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

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html', {})

def about(request):
    return render(request, 'pages/about.html', {})

def login(request):
    return render(request, 'pages/login.html', {})



def register(request):
    return render(request, 'pages/register.html', {})

def curator_dashboard(request):
        exhibits = Exhibit.objects.all()
        return render(request, 'pages/curator_dashboard.html', {"exhibits": exhibits})


def exhibit_detail(request):
        return render(request, 'pages/curator/exhibit_detail.html', {})

def ai(request):
        return render(request, 'pages/curator/ai.html', {})

def artefact(request):
        return render(request, 'pages/curator/artefact.html', {})

def factors(request):
        return render(request, 'pages/curator/factors.html', {})

def failure(request):
        return render(request, 'pages/curator/failure.html', {})

def lessons(request):
        return render(request, 'pages/curator/lessons.html', {})

def system(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        ai_description = AiSystemDescription.objects.filter(exhibit_id=exhibit).first()
        return render(request, 'pages/curator/system.html',
                       {"exhibit": exhibit,
                        "ai_description":ai_description})
"""
def results(request,quizId ): 
    question = get_object_or_404(QuizzQuestion, questionId=quizId)
    return (response, "pags/options.html" )


def results(request,quizId ): 
    response = " "
    return Http404



def quiz(request, quizId):
    return render(request, 'pages/quiz.html', {})

def results(request,quizId ): 
    question = get_object_or_404(QuizzQuestion, questionId=quizId)
    return (response, "pags/options.html" )


def results(request,quizId ): 
    response = " "
    return Http404



"""
