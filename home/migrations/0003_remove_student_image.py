# Generated by Django 4.2.1 on 2023-05-07 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]