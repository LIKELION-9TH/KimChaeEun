from django.shortcuts import redirect, render
from .models import Category, Hobby, Home, About, Music, Portfolio, Profile, Comment
from django.utils import timezone

# Create your views here.
def index(request):

    # 가장 최근에 수정한 Home 인사말, 사진
    home = Home.objects.latest('updated')

    # 가장 최근 수정 프로필 
    about = About.objects.latest('updated')
    profile = Profile.objects.filter(about=about)   

    comments = Comment.objects.all()

    return render(request, 'index.html', {'home' : home, 'about' : about,'profile' : profile, 'comments':comments})

def comment(request):
    new_comment = Comment()
    new_comment.writer = request.POST['writer']
    new_comment.content = request.POST['content']
    new_comment.write_date = timezone.now()
    new_comment.save()

    return redirect('index')

def picture(request):
    pictures = Portfolio.objects.all()
    return render(request, 'my_pictures.html', {'pictures' : pictures})

def place(request):
    categories = Category.objects.all()
    return render(request, 'my_place.html', {'categories' : categories})


def hobby(request):
    hobbies = Hobby.objects.all()
    return render(request, 'my_hobby.html', {'hobbies' : hobbies})

def music(request):
    musics = Music.objects.all()
    return render(request, 'my_music.html', {'musics': musics})

