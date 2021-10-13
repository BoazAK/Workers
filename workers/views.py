from django.shortcuts import render, redirect
from .forms import WorkersForm
from .models import Workers

def worker_list(request):
    context = {'workers_list' : Workers.objects.all()}
    return render(request, "workers/worker_list.html", context)


def worker_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = WorkersForm()
        else:
            worker = Workers.objects.get(pk = id)
            form = WorkersForm(instance = worker)
        return render(request, "workers/worker_form.html",{'form':form})
    else:
        if id == 0:
            form = WorkersForm(request.POST)
        else:
            worker = Workers.objects.get(pk = id)
            form = WorkersForm(request.POST, instance = worker)
        if form.is_valid():
            form.save()
        return redirect('/list')

def worker_delete(request, id):
    worker = Workers.objects.get(pk = id)
    worker.delete()
    return redirect('/list')
