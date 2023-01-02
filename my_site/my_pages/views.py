from django.shortcuts import render, redirect, get_object_or_404
from .models import Image_data, Project_images
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from .email_code import email_check





########################### RUS PART ###########################

def index(request):
    # блок отправки письма
    form = email_check(request)
    mi_foto1 = Image_data.objects.filter(title='mi_foto1')
    mi_foto2 = Image_data.objects.filter(title='mi_foto2')
    return render(request, 'ru_index.html', {'mi_foto2': mi_foto2, 'mi_foto1': mi_foto1, 'form': form})



def projects(request):
    # блок отправки письма
    form = email_check(request)
    return render(request, 'ru/projects.html', {'form': form})



def maria_project(request):
    maria_project_img = Project_images.objects.filter(title='maria_project')
    maria_project_control_admin = Project_images.objects.filter(title='maria_project_control_admin')
    maria_project_docker = Project_images.objects.filter(title='maria_project_docker')
    maria_style_css = Project_images.objects.filter(title='maria_project_style_dec')
    form = email_check(request)
    return render(request, 'ru/maria_project.html',
                  {'form': form,
                      'maria_project': maria_project_img,
                      'maria_project_control_admin': maria_project_control_admin,
                      'maria_project_docker': maria_project_docker,
                      'maria_style': maria_style_css})




########################### ENG PART ###########################

def eng_index(request):
    # блок отправки письма
    form = email_check(request)
    mi_foto1 = Image_data.objects.filter(title='mi_foto1')
    mi_foto2 = Image_data.objects.filter(title='mi_foto2')
    return render(request, 'eng_index.html', {'mi_foto2': mi_foto2, 'mi_foto1': mi_foto1, 'form': form})






########################### ESP PART ###########################

def esp_index(request):
    # блок отправки письма
    form = email_check(request)
    mi_foto1 = Image_data.objects.filter(title='mi_foto1')
    mi_foto2 = Image_data.objects.filter(title='mi_foto2')
    return render(request, 'esp_index.html', {'mi_foto2': mi_foto2, 'mi_foto1': mi_foto1, 'form': form})
