from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def blog_detail(request, pk):
    blog = get_object_or_404(Blogger, pk=pk)
    context = {'blog':blog}
    return render(request, 'blog_detail.html',context)