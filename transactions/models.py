from django.db import models

# Create your models here.


class Transaction(models.Model):
    file = models.FileField(upload_to="documents/")
