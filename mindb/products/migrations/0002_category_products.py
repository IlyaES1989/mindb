# Generated by Django 4.1.3 on 2022-11-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, through='products.Pair', to='products.product', verbose_name='категории'),
        ),
    ]
