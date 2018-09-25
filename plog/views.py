from django.shortcuts import render,get_object_or_404
from .models import plog

# Create your views here.
def allblogs(request):
    plogs=plog.objects
    return render(request,"plog/home.html",{"plogs":plogs})
def viewplog(request,blog_id):
    blog=get_object_or_404(plog,pk=blog_id)
    return render(request,"plog/viewplog.html",{"blog":blog})
