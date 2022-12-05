from django.db import models


class Storage(models.Model):
    shortcut = models.CharField('Короткое название', max_length=20)
    full_address = models.CharField('Полный адресс', max_length=100)

    def __str__(self):
        return self.shortcut

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
