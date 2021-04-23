from django.db import models
from django.utils import timezone
from django import forms



class Libro(models.Model):
  titulo = models.CharField(max_length=200, primary_key=True)
  autor  = models.CharField(max_length=100)
  imdb = models.CharField(max_length=20)
  genero = models.CharField(max_length=20)
  fecha_publi = models.DateField()
  #portada = models.ImageField(upload_to='libros')

  

"""
class Usuario(models.Model):
  nombre=models.CharField(max_length=50, primary_key=True)
  ap1=models.CharField(max_length=50)
  ap2=models.CharField(max_length=50)
  email=models.CharField(max_length=100)
"""

class Prestamo(models.Model):
  usuario = models.CharField(max_length=200)
  libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
  fecha = models.DateField(default=timezone.now)


class LibroForm(forms.Form):
  titulo = forms.CharField(label='titulo', max_length=200, widget=forms.TextInput())
  autor = forms.CharField(label='autor', max_length=100, widget=forms.TextInput())
  imdb = forms.CharField(label= 'imdb', max_length=20, widget=forms.TextInput())
  genero = forms.CharField(label= 'genero', max_length=20, widget=forms.TextInput())
  fecha_publi = forms.DateField(label='fecha_publi', widget=forms.SelectDateWidget(years=range(1500,2020)))


class PrestamoForm(forms.Form):
  usuario = forms.CharField(label='usuario', max_length=200, widget=forms.TextInput())
  libro = forms.CharField(label='libro', widget=forms.TextInput())

class BorrarLibroForm(forms.Form):
  titulo = forms.CharField(label='titulo', max_length=200, widget=forms.TextInput())

  

def new_libro(titulo, autor, imdb, genero, fecha_publi):
  libro = Libro(titulo=titulo, autor=autor, imdb=imdb, genero=genero, fecha_publi=fecha_publi)
  libro.save()
  return 1

def new_prestamo(usuario, libro):
  idlibro=Libro.objects.get(titulo=libro)
  prestamo = Prestamo(usuario=usuario, libro=idlibro)
  prestamo.save()
  return 1

#PRÁCTICA 7

class LoginForm(forms.Form):
  usuario=forms.CharField(label='usuario', max_length=200, widget=forms.TextInput())
  password=forms.CharField(label='password', max_length=50, widget=forms.TextInput())