from django.shortcuts import render, redirect, get_object_or_404
from .forms import InspectionForm
from .models import Inspection


def add_inspection(request):
    template_name = 'inspections/add_inspection.html'
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save(commit=False)
            inspection.save()
            form.save_m2m()
            return redirect('inspections:list_inspection')
    else:
        form = InspectionForm()
    return render(request, template_name, {'form': form})


def list_inspection(request):
    template_name = 'inspections/list_inspection.html'
    inspections = Inspection.objects.all()
    context = {'inspections': inspections}
    return render(request, template_name, context)


def edit_inspection(request, id_inspection):
    template_name = 'inspections/add_inspection.html'
    inspection = get_object_or_404(Inspection, id=id_inspection)
    if request.method == 'POST':
        form = InspectionForm(request.POST, instance=inspection)
        if form.is_valid():
            form.save()
            return redirect('inspections:list_inspection')
    else:
        form = InspectionForm(instance=inspection)
    return render(request, template_name, {'form': form})


def delete_inspection(request, id_inspection):
    inspection = get_object_or_404(Inspection, id=id_inspection)
    inspection.delete()
    return redirect('inspections:list_inspection')
