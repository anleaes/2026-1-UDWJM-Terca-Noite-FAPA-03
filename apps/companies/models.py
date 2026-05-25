from django.db import models


class Company(models.Model):
    corporate_name = models.CharField('Razão social', max_length=150)
    corporate_tax_id = models.CharField('CNPJ', max_length=18)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone', max_length=20)
    is_active = models.BooleanField('Ativa', default=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['id']

    def __str__(self):
        return self.corporate_name
