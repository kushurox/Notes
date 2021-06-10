from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='notes-home'),
    path('notes', views.notes, name='notes-notes'),
    path('new', views.new_note, name='notes-new'),
    path('info/<str:title>', views.info)
]
