from django.db import models
from constructions.models import Construction
from citizens.models import Citizen


class Incident(models.Model):
    TYPE_CHOICES = [
        ('accident', 'Acidente'),
        ('structural', 'Problema Estrutural'),
        ('environmental', 'Dano Ambiental'),
        ('vandalism', 'Vandalismo'),
        ('delay', 'Atraso'),
        ('other', 'Outro'),
    ]

    description = models.TextField('Descrição')
    type = models.CharField('Tipo', max_length=20, choices=TYPE_CHOICES)
    occurred_at = models.DateTimeField('Ocorrido em')
    severity = models.IntegerField('Severidade (1-5)')
    is_resolved = models.BooleanField('Resolvido', default=False)
    construction = models.ForeignKey(Construction, on_delete=models.PROTECT, verbose_name='Obra')
    reported_by = models.ForeignKey(Citizen, on_delete=models.PROTECT, verbose_name='Reportado por')

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'
        ordering = ['-occurred_at']

    def __str__(self):
        return f'{self.get_type_display()} — {self.construction}'
