from django import forms
from .models import Inspection


class InspectionForm(forms.ModelForm):
    visit_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M',
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
        label='Data da visita',
    )

    class Meta:
        model = Inspection
        exclude = ()
        widgets = {
            'status_found': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_compliant': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'construction': forms.Select(attrs={'class': 'form-select'}),
            'employee': forms.Select(attrs={'class': 'form-select'}),
        }
