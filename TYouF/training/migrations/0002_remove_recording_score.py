# Generated by Django 4.2.6 on 2023-10-29 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='score',
        ),
    ]