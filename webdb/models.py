from django.db import models
from django.contrib.auth.models import User

genre_choice = [('Romance','Romance'),('Action','Action'),('Sci-Fi','Sci-Fi'),]
lang_choice = [('English','English'),('Hindi','Hindi'),('Bengali','Bengali')]
plat_choice = [('Youtube','Youtube'),('Netflix','Netflix'),('Hoichoi','Hoichoi')]


class GenreList(models.Model):
    choice = models.CharField(max_length=20)
    def __str__(self): return self.choice

class item(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers/")
    published = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField(GenreList)
    language = models.CharField(choices=lang_choice,max_length=20)
    platform = models.CharField(choices=plat_choice,max_length=10)
    link = models.URLField(default="https://notfound.com/notfound.html")
    def __str__(self): return self.title



class comment(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    published = models.DateTimeField(auto_now_add=True)

class rating(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

class watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

