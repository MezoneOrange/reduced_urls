# Generated by Django 3.0.6 on 2020-06-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200605_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='reduced_link',
            field=models.CharField(max_length=50, unique=True, verbose_name='Сокращенная ссылка'),
        ),
    ]