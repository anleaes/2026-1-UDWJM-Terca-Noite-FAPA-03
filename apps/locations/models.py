from django.db import models


class Location(models.Model):
    TYPE_CHOICES = [
        ('RUA', 'Rua'),
        ('AVENIDA', 'Avenida'),
        ('PRACA', 'Praça'),
        ('PARQUE', 'Parque'),
        ('VIELA', 'Viela'),
        ('OUTRO', 'Outro'),
    ]

    name = models.CharField('Nome', max_length=200)
    neighborhood = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=100)
    type = models.CharField('Tipo', max_length=20, choices=TYPE_CHOICES)
    is_paved = models.BooleanField('Pavimentado', default=False)

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'
        ordering = ['id']

    def __str__(self):
        return self.name
