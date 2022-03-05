from django.db import models


class Matter(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=500, null=True)
    hours_number = models.IntegerField(null=True)

    def __str__(self):
        return self.name
