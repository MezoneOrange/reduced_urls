# Generated by Django 3.0.6 on 2020-06-05 08:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200605_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='long_link',
            field=models.URLField(max_length=250, validators=[django.core.validators.MaxLengthValidator(250), django.core.validators.URLValidator()], verbose_name='Длинная ссылка'),
        ),
    ]
