from django.http import JsonResponse
from django.db.models import Avg

from .models import ItemModel,RatingModel,WatchList



def rateitem(request,pk,value):
    if request.user.is_authenticated:
        item = ItemModel.objects.get(pk=pk)
        value = int(value)
        if request.user.ratingmodel_set.filter(item=item).exists() and value <= 10:
            r = request.user.ratingmodel_set.get(item=item)
            r.rating = value
            r.save()
            item.rating = RatingModel.objects.filter(item=item).aggregate(result=Avg('rating'))['result']
            item.save()
            return JsonResponse({'status':'updated'})
        else:
            item.ratingcount += 1
            RatingModel(user=request.user,rating=value,item=item).save()
            item.rating = RatingModel.objects.filter(item=item).aggregate(result=Avg('rating'))['result']
            item.save()
            return JsonResponse({'status':'added'})
    return JsonResponse({'status':False})



def addwatchlist(request,pk):
    if request.user.is_authenticated:
        item = ItemModel.objects.get(pk=pk)
        if request.user.watchlist_set.filter(item=item).exists(): return JsonResponse({'status':'exists'})
        WatchList(user=request.user, item=item).save()
        return JsonResponse({'status':'done'})