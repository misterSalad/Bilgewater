# Generated by Django 5.0.6 on 2024-06-05 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0009_alter_bohater_emblemat_alter_bohater_pozycja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bohater',
            name='emblemat',
        ),
        migrations.RemoveField(
            model_name='bohater',
            name='pozycja',
        ),
    ]
