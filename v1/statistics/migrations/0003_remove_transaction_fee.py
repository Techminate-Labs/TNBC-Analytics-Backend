# Generated by Django 3.2.5 on 2021-08-17 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0002_auto_20210817_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='fee',
        ),
    ]
