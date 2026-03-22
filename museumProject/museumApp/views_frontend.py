from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rest_framework import request
from .models import *
from .forms import EditUserForm
from .decorators import curator_required
from django.contrib.auth.decorators import login_required
from quizApp.models import Quiz


# URLs to render actual HTML pages for the front end
@login_required
def exhibits(request):
    return render(request, "pages/exhibits.html", {})
@login_required
def bookmarkExhibit(request, exhibitId):
    exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
    userId = request.user
    BookMarks.objects.get_or_create(exhibitId=exhibit,userId=userId)
    return JsonResponse({'success': True})
@login_required
def bookmarkedExhibits(request):
        bookmarks = BookMarks.objects.filter(userId=request.user).select_related('exhibitId')
        exhibits = [i.exhibitId for i in bookmarks]
        form = EditUserForm(instance=request.user)
        return render(request, 'pages/bookmarks.html', {"exhibits": exhibits, "form": form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})
@login_required
def unbookmarkExhibit(request, exhibitId):
    if request.method == 'POST':
        BookMarks.objects.filter(exhibitId=exhibitId, userId=request.user).delete()
        return JsonResponse({'success': True})
    else: 
        return JsonResponse({'success': False})
   
@login_required
def single_exhibit(request,  exhibitId):
    exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)

    artefacts = Artefact.objects.filter(exhibitId=exhibit)
    ai_description = AiSystemDescription.objects.filter(exhibitId=exhibit).first()
    contributing_factors = ContributingFactors.objects.filter(exhibitId=exhibit).first()
    failures = FailureDescription.objects.filter(exhibitId=exhibit).first()
    lessons = LessonsLearned.objects.filter(exhibitId=exhibit).first()
    comments = Comments.objects.filter(exhibit=exhibit, isApproved=True)
    exhibit.viewNumber += 1
    exhibit.save()
    

    return render(request, "pages/single_exhibit.html", {
        "exhibit": exhibit,
        "artefacts": artefacts,
        "ai_description": ai_description,
        "contributing_factors": contributing_factors,
        "failures": failures,
        "lessons": lessons,
        "comments": comments,
    })


def home(request):
    return render(request, 'pages/home.html', {})


def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


@login_required
@curator_required
def curator_dashboard(request):
        exhibits = Exhibit.objects.all()
        return render(request, 'pages/curator_dashboard.html', {"exhibits": exhibits})

@login_required
@curator_required
def edit_system(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        ai_description = AiSystemDescription.objects.filter(exhibitId=exhibit).first()
        return render(request, 'pages/curator/edit_system.html',
                       {"exhibit": exhibit,
                        "ai_description":ai_description})

@login_required
@curator_required
def edit_lessons(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        lessons = LessonsLearned.objects.filter(exhibitId=exhibit).first()
        return render(request, 'pages/curator/edit_lessons.html',
                       {"exhibit": exhibit,
                        "lessons": lessons})

@login_required
@curator_required
def edit_failure(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        failures = FailureDescription.objects.filter(exhibitId=exhibit).first()
        return render(request, 'pages/curator/edit_failure.html',
                       {"exhibit": exhibit,
                        "failures": failures})

@login_required
@curator_required
def edit_factors(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        contributing_factors = ContributingFactors.objects.filter(exhibitId=exhibit).first()
        return render(request, 'pages/curator/edit_factors.html',
                       {"exhibit": exhibit,
                        "contributing_factors":contributing_factors})

@login_required
@curator_required
def edit_exhibit_detail(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        return render(request, 'pages/curator/edit_exhibit_detail.html',
                       {"exhibit": exhibit})

@login_required
@curator_required
def edit_artefact(request, exhibitId, artefactId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        artefact = get_object_or_404(Artefact, artefactId=artefactId)

        return render(request, 'pages/curator/edit_artefact.html',
                       {"exhibit": exhibit,
                        "artefact":artefact})


@login_required
@curator_required
def create_system(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        return render(request, 'pages/curator/create_system.html',
                       {"exhibit": exhibit})

@login_required
@curator_required
def create_lessons(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        return render(request, 'pages/curator/create_lessons.html',
                       {"exhibit": exhibit})

@login_required
@curator_required
def create_failure(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        return render(request, 'pages/curator/create_failure.html',
                       {"exhibit": exhibit})

@login_required
@curator_required
def create_factors(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        return render(request, 'pages/curator/create_factors.html',
                       {"exhibit": exhibit})

@login_required
@curator_required
def create_exhibit(request):
        return render(request,'pages/curator/create_exhibit.html', {"exhibit": None})

@login_required
@curator_required
def create_artefact(request, exhibitId):
        exhibit = get_object_or_404(Exhibit, exhibitId=exhibitId)
        return render(request, 'pages/curator/create_artefact.html',
                       {"exhibit": exhibit})

@login_required
def quiz(request): 
        quiz = Quiz.objects.all()
        return render(request, "pages/quiz.html", {"quiz": quiz})

@login_required
def single_quiz(request, quizId):
        quizzes = Quiz.objects.all()
        return render(request, "pages/single_quiz.html", {"quizId": quizId, "quizzes": quizzes})    


"""
def results(request,quizId ): 
    question = get_object_or_404(QuizzQuestion, questionId=quizId)
    return (response, "pags/options.html" )


def results(request,quizId ): 
    response = " "
    return Http404


def quiz(request, quizId):
    return render(request, 'pages/quiz.html', {})




"""

@login_required
@curator_required
def review_comments(request):
    incoming = Comments.objects.filter(isApproved=False)
    return render(request, 'pages/curator/review_comments.html', {'comments': incoming})

