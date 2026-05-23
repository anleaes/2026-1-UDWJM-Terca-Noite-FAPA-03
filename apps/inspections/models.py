from django.db import models
from constructions.models import Construction
from employees.models import Employee


class Inspection(models.Model):
    STATUS_CHOICES = [
        ('regular', 'Regular'),
        ('irregular', 'Irregular'),
        ('partial', 'Parcialmente Regular'),
        ('critical', 'Crítico'),
    ]

    visit_date = models.DateTimeField('Data da Visita')
    status_found = models.CharField('Status Encontrado', max_length=20, choices=STATUS_CHOICES)
    description = models.TextField('Descrição')
    is_compliant = models.BooleanField('Em Conformidade', default=False)
    score = models.FloatField('Pontuação')
    construction = models.ForeignKey(Construction, on_delete=models.PROTECT, verbose_name='Obra')
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='Fiscal')

    class Meta:
        verbose_name = 'Inspection'
        verbose_name_plural = 'Inspections'
        ordering = ['-visit_date']

    def __str__(self):
        return f'{self.construction} — {self.visit_date:%d/%m/%Y}'
