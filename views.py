from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseRedirect
# Create your views here.

from notes.models import Notes

def WriteNotes(request):
    if request.method == "POST":
        notes2 = Notes()
        notes2.title = request.POST.get("title")
        notes2.content = request.POST.get("content")
        notes2.save()
    
    return render(request, "writenotes.html")

def ShowNotes(request):
    notes_list = Notes.objects.all()
    return render(request, "notes.html", {"notes_list": notes_list})

def NotesDetails(request,notes_id):
    note = Notes.objects.get(id=notes_id)
    notes_list = Notes.objects.all()
    notes_pre = Notes.objects.filter(id__lt=notes_id).all().order_by("-id").first() #小于本条的降序第一个
    notes_aft = Notes.objects.filter(id__gt=notes_id).all().order_by("id").first() #大于本条的第一个
    return render(request, "notesdetails.html", {"note": note,"notes_pre": notes_pre,"notes_aft": notes_aft,"notes_list": notes_list})

def delete_note(request,delete_id):
    Notes.objects.filter(id=delete_id).delete()
    return HttpResponseRedirect('/notes')