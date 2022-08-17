from django.shortcuts import render
#from django.views.generic import TemplateView, ListView
from .models import ModelformsProject
#from products.models import Project
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'modelForms/index.html')

def listProjects(request):
    projectsList=ModelformsProject.objects.all()
    return render(request,'modelForms/listProjects.html',{'projects':projectsList})

def search_results(request):
    projectsList=ModelformsProject.objects.all()
    return render(request,'modelForms/search_results.html',{'projects':projectsList})

def get_queryset(request): 
    projectsList = ModelformsProject.objects.filter(productTitle__icontains='pixel')
    return render(request,'modelForms/search_results.html',{'projects':projectsList})


def get_queryset1(request):  # new
        query = request.GET.get("q")
        object_list = ModelformsProject.objects.filter(Q(productTitle__icontains=query))
        return render(request,'modelForms/search_results.html',{'projects':object_list})