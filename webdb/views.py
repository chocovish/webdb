from django.shortcuts import render,HttpResponse
from .models import ItemModel,RatingModel
from .forms import CreateForm


def itemlist(request):
    queryset = ItemModel.objects.all().order_by("-pk")
    return render(request, 'webdb/list.html', {'queryset':queryset})


def details(request, pk):
    query = ItemModel.objects.get(pk=pk)
    return render(request, 'webdb/details.html', {'q':query})

def userprofile(request):
    return render(request,'webdb/userprofile.html')


def create(request):
    if request.method=='POST':
        form = CreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
    form = CreateForm()
    return render(request, 'webdb/create.html', {'form': form})

