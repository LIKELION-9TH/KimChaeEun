from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=20)
    greetings_2 = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='picture/', blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

#Meta 왜쓰는 거였더라?!
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    skill_name = models.CharField(max_length=20)


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

#아직 이해못했지만 일단 따라함
    def __str__(self):
        return f'Portfolio {self.id}'


class Hobby(models.Model):
    image = models.ImageField(upload_to='Hobby/')
    name = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.name


class Music(models.Model):
    image = models.ImageField(upload_to='Music/', blank='True')
    singer = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    link = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    writer = models.CharField(max_length=20)
    write_date = models.DateTimeField()
    content = models.TextField(blank=False)
