# Generated by Django 2.2.7 on 2019-11-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactanos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=50)),
                ('Messg', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=50)),
                ('Pass1', models.CharField(max_length=30)),
                ('Pass2', models.CharField(max_length=30)),
                ('Fono', models.CharField(max_length=9)),
                ('Fecha', models.DateField()),
            ],
        ),
    ]
