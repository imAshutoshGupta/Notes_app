from django.shortcuts import render
from .models import Notes
# Create your views here.

def dash(request):
    o = Notes.objects.all()
    context = {'notes' : 'o'}

    return render(request, 'notes_app/dashboard.html', context)

def create(request):
    if request.method == 'GET':
        return render(request,'notes_app/addnotes.html')
    else:
        t = request.POST['ititle']
        c = request.POST['icontent']


        o = Notes.objects.create(title = t, content = c)
        o.save()

        return render(request, 'notes_app/addnotes.html')
def update(request):
    #if request.method == 'POST':


    return render(request, 'notes_app/updatenotes.html')
def delete(request):
    #if request.method == 'POST':


    return render(request, 'notes_app/dash.html')
