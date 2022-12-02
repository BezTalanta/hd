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

    def __str__(self):
        return self.username
