# Generated by Django 4.1.2 on 2023-06-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageTool', '0045_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_details',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]