from django.shortcuts import render, redirect, get_object_or_404
from .models import Image_data
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


def index(request):
    # блок отправки письма
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['email'], 'erapyth@gmail.com',
                             ['moonanamiss@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Сообщение успешно отправлено')
                return redirect('index')
            else:
                messages.error(request, 'Письмо не отправлено')
        else:
            messages.error(request, 'Письмо не отправлено')
    else:
        form = ContactForm()

    mi_foto1 = Image_data.objects.filter(title='mi_foto1')
    return render(request, 'index.html', {'mi_foto1': mi_foto1, 'form': form})


def about_me(request):
    return render(request, 'about_me.html')


def projects(request):
    return render(request, 'projects.html')