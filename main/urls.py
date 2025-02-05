from django.urls import path
from . import views

app_name = 'main'  # Pour namespace des URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('formation/', views.formation, name='formation'),
    path('competences/', views.competences, name='competences'),
    path('experience/', views.experience, name='experience'),
    path('qualites/', views.qualites, name='qualites'),
    path('loisirs/', views.loisirs, name='loisirs'),
] 