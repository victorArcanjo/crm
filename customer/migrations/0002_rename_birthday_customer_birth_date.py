# Generated by Django 3.2.6 on 2021-08-09 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='birthday',
            new_name='birth_date',
        ),
    ]
