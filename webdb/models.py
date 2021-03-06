from django.db import models
from django.contrib.auth.models import User

#genre_choice = [('Romance','Romance'),('Action','Action'),('Sci-Fi','Sci-Fi'),]
lang_choice = [('English','English'),('Hindi','Hindi'),('Bengali','Bengali')]
plat_choice = [('Youtube','Youtube'),('Netflix','Netflix'),('Hoichoi','Hoichoi')]


class GenreList(models.Model):
    choice = models.CharField(max_length=20)
    def __str__(self): return self.choice


class ItemModel(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers/")
    published = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField(GenreList)
    language = models.CharField(choices=lang_choice,max_length=20)
    platform = models.CharField(choices=plat_choice,max_length=10)
    link = models.URLField(default="https://notfound.com/notfound.html")
    rating = models.DecimalField(decimal_places=2,max_digits=4,default=0)
    ratingcount = models.IntegerField(default=0)
    def __str__(self): return self.title



class CommentModel(models.Model):
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    published = models.DateTimeField(auto_now_add=True)


class RatingModel(models.Model):
    item = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

