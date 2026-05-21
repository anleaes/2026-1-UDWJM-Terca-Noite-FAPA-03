from django.db import models
from companies.models import Company


class Equipment(models.Model):
    TYPE_CHOICES = [
        ('excavator', 'Escavadeira'),
        ('crane', 'Guindaste'),
        ('truck', 'Caminhão'),
        ('bulldozer', 'Bulldozer'),
        ('concrete_mixer', 'Betoneira'),
        ('compactor', 'Compactador'),
        ('other', 'Outro'),
    ]

    name = models.CharField('Nome', max_length=200)
    type = models.CharField('Tipo', max_length=20, choices=TYPE_CHOICES)
    daily_rate = models.DecimalField('Diária (R$)', max_digits=10, decimal_places=2)
    is_available = models.BooleanField('Disponível', default=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
        ordering = ['name']

    def __str__(self):
        return self.name
