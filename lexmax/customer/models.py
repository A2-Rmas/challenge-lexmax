from django.db import models
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    name = models.CharField(
        _('Nombre'), 
        max_length=50
    )
    lastname = models.CharField(
        _('Apellido'),
        max_length=50
    )
    email = models.EmailField(
        _('Correo electrónico'),
    )
    address = models.CharField(
        _('Dirrecion'), 
        max_length=50,
        null=True,
        blank=True
    )
    reference_address = models.CharField(
        _('Referencia de la dirección'),
        max_length=50,
        null=True,
        blank=True
    )
    phone = models.CharField(
        _('Teléfono'), 
        max_length=20,
        null=True,
        blank=True
    )
   
    created_at = models.DateTimeField(
        _('Created at'), 
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated at'), 
        auto_now=True
    )

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
        ordering = ['-created_at']

    def __str__(self):
        return self.name
