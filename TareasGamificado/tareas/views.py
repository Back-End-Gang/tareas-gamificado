from django.contrib.auth import views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Tarea
from logros.models import Logro

@login_required
def crear_tarea(request):
    logros = Logro.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        logro_id = request.POST.get('categoria')
        logro = Logro.objects.get(id=logro_id) if logro_id else None

        Tarea.objects.create(nombre=nombre,descripcion=descripcion,logro=logro)
        return redirect('listar_tarea')
    return render(request,'crear.html', {'logros': logros})

def listar_tareas(request):
    tareas = Tarea.objects.select_related('logro').all().order_by('-fecha_creacion')
    print(tareas)
    paginator = Paginator(tareas, 10)  # 5 tareas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #contexto = {'tareas':tareas}
    return render(request,'listar_tareas.html', {'page_obj': page_obj} )

@login_required
def actualizar_tarea(request,id):
    #contexto={}
    tarea=get_object_or_404(Tarea,id=id)
    logros = Logro.objects.all()
    print(tarea.titulo)
    print(tarea.descripcion)
    if request.method == 'POST':
        tarea.nombre = request.POST.get('nombre')
        tarea.descripcion = request.POST.get('descripcion')
        logro_id = request.POST.get('logro')
        tarea.logro = Logro.objects.get(id=logro_id) if logro_id else None

        tarea.save()
        #contexto = {'tarea':tarea}
        return redirect('listar_tarea')
    return render(request,'actualizar_tarea.html',{'tarea':tarea, 'logros': logros})

@login_required
def eliminar_tarea(request, id):
    #contexto={}
    tarea=get_object_or_404(Tarea,id=id)
    if request.method == 'POST':
        tarea.delete()
        #contexto = {'tarea':tarea}
        return redirect('listar_tarea')
    return render(request,'eliminar_tarea.html',{'tarea':tarea})