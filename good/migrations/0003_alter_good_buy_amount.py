# Generated by Django 4.1.3 on 2022-12-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0002_good_image_link_alter_good_artikul_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='buy_amount',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Кол-во раз купили'),
        ),
    ]
