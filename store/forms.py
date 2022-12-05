from django.forms import ModelForm

from .models import Store
from account.models import User


class StoreForm(ModelForm):
    class Meta:
        model = User
        fields = ('accepted_store',)
