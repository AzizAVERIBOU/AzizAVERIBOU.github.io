from django.contrib import admin
from .models import PersonalInfo, Experience, Education, Skill, PersonalQuality, Hobby

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')
    search_fields = ('name', 'email')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date')
    list_filter = ('company',)
    search_fields = ('position', 'company')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'field', 'institution', 'start_date', 'end_date')
    search_fields = ('degree', 'institution')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_filter = ('level',)

@admin.register(PersonalQuality)
class PersonalQualityAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)
