from django.db import models


class Person(models.Model):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    national_id = models.CharField('CPF', max_length=14)
    address = models.CharField('Endereço', max_length=255)
    phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')

    class Meta:
        abstract = True


class Employee(Person):
    salary = models.DecimalField('Salário', max_digits=10, decimal_places=2)
    position = models.CharField('Cargo', max_length=100)
    hire_date = models.DateField('Data de contratação')
    is_active = models.BooleanField('Ativo', default=True)
    # company = models.ForeignKey('companies.Company', verbose_name='Empresa', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
