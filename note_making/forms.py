from django import forms
from .models import Note


class NewNote(forms.Form):
    title = forms.CharField(max_length=20, required=True,
                            widget=forms.TextInput(attrs={'class': "form-title",
                                                          'placeholder': 'Enter your title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-content',
                                                           'placeholder': 'Notes go here...'}), required=True)

    category = forms.CharField(max_length=20, required=True,
                               widget=forms.TextInput(attrs={'class': "form-title",
                                                             'placeholder': 'Enter your Category'}))

    def save(self) -> bool:
        if len(Note.objects.filter(title=self.cleaned_data['title'].title())) != 0:
            return False

        n = Note(title=self.cleaned_data['title'].title(),
                 content=self.cleaned_data['content'], category=self.cleaned_data['category'].title())
        n.save()
        return True


class EditNote(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': 'content',
                                                           'placeholder': 'Notes go here...'}),
                              disabled=True, label="", required=True)

    def edit(self, title):
        note = Note.objects.filter(title=title)[0]
        note.content = self.cleaned_data['content']
        note.save()
