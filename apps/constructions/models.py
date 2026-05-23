from django.db import models
from companies.models import Company
from locations.models import Location
from employees.models import Employee


class Construction(models.Model):
    TYPE_CHOICES = [
        ('road', 'Rodovia'),
        ('bridge', 'Ponte'),
        ('building', 'Edifício'),
        ('sanitation', 'Saneamento'),
        ('urban', 'Urbanização'),
        ('other', 'Outro'),
    ]

    STATUS_CHOICES = [
        ('planned', 'Planejada'),
        ('in_progress', 'Em Andamento'),
        ('paused', 'Pausada'),
        ('completed', 'Concluída'),
        ('cancelled', 'Cancelada'),
    ]

    title = models.CharField('Título', max_length=200)
    type = models.CharField('Tipo', max_length=20, choices=TYPE_CHOICES)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='planned')
    start_date = models.DateField('Data de Início')
    expected_end_date = models.DateField('Previsão de Término')
    total_value = models.DecimalField('Valor Total (R$)', max_digits=14, decimal_places=2)
    is_completed = models.BooleanField('Concluída', default=False)
    photo = models.ImageField('Foto', upload_to='photos/', blank=True, null=True)
    report = models.FileField('Relatório', upload_to='docs/', blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, verbose_name='Localização')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Empresa')
    employees = models.ManyToManyField(Employee, verbose_name='Funcionários', blank=True)

    class Meta:
        verbose_name = 'Construction'
        verbose_name_plural = 'Constructions'
        ordering = ['id']

    def __str__(self):
        return self.title
