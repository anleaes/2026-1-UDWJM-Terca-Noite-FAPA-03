from django.db import models
from constructions.models import Construction
from companies.models import Company


class Contract(models.Model):
    number = models.CharField('Número', max_length=20)
    signing_date = models.DateField('Data de Assinatura')
    value = models.DecimalField('Valor', max_digits=14, decimal_places=2)
    validity_days = models.IntegerField('Dias de Validade')
    document = models.FileField('Documento', upload_to='docs/', blank=True, null=True)
    is_active = models.BooleanField('Ativo', default=True)
    construction = models.ForeignKey(Construction, on_delete=models.PROTECT, verbose_name='Obra')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'
        ordering = ['id']

    def __str__(self):
        return self.number
