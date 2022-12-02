from django.forms import ModelForm

from .models import Good


class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = ['title', 'description',
                  'price', 'buy_amount',
                  'image_link']
