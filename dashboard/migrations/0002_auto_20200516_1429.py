# Generated by Django 3.0.5 on 2020-05-16 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='email',
            new_name='staff_email',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='name',
            new_name='staff_name',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='phone',
            new_name='staff_phone',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='position',
            new_name='staff_position',
        ),
    ]
