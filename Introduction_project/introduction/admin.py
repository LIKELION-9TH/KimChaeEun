from django.contrib import admin
from .models import Comment, Hobby, Home, About, Music, Profile, Category, Skills, Portfolio 

# Register your models here.
admin.site.register(Home)
admin.site.register(Hobby)
admin.site.register(Music)
admin.site.register(Comment)

# About 아직 이해못함
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

#Skills
class SkillInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
    ]

#Portfolio    
admin.site.register(Portfolio)
admin.site.register(Profile)

admin.site.register(Skills)
