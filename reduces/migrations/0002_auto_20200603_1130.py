# Generated by Django 3.0.6 on 2020-06-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reduces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='long_link',
            field=models.URLField(max_length=250),
        ),
    ]
