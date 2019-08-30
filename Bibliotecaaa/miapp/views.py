from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Libro, Ejemplar, Prestamo

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin




def cargar_inicio(request):
    return render(request, "miapp/index.html")

class LibroList(ListView):
    model = Libro
    template_name = 'miapp/lista_libros.html'

class LibroDetalle(DetailView):
    model = Libro
    template_name = 'miapp/detalle_libro.html'

class LibroCreate(LoginRequiredMixin,CreateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/nuevo_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroUpdate(UpdateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/actualizar_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroDelete(LoginRequiredMixin,DeleteView):
    model = Libro
    template_name = 'miapp/eliminar_libro.html'
    success_url = reverse_lazy('listar_libros')

class EjemplarList(ListView):
    model = Ejemplar
    template_name ='miapp/ejemplares.html'

class EjemplarDetalle(DetailView):
    model = Ejemplar
    template_name = 'miapp/detalle_ejemplar.html'

class EjemplarCreate(LoginRequiredMixin,CreateView):
    model = Ejemplar
    fields = ['numeroejemplar','fechadecompra','libro']
    template_name = 'miapp/nuevo_ejemplar.html'
    success_url = reverse_lazy('ejemplar_libro')

class EjemplarUpdate(UpdateView):
    model = Ejemplar
    fields = ['numeroejemplar','fechadecompra','libro']
    template_name = 'miapp/actualizar_ejemplar.html'
    success_url = reverse_lazy('ejemplar_libro')


class EjemplarDelete(LoginRequiredMixin,DeleteView):
    model = Ejemplar
    template_name = 'miapp/eliminar_ejemplar.html'
    success_url = reverse_lazy('ejemplar_libro')

class PrestamoList(ListView):
    model = Prestamo
    template_name ='miapp/prestamo.html'

class PrestamoCreate(LoginRequiredMixin,CreateView):
    model = Prestamo
    fields = ['fechaprestamo','nombre_cliente','telefono','estado']
    template_name = 'miapp/nuevo_prestamo.html'
    success_url = reverse_lazy('prestamo_libros')

class PrestamoUpdate(UpdateView):
    model = Prestamo
    fields = ['fechaprestamo','nombre_cliente','telefono','estado']
    template_name = 'miapp/actualizar_prestamo.html'
    success_url = reverse_lazy('prestamo_libros')

class PrestamoDelete(LoginRequiredMixin,DeleteView):
    model = Prestamo
    template_name = 'miapp/eliminar_prestamo.html'
    success_url = reverse_lazy('prestamo_libros')

class PrestamoDetalle(DetailView):
    model = Prestamo
    template_name = 'miapp/detalle_prestamo.html'

    



