# Generated by Django 4.1.2 on 2023-06-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0044_alter_contractemployment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
