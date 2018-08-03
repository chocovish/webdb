from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import ItemModel
from .forms import CreateForm


def itemlist(request):
    queryset = ItemModel.objects.all().order_by("-pk")
    return render(request, 'webdb/list.html', {'queryset':queryset})


def details(request, pk):
    queryset = ItemModel.objects.get(pk=pk)
    return render(request, 'webdb/details.html', {'q':queryset})

def rateitem(request,pk,value):
    value = int(value)
    if value <= 10:
        i = ItemModel.objects.get(pk=pk)
        i.ratingcount += 1
        i.rating = float(i.rating) + value/i.ratingcount
        i.save()
        return JsonResponse({'status':'ok'})
    return JsonResponse({'status':'error'})


def create(request):
    if request.method=='POST':
        form = CreateForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("success")
    
    form = CreateForm()
    return render(request, 'webdb/create.html', {'form': form})

