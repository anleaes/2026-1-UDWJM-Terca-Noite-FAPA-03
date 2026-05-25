from django.shortcuts import render, redirect, get_object_or_404

from .forms import EmployeeForm
from .models import Employee


def add_employee(request):
    template_name = 'employees/add_employee.html'
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('employees:list_employees')
    else:
        form = EmployeeForm()
    return render(request, template_name, {'form': form})


def list_employees(request):
    template_name = 'employees/list_employees.html'
    employees = Employee.objects.filter()
    context = {'employees': employees}
    return render(request, template_name, context)


def edit_employee(request, id_employee):
    template_name = 'employees/add_employee.html'
    employee = get_object_or_404(Employee, id=id_employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:list_employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, template_name, {'form': form})


def delete_employee(request, id_employee):
    employee = get_object_or_404(Employee, id=id_employee)
    employee.delete()
    return redirect('employees:list_employees')
