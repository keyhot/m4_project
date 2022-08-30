from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    bottles_ordered = models.IntegerField(default=0)
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to="photos",
        null=True,
        blank=True
    )
