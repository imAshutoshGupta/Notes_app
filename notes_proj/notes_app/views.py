from django.shortcuts import render
from .models import Notes
# Create your views here.

def editor(request):
    note_id = int(request.GET.get('note_id',0))
    texts = Notes.objects.all()

    context = {
        'note_id' : note_id,
        'texts' : texts
    }

    return render(request, 'notes_app/editor.html', context)