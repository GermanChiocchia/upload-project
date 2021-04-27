from django.db import models


# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=150, default='Imagen')
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name