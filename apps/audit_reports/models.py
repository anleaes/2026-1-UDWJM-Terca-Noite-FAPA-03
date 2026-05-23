from django.db import models
from inspections.models import Inspection


class AuditReport(models.Model):
    number = models.CharField('Número', max_length=50)
    issue_date = models.DateField('Data de Emissão')
    conclusion = models.TextField('Conclusão')
    is_approved = models.BooleanField('Aprovado', default=False)
    inspection = models.OneToOneField(Inspection, on_delete=models.PROTECT, verbose_name='Inspeção')

    class Meta:
        verbose_name = 'Audit Report'
        verbose_name_plural = 'Audit Reports'
        ordering = ['-issue_date']

    def __str__(self):
        return self.number
