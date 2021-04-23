from django.shortcuts import render
from .models import *
import sqlite3

from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

#Para autenticación
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    #return HttpResponse("Hello world")
    return render(request,'test.html')

def mostrar_libros(request):
    libros=Libro.objects.all()
    for libro in libros:
        print(libro.titulo)
        print(libro.autor)
    return render(request, 'mostrar_libros.html', {'mislibros':libros})

@staff_member_required
def crear_libro(request):
    #Crear una nueva instacia del modelo Libro y guardarla en la BD. 
    if request.method == 'POST':
        #Creamos una instancia del LibroForm
        form = LibroForm(request.POST)
        if form.is_valid():
            new_libro(form.cleaned_data['titulo'], form.cleaned_data['autor'],
            form.cleaned_data['imdb'], form.cleaned_data['genero'], form.cleaned_data['fecha_publi']  )
            return HttpResponseRedirect('libros', '/Libro guardado con éxito/')
        else:
            print(form.errors)
            return HttpResponse('/Algo ha fallado/')
    else:
        form = LibroForm()
        return render(request, 'crear_libro.html', {'form':form})


def mostrar_prestamos(request):
    #Devolvemos todas las instancias de prestamos
    listaprestamos=Prestamo.objects.all()
    return render(request, 'mostrar_prestamos.html', {'listaprestamos':listaprestamos})

@login_required
def crear_prestamo(request):
    #Crear una nueva instancia del modelo préstamo y guardarla en la BD.
    if request.method == 'POST':
        #Creamos una instancia del PrestamoForm
        form = PrestamoForm(request.POST)
        if form.is_valid():
            new_prestamo(form.cleaned_data['usuario'], form.cleaned_data['libro'])
            return HttpResponseRedirect('prestamos', '/Préstamo guardado con éxito/')
        else:
            print(form.errors)
            return HttpResponseRedirect('/Algo ha fallado/')
    else:
        form = PrestamoForm()
        return render(request, 'crear_prestamo.html', {'form':form})

@staff_member_required
def borrar_libro(request):
    #Borrar una instancia del modelo Libro de la BD.
    if request.method == 'POST':
        form = BorrarLibroForm(request.POST)
        if form.is_valid():
            try:
                objeto = Libro.objects.get(titulo=form.cleaned_data['titulo'])
                objecto.delete()
                return HttpResponseRedirect('libros', '/Libro eliminado con éxito/')
            except:
                return HttpResponseRedirect('libros', 'El libro introducido no existe')
        else:
            print(form.errors)
            return HttpResponseRedirect('/Algo ha fallado/')
    else:
        form = BorrarLibroForm()
        return render(request, 'borrar_libro.html', {'form':form})

@staff_member_required
def borrar_prestamo(request):
    #Borrar una instancia del modelo prestamo de la BD.
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            try:
                objeto = Prestamo.objects.get(usuario=form.cleaned_data['usuario'], libro=form.cleaned_data['libro'])
                objecto.delete()
                return HttpResponseRedirect('prestamos', '/Préstamo eliminado con éxito/')
            except:
                return HttpResponseRedirect('prestamos', 'El préstamo introducido no existe')
        else:
            print(form.errors)
            return HttpResponseRedirect('/Algo ha fallado/')
    else:
        form = BorrarLibroForm()
        return render(request, 'borrar_prestamo.html', {'form':form})

@staff_member_required
def editar_libro(request):
    #Editar una instancia del modelo prestamo de la BD.
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            try:
                objeto = Libro.objects.get(titulo=form.cleaned_data['titulo'])
                objecto.delete()
                new_libro(form.cleaned_data['titulo'], form.cleaned_data['autor'],
                form.cleaned_data['imdb'], form.cleaned_data['genero'], form.cleaned_data['fecha_publi'] )
                return HttpResponseRedirect('libros', '/Libro guardado con éxito/')
            except:
                return HttpResponseRedirect('libros', 'El libro introducido no existe')
        else:
            print(form.errors)
            return HttpResponseRedirect('/Algo ha fallado/')
    else:
        form = LibroForm()
        return render(request, 'editar_libro.html', {'form':form})

@login_required
def editar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            try:
                objeto = Prestamo.objects.get(usuario=form.cleaned_data['usuario'], libro=form.cleaned_data['libro'])
                objecto.delete()
                new_prestamo(form.cleaned_data['usuario'], form.cleaned_data['libro'])
                return HttpResponseRedirect('prestamos', '/Préstamo editado con éxito/')
            except:
                return HttpResponseRedirect('prestamos', '/Préstamo introducido erróneo/')
        else:
            print(form.errors)
            return HttpResponseRedirect('/Algo ha fallado/')
    else:
        form = PrestamoForm()
        return render(request, 'editar_prestamo.html', {'form':form})


#PRÁCTICA 7. Autenticación con Django-allauth

class Home(TemplateView):
    template_name = 'test.html'

"""
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #Procesar
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            #Procesar
    else:
        form=SignInForm()
        return render(request, 'signin.html', {'form':form})
"""