from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import *
from .forms import *
from django.contrib.auth import logout as do_logout


# Create your views here.

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "core/home.html")
    # En otro caso redireccionamos al login
    return redirect('core/index')

def home(request):
    return render(request, "core/home.html")

def index(request):
    return render(request, "core/index.html")

def statistics(request):
    return render(request, "core/statistics.html")

# def register(request):
#     return render(request, "core/register.html")

# def contact(request):
#     return render(request, "core/contact.html")

def navbar(request):
    return render(request, "core/navbar.html")


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            Nombre = contact_form.cleaned_data['Nombre']
            Email = contact_form.cleaned_data['Email']
            Messg = contact_form.cleaned_data['Messg']
            cc_myself = "tareasduocav@gmail.com"

            recipients = ['tareasduocav@gmail.com']
            if cc_myself:

                recipients.append(Email)

                send_mail(Nombre, Messg, Email, recipients)
                contact_form.save()
                print('Successful')
                return redirect('contact')
        else:
            print('Fails')

    else:
        contact_form = ContactForm(request.POST)

    context = {
        "contact_form": contact_form,
    }
    template = 'core/contact.html'
    return render(request, template, context)

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            Nombre = register_form.cleaned_data['Nombre']
            Email = register_form.cleaned_data['Email']
            Pass1 = register_form.cleaned_data['Pass1']
            Pass2 = register_form.cleaned_data['Pass2']
            Fono = register_form.cleaned_data['Fono']
            cc_myself = "tareasduocav@gmail.com"

            recipients = ['tareasduocav@gmail.com']
            if cc_myself:

                recipients.append(Email)

                send_mail(Nombre, Email, Pass1, Pass2,Fono, recipients)
                register_form.save()
                print('Successful')
                return redirect('contact')
        else:
            print('Fails')

    else:
        register_form = RegisterForm(request.POST)

    context = {
        "contact_form": register_form,
    }
    template = 'core/register.html'
    return render(request, template, context)