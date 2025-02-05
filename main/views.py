from django.shortcuts import render
from .models import PersonalInfo, Experience, Education, Skill, PersonalQuality, Hobby

def home(request):
    context = {
        'personal_info': PersonalInfo.objects.first(),
    }
    return render(request, 'main/home.html', context)

def formation(request):
    context = {
        'education': Education.objects.all().order_by('-start_date'),
        'personal_info': PersonalInfo.objects.first(),
    }
    return render(request, 'main/formation.html', context)

def competences(request):
    context = {
        'skills': Skill.objects.all(),
        'personal_info': PersonalInfo.objects.first(),
    }
    return render(request, 'main/competences.html', context)

def experience(request):
    context = {
        'experiences': Experience.objects.all().order_by('-start_date'),
        'personal_info': PersonalInfo.objects.first(),
    }
    return render(request, 'main/experience.html', context)

def qualites(request):
    context = {
        'personal_info': PersonalInfo.objects.first(),
        'qualities': PersonalQuality.objects.all(),
    }
    return render(request, 'main/qualites.html', context)

def loisirs(request):
    context = {
        'personal_info': PersonalInfo.objects.first(),
        'hobbies': Hobby.objects.all(),
    }
    return render(request, 'main/loisirs.html', context)
