from django.shortcuts import render, redirect, get_object_or_404
from .models import Image_data, Project_images
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from .email_code import email_check


def index(request):
    # блок отправки письма
    form = email_check(request)
    mi_foto1 = Image_data.objects.filter(title='mi_foto1')
    mi_foto2 = Image_data.objects.filter(title='mi_foto2')
    return render(request, 'index.html', {'mi_foto2': mi_foto2, 'mi_foto1': mi_foto1, 'form': form})




def projects(request):
    # блок отправки письма
    form = email_check(request)
    return render(request, 'projects.html', {'form': form})



def maria_project(request):
    maria_project_img = Project_images.objects.filter(title='maria_project')
    maria_project_control_admin = Project_images.objects.filter(title='maria_project_control_admin')
    maria_project_docker = Project_images.objects.filter(title='maria_project_docker')
    form = email_check(request)
    return render(request, 'maria_project.html',
                  {'form': form,
                      'maria_project': maria_project_img,
                      'maria_project_control_admin': maria_project_control_admin,
                      'maria_project_docker': maria_project_docker})


# def control_project(request):
#     control_project_img = Project_images.objects.filter(title='control_project')
#     return render(request, 'maria_project.html', {'control_project': control_project_img})