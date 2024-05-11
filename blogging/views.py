from django.http import HttpResponse
from django.shortcuts import render
from bloggers.models import *

def home(request):
    blog = Blogger.objects.all()
    context = {'blog':blog}
    return render(request, 'home.html', context)