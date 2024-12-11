from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Usuario

# Create your views here.
@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    paginator = Paginator(usuarios, 5)  # 5 tareas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listar_usuarios.html', {'page_obj': page_obj})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        nivel = request.POST.get('nivel')
        Usuario.objects.create(correo=correo, nivel=nivel)
        return redirect('listar_usuarios')
    return render(request, 'crear_usuario.html')

@login_required
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.correo = request.POST.get('nombre')
        usuario.nivel = request.POST.get('nivel')
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'editar_usuario.html', {'usuario': usuario})

@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})