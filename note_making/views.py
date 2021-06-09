from django.shortcuts import render, redirect
from .models import Note
from .forms import NewNote


# Create your views here.

def home(req):
    context = {
        "notes": Note.objects.all(),
        "title": "Notes"
    }

    return render(req, 'notes/home.html', context)


def notes(req):
    return render(req, 'notes/notes.html')


def new_note(req):
    if req.method == "POST":
        form = NewNote(req.POST)
        if form.is_valid():
            form.save()
            return redirect('notes-home')

    form = NewNote()
    context = {
        'title': 'New Note!',
        'form': form
    }
    return render(req, 'notes/create_note.html', context)