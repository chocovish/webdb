from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import item
from .forms import CreateForm


def itemlist(request):
    queryset = item.objects.all().order_by("-pk")
    return render(request, 'webdb/list.html', {'queryset':queryset})


def details(request, pk):
    queryset = item.objects.get(pk=pk)
    return render(request, 'webdb/details.html', {'q':queryset})


def create(request):
    if request.method=='POST':
        form = CreateForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse("success")
    
    form = CreateForm()
    return render(request, 'webdb/create.html', {'form': form})

