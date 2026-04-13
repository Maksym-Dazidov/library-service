from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    class Cover(models.TextChoices):
        HARD = 'HARD', 'Hardcover'
        SOFT = 'SOFT', 'Softcover'

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.CharField(max_length=10, choices=Cover.choices)
    inventory = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )
    daily_fee = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )

    def __str__(self):
        return self.title
