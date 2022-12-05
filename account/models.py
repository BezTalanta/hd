from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USER_ROLES = (
        ('CL', 'Client'),
        ('SW', 'Store worker'),
        ('CW', 'Storage worker'),
        # ('CL', 'client'),
    )
    role = models.CharField(max_length=2, choices=USER_ROLES, default='CL')
    is_user_allow_to_dashboard = models.BooleanField(default=False)
    accepted_store = models.ForeignKey("store.store",
                                       verbose_name="Выбранный магазин",
                                       on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username
