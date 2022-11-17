from django.shortcuts import render

# Create your views here.

from rate.models import message

def insert(request):
    if request.method == "POST":
        message2 = message()
        message2.institute = request.POST.get("institute")
        message2.star = request.POST.get("star")
        message2.comment = request.POST.get("comment")
        message2.save()
    
    return render(request, "insert.html")

def list(request):
    message_list = message.objects.all()
    return render(request, "show.html", {"message_list": message_list})

def search(request):
    return render(request, "search.html")

def list_filter(request):
    if request.method == "POST":
        searchinstitute = request.POST.get("searchinstitute")
        searchstar = request.POST.get("searchstar")
        searchcomment = request.POST.get("searchcomment")
    message_list = message.objects.filter(institute__icontains=searchinstitute).filter(star__icontains=searchstar).filter(comment__icontains=searchcomment)
    return render(request, "show.html", {"message_list": message_list})
