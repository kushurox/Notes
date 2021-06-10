from django.shortcuts import render, redirect
from .models import Note
from .forms import NewNote
from collections import defaultdict


def home(req):
    """
    Manages The logic for home.html
    """
    context = {
        "notes": Note.objects.all()[::-1],
        "title": "Notes"
    }

    return render(req, 'notes/home.html', context)


def notes(req):
    """
    Manages the logic for notes.html
    """
    note_map = defaultdict(lambda: [])
    for i in Note.objects.all():
        note_map[i.category].append(i.title)

    return render(req, 'notes/notes.html', {'notes': note_map.items()})


def new_note(req):
    """
    Manages the logic for create_note.html
    """
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
