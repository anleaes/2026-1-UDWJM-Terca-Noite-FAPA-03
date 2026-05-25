from django.db import models
from employees.models import Person


class Citizen(Person):
    registration_number = models.CharField('Número de cadastro', max_length=50)
    neighborhood_association = models.CharField('Associação de bairro', max_length=200)

    class Meta:
        verbose_name = 'Cidadão'
        verbose_name_plural = 'Cidadãos'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
