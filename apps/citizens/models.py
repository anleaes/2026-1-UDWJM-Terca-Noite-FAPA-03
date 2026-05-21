from django.db import models
from employees.models import Person

# Create your models here.
class Citizen(Person):
    registration_number = models.CharField('Número de Cadastro', max_length=50)
    neighborhood_association = models.CharField('Associação de Bairro', max_length=200)

    class Meta:
        verbose_name = 'Citizen'
        verbose_name_plural = 'Citizens'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
