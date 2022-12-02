from django.db import models
from django.urls import reverse


class Store(models.Model):
    x = models.PositiveSmallIntegerField('Широта')
    y = models.PositiveSmallIntegerField('Долгота')
    full_address = models.CharField('Полный адрес', max_length=200)
    city = models.CharField('Город для отображения', max_length=50)
    description = models.TextField('Описание магазина', max_length=500)

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return reverse("store_detail", kwargs={"id": self.pk})

    class Meta:
        unique_together = ['x', 'y', 'full_address']
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['city']
