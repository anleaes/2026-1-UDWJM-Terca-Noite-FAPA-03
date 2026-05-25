from django.db import models


class Location(models.Model):
    TYPE_CHOICES = [
        ('street', 'Rua'),
        ('avenue', 'Avenida'),
        ('square', 'Praça'),
        ('park', 'Parque'),
        ('highway', 'Rodovia'),
    ]

    name = models.CharField('Nome', max_length=150)
    neighborhood = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=100)
    type = models.CharField('Tipo', max_length=20, choices=TYPE_CHOICES)
    is_paved = models.BooleanField('Pavimentado', default=False)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['id']

    def __str__(self):
        return self.name
