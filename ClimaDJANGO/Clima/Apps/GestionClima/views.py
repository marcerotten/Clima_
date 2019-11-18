from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import *
from .forms import *


# Create your views here.
#cuenta para listar usuarios inicio
def listado(request):
    cuentas = Cuenta.objects.all()
    fono = 123456789  # Filtro por defecto

    if request.POST.get('fono'):
        fono = int(request.POST.get('fono'))
        cuentas = cuentas.filter(fono__gte=fono)

    return render(request, "core/list.html", {'cuentas': cuentas, 'fono': fono})
#cuenta para listar usuarios fin


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


def add(request):
    # Creamos un formulario vacío
    form = TipoUserForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = TipoUserForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "core/add.html", {'form': form})


def edit(request, tipoUser_id):
    # Recuperamos la instancia de la persona
    instancia = TipoUser.objects.get(id=tipoUser_id)

    # Creamos el formulario con los datos de la instancia
    form = TipoUserForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = TipoUserForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "core/edit.html", {'form': form})


def delete(request, tipoUser_id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = TipoUser.objects.get(id=tipoUser_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('/')



