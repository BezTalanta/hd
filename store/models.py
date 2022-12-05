from django.db import models
from django.urls import reverse


class Store(models.Model):
    full_address = models.CharField('Полный адрес', max_length=200,
                                    unique=True)
    city = models.CharField('Город для отображения', max_length=50)
    description = models.TextField('Описание магазина', max_length=500)
    storage = models.ForeignKey("storage.storage", verbose_name="Склад",
                                on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_address

    def get_absolute_url(self):
        return reverse("store_detail", kwargs={"id": self.pk})

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['city']


class History(models.Model):
    user = models.ForeignKey("account.user", verbose_name="Пользователь",
                             on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Store, verbose_name="Магазин",
                              on_delete=models.SET_NULL, null=True)
    good = models.ForeignKey("good.good", verbose_name="Товар",
                             on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField("Дата покупки", auto_now_add=True)

    def __str__(self):
        return f'{self.user} купил {self.good}'

    class Meta:
        verbose_name = 'История покупок'
        verbose_name_plural = 'Истории покупок'
