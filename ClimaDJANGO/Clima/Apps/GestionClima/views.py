from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import *
from .forms import *


# Create your views here.

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
            Msj = "Registro Exitoso"
            cc_myself = "tareasduocav@gmail.com"

            recipients = ['tareasduocav@gmail.com']
            if cc_myself:

                recipients.append(Email)

                send_mail(Nombre, Msj, Email, recipients)
                register_form.save()
                print('Successful')
                return redirect('register')
        else:
            print('Fails')

    else:
        register_form = RegisterForm(request.POST)

    context = {
        "register_form": register_form,
    }
    template = 'core/register.html'
    return render(request, template, context)