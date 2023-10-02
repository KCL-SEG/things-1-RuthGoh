from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Thing(models.Model):
    """ def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity """

    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
    )
    description = models.CharField(
        max_length=120,
        unique=False,
        blank=True,
    )
    quantity = models.PositiveIntegerField(
        unique=False,
        validators=[
            MaxValueValidator(100, message='Must be <= 100.'),
            MinValueValidator(0, message='Must be >= 0.')
        ]
    )
