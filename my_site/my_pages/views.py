from django.shortcuts import render, redirect, get_object_or_404
from .models import Image_data


def index(request):
    mi_foto1 = Image_data.objects.filter(title='mi_foto1')
    return render(request, 'index.html', {'mi_foto1': mi_foto1})


def about_me(request):
    return render(request, 'about_me.html')


def projects(request):
    return render(request, 'projects.html')