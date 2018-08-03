from django.contrib import admin
from .models import ItemModel,GenreList
# Register your models here.
admin.site.register(ItemModel)
admin.site.register(GenreList)