from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    signing_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'},
            format='%Y-%m-%d',
        ),
        input_formats=['%Y-%m-%d'],
        label='Data de assinatura',
    )

    class Meta:
        model = Contract
        exclude = ()
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'validity_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'construction': forms.Select(attrs={'class': 'form-select'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
        }
