# Generated by Django 4.2.1 on 2023-05-13 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeProject', '0007_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_name'], 'verbose_name': 'student'},
        ),
    ]
