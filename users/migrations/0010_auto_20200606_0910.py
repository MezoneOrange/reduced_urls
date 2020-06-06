# Generated by Django 3.0.6 on 2020-06-06 09:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200606_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='reduced_link',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MaxLengthValidator(50)], verbose_name='Сокращенная ссылка'),
        ),
    ]