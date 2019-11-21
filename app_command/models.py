from django.db import models


class SaveBirth(models.Model):
    name = models.CharField(max_length=30)
    birth_day = models.DateField(blank=True, null=True)
