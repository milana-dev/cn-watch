# Generated by Django 5.1.2 on 2024-11-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0003_remove_watches_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watches',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]