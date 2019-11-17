from django.db import models

# Create your models here.

class Cuenta(models.Model):
    Nombre = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)
    Pass1 = models.CharField(max_length=30)
    Pass2 = models.CharField(max_length=30)
    Fono = models.CharField(max_length=9)
    Fecha = models.DateTimeField(auto_now=True)


    def CuentaUsuario(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.Nombre, self.Fecha, self.Pass1)

    def __str__(self):
        return self.CuentaUsuario()

class Contactanos(models.Model):
    Nombre = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)
    Messg = models.CharField(max_length=300)

    def __str__(self):
        return "{0} {1}".format(self.Nombre, self.Email)

