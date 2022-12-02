import random
from django.db import models
from django.urls import reverse
from django.conf import settings

import config.cute_logging as clog


class Good(models.Model):
    artikul = models.PositiveIntegerField('Артикул', blank=True,
                                          null=True, unique=True)
    title = models.CharField('Заголовок', max_length=20)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена')
    buy_amount = models.PositiveIntegerField('Кол-во раз купили',
                                             blank=True, null=True, default=0)
    image_link = models.URLField(max_length=200,
                                 default=settings.NON_IMAGE_URL)

    def save(self, *args, **kwargs):
        if self.artikul is None:
            rnint = random.randint(100_000, 999_999)
            while Good.objects.filter(artikul=rnint).exists():
                clog.message(f'[Good model log]{rnint} already used',
                             clog.WARNING)
                rnint = random.randint(100_000, 999_999)
            self.artikul = rnint
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('good_detail', kwargs={'id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'artikul']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
