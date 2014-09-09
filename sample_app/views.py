from django.shortcuts import render
from django.conf import settings


from .models import Book


def home_view(request):

	#do something with Book model etc
    
    hello = "Hello world welcome to docker with Chromebook." 

    return render(request, "hello.html", {'hello': hello})
