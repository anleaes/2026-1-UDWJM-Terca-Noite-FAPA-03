from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .forms import ConstructionEquipmentForm
from .models import ConstructionEquipment


def add_constructionequipment(request):
    template_name = 'constructionequipments/add_constructionequipment.html'
    if request.method == 'POST':
        form = ConstructionEquipmentForm(request.POST)
        if form.is_valid():
            allocation = form.save(commit=False)
            allocation.save()
            form.save_m2m()
            allocation.equipment.is_available = False
            allocation.equipment.save()
            return redirect('constructionequipments:list_constructionequipment')
    else:
        form = ConstructionEquipmentForm()
    return render(request, template_name, {'form': form})


def list_constructionequipment(request):
    template_name = 'constructionequipments/list_constructionequipment.html'
    allocations = ConstructionEquipment.objects.all()
    context = {'allocations': allocations}
    return render(request, template_name, context)


def edit_constructionequipment(request, id_constructionequipment):
    template_name = 'constructionequipments/add_constructionequipment.html'
    allocation = get_object_or_404(ConstructionEquipment, id=id_constructionequipment)
    if request.method == 'POST':
        form = ConstructionEquipmentForm(request.POST, instance=allocation)
        if form.is_valid():
            updated = form.save(commit=False)
            if updated.return_date:
                daily_rate = updated.equipment.daily_rate
                days = (updated.return_date - updated.allocation_date).days
                updated.usage_cost = daily_rate * days
                updated.equipment.is_available = True
                updated.equipment.save()
            updated.save()
            return redirect('constructionequipments:list_constructionequipment')
    else:
        form = ConstructionEquipmentForm(instance=allocation)
    return render(request, template_name, {'form': form})


def delete_constructionequipment(request, id_constructionequipment):
    allocation = get_object_or_404(ConstructionEquipment, id=id_constructionequipment)
    allocation.equipment.is_available = True
    allocation.equipment.save()
    allocation.delete()
    return redirect('constructionequipments:list_constructionequipment')
