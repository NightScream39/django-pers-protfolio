# Generated by Django 4.0.5 on 2022-07-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(default='Samsung/Apple/LG/Xiaomi...etc', max_length=50),
        ),
    ]
