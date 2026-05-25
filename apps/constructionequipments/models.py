from django.db import models
from constructions.models import Construction
from equipments.models import Equipment


class ConstructionEquipment(models.Model):
    allocation_date = models.DateField('Data de alocação')
    return_date = models.DateField('Data de devolução', null=True, blank=True)
    usage_cost = models.DecimalField('Custo de uso (R$)', max_digits=10, decimal_places=2, default=0)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE, verbose_name='Obra')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Equipamento')

    class Meta:
        verbose_name = 'Construction Equipment'
        verbose_name_plural = 'Construction Equipments'
        ordering = ['id']

    def __str__(self):
        return f'{self.equipment} — {self.construction}'
