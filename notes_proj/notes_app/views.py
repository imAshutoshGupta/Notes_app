from django.shortcuts import render, redirect, HttpResponse
from .models import Notes
# Create your views here.

def create(request):
    
    if request.method == 'POST':
        t = request.POST['ititle']
        c = request.POST['icontent']
        print(t)
        print(c)

        o = Notes.objects.create(title = t, content = c)
        print(o)
        o.save()
        #return HttpResponse("data inserted")
        return redirect('/dash')
    else:
        return render(request,'notes_app/addnotes.html')
    
def dash(request):
    o = Notes.objects.all()
    context = {}
    context['notes'] = o

    return render(request, 'notes_app/dashboard.html', context)

def update(request):
    #if request.method == 'POST':


    return render(request, 'notes_app/updatenotes.html')
def delete(request,rid):
    o = Notes.objects.filter(id=rid)
    o.delete()
    return redirect('/dash')
