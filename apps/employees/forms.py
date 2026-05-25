from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    hire_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
        label='Data de contratação',
    )

    class Meta:
        model = Employee
        exclude = ()
