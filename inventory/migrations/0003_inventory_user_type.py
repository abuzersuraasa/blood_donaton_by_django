# Generated by Django 3.2 on 2023-06-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_inventorymodel_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='user_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
