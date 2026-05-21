from django.db import models


class Company(models.Model):
    corporate_name = models.CharField('Razao Social', max_length=200)
    corporate_tax_id = models.CharField('CNPJ', max_length=18, unique=True)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone', max_length=20)
    is_active = models.BooleanField('Ativa', default=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['corporate_name']

    def __str__(self):
        return self.corporate_name
