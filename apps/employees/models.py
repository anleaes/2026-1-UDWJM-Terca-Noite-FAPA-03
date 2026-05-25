from django.db import models


class Person(models.Model):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    national_id = models.CharField('CPF', max_length=14, unique=True)
    address = models.CharField('Endereco', max_length=200)
    phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Employee(Person):
    POSITION_CHOICES = [
        ('engineer', 'Engenheiro(a)'),
        ('architect', 'Arquiteto(a)'),
        ('foreman', 'Mestre de Obras'),
        ('inspector', 'Fiscal'),
        ('worker', 'Operario(a)'),
        ('manager', 'Gerente'),
    ]

    salary = models.DecimalField('Salario', max_digits=10, decimal_places=2)
    position = models.CharField('Cargo', max_length=30, choices=POSITION_CHOICES)
    hire_date = models.DateField('Data de Admissao')
    is_active = models.BooleanField('Ativo', default=True)
    company = models.ForeignKey('companies.Company', on_delete=models.PROTECT, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.get_position_display()}'
