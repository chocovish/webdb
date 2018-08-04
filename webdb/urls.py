from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import itemlist, details, create, userprofile
from .apiviews import rateitem,addwatchlist

urlpatterns = [
    path("", itemlist, name="list"),
    path('details/<pk>', details, name='details'),
    path('create/', create, name='create'),
    path('api/rate/<pk>/<value>/',rateitem,name='rateitem'),
    path('api/addwatchlist/<pk>', addwatchlist, name='addwatchlist'),
    path('profile/', userprofile, name="userprofile"),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
