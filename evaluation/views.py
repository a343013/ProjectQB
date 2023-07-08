from django.shortcuts import render, redirect, reverse
from .models import Agente, Inspector, Evaluacion
from .forms import AgenteForm, InspectorForm, EvaluacionForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def registrar(request):
    return render(request, 'registrar.html')

def consultar(request):
    consulta = request.GET.get('consulta')

    if consulta == 'agentes':
        agentes = Agente.objects.all()
        return render(request, 'consultar.html', {'consulta': consulta, 'agentes': agentes})
    elif consulta == 'inspectores':
        inspectores = Inspector.objects.all()
        return render(request, 'consultar.html', {'consulta': consulta, 'inspectores': inspectores})
    elif consulta == 'evaluaciones':
        evaluaciones = Evaluacion.objects.all().select_related('agente')
        return render(request, 'consultar.html', {'consulta': consulta, 'evaluaciones': evaluaciones})
    else:
        return render(request, 'consultar.html')

def modificar(request):
    agentes = Agente.objects.all()
    inspectores = Inspector.objects.all()
    evaluaciones = Evaluacion.objects.all()
    return render(request, 'modificar.html', {'agentes': agentes, 'inspectores': inspectores, 'evaluaciones': evaluaciones})

def crear_agente(request):
    if request.method == 'POST':
        form = AgenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar')
    else:
        form = AgenteForm()
    return render(request, 'crear_agente.html', {'form': form})

def crear_inspector(request):
    if request.method == 'POST':
        form = InspectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar')
    else:
        form = InspectorForm()
    return render(request, 'crear_inspector.html', {'form': form})


def crear_evaluacion(request):
    if request.method == 'POST':
        # Obtener los valores del formulario
        agente_id = request.POST.get('agente')
        inspector_id = request.POST.get('inspector')
        fecha = request.POST.get('fecha')
        interaccion = request.POST.get('interaccion')
        pregunta1 = request.POST.get('pregunta1')
        pregunta2 = request.POST.get('pregunta2')
        pregunta3 = request.POST.get('pregunta3')
        pregunta4 = request.POST.get('pregunta4')
        pregunta5 = request.POST.get('pregunta5')

        # Verificar si hay campos vacíos
        if not agente_id or not inspector_id or not fecha or not interaccion or not pregunta1 or not pregunta2 or not pregunta3 or not pregunta4 or not pregunta5:
            messages.error(request, 'Todos los campos son requeridos.')
            return HttpResponseRedirect(request.path_info)

        # Realizar los cálculos necesarios
        puntaje = 0
        if pregunta1 == 'si':
            puntaje += 20
        if pregunta2 == 'si':
            puntaje += 20
        if pregunta3 == 'si':
            puntaje += 20
        if pregunta4 == 'si':
            puntaje += 20
        if pregunta5 == 'si':
            puntaje += 20

        # Obtener el agente y el inspector seleccionados
        agente = Agente.objects.get(id=agente_id)
        inspector = Inspector.objects.get(id=inspector_id)

        # Guardar los datos en la base de datos
        evaluacion = Evaluacion(
            agente=agente,
            inspector=inspector,
            fecha=fecha,
            interaccion=interaccion,
            pregunta1=pregunta1,
            pregunta2=pregunta2,
            pregunta3=pregunta3,
            pregunta4=pregunta4,
            pregunta5=pregunta5,
            puntaje=puntaje
        )
        evaluacion.save()

        # Redireccionar a otra página o mostrar un mensaje de éxito
        messages.success(request, 'La evaluación se ha registrado exitosamente')
        return redirect('index') # Cambia 'editar_evaluacion.html' por el nombre de la vista o URL donde deseas redireccionar después de guardar la evaluación
    else:
        # Obtener la lista de agentes (probablemente desde la base de datos)
        agentes = Agente.objects.all()  # Ejemplo: suponiendo que tienes un modelo Agente

        # Obtener la lista de inspectores (probablemente desde la base de datos)
        inspectores = Inspector.objects.all()  # Ejemplo: suponiendo que tienes un modelo Inspector

        # Renderizar el formulario de creación de evaluación con las listas de agentes e inspectores
        context = {
            'agentes': agentes,
            'inspectores': inspectores,
        }
        return render(request, 'crear_evaluacion.html', context)

def editar_agente(request, pk):
    agente = Agente.objects.get(pk=pk)
    if request.method == 'POST':
        form = AgenteForm(request.POST, instance=agente)
        if form.is_valid():
            form.save()
            return redirect('modificar')
    else:
        form = AgenteForm(instance=agente)
    return render(request, 'editar_agente.html', {'form': form})

def editar_inspector(request, pk):
    inspector = Inspector.objects.get(pk=pk)
    if request.method == 'POST':
        form = InspectorForm(request.POST, instance=inspector)
        if form.is_valid():
            form.save()
            return redirect('modificar')
    else:
        form = InspectorForm(instance=inspector)
    return render(request, 'editar_inspector.html', {'form': form})

def editar_evaluacion(request, pk):
    evaluacion = Evaluacion.objects.get(pk=pk)
    puntaje_anterior = evaluacion.puntaje  # Obtén el puntaje anterior

    if request.method == 'POST':
        form = EvaluacionForm(request.POST, instance=evaluacion)
        if form.is_valid():
            evaluacion_modificada = form.save(commit=False)

            # Calcula el nuevo puntaje en base a las respuestas modificadas
            nuevo_puntaje = evaluacion_modificada.calcular_puntaje()

            evaluacion_modificada.puntaje = nuevo_puntaje
            evaluacion_modificada.save()

            return redirect('modificar')
    else:
        form = EvaluacionForm(instance=evaluacion)

    return render(request, 'editar_evaluacion.html', {'form': form})

def eliminar_agente(request, pk):
    agente = Agente.objects.get(pk=pk)
    agente.delete()
    return redirect('modificar')

def eliminar_inspector(request, pk):
    inspector = Inspector.objects.get(pk=pk)
    inspector.delete()
    return redirect('modificar')

def eliminar_evaluacion(request, pk):
    evaluacion = Evaluacion.objects.get(pk=pk)
    evaluacion.delete()
    return redirect('modificar')