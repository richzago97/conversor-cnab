from django.db import models


from django.core.validators import MaxValueValidator, MinValueValidator


class TransactionModel(models.Model):
    type = models.PositiveSmallIntegerField(
        null=False, validators=[MinValueValidator(1), MaxValueValidator(9)]
    )
    date = models.DateField(null=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cpf = models.CharField(max_length=11, null=False)
    card = models.CharField(max_length=12, null=False)
    time = models.TimeField(null=False)
    owner_store = models.CharField(max_length=14, null=False)
    name_store = models.CharField(max_length=19, null=False)
