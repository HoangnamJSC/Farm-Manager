# Generated by Django 3.0.5 on 2020-06-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_salary',
            field=models.IntegerField(default=0),
        ),
    ]