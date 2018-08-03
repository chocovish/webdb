from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import itemlist, details, create,rateitem

urlpatterns = [
    path("", itemlist, name="list"),
    path('details/<pk>', details, name='details'),
    path('create/', create, name='create'),
    path('api/rate/<pk>/<value>/',rateitem,name='rateitem')

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
