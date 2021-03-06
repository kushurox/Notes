from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from django.shortcuts import render, redirect
from .models import Note
from .forms import NewNote, EditNote
from collections import defaultdict


def home(req):
    """
    Manages The logic for home.html
    """

    context = {
        "notes": Note.objects.order_by(
            Trunc('date_of_creation', 'date', output_field=DateTimeField()).desc(), '-date_of_creation'),
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
        error = False
        form = NewNote(req.POST)
        if form.is_valid():
            if form.save():
                return redirect('notes-home')
            else:
                error = True
                return render(req, 'notes/create_note.html', {'form': form, 'title': 'New Note!',
                                                              'error': error})

    form = NewNote()
    context = {
        'title': 'New Note!',
        'form': form
    }
    return render(req, 'notes/create_note.html', context)


def info(req, title):
    """
    Manages the logic for info.html
    """
    if req.method == "POST":
        if 'delete' in req.POST:
            Note.objects.filter(title=title)[0].delete()
            return redirect('notes-home')
        elif 'content' in req.POST:
            n = Note.objects.get(title=title)
            n.content = req.POST['content']
            n.save()


            # TODO pls ask someone for help later since this isn't working as of now

            # form.is_valid()

            # redirect them to diff page

    notes = Note.objects.filter(title=title)

    form = EditNote()

    context = {
        'title': title,
        'note_data': notes,
        'edit_form': form
    }
    return render(req, 'notes/info.html', context)
