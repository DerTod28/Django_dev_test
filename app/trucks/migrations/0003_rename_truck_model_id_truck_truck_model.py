# Generated by Django 4.2 on 2023-04-24 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0002_alter_cargo_name_alter_cargo_truck_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truck',
            old_name='truck_model_id',
            new_name='truck_model',
        ),
    ]
